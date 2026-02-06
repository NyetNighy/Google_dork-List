#!/usr/bin/env python3
"""
Dork Runner - authorized search helper.

This tool is intended ONLY for systems you own or have explicit written
permission to test. Do not use this to violate laws or platform terms.
"""

import argparse
import csv
import json
import os
import shlex
import subprocess
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Iterable, List, Dict, Any, Optional

DEFAULT_KEYWORDS = {
    "index of": 4,
    "password": 8,
    "passwd": 8,
    "backup": 6,
    "db": 4,
    "database": 5,
    "config": 6,
    "secret": 7,
    "token": 7,
    "apikey": 7,
    "admin": 3,
    "login": 2,
    "sql": 5,
    "rce": 9,
    "xss": 6,
    "ssrf": 8,
    "lfi": 7,
    "rfi": 7,
    "env": 4,
    ".env": 7,
    "aws": 3,
    "s3": 4,
    "bucket": 4,
    "git": 3,
    ".git": 6,
    "backup.sql": 8,
}


@dataclass
class Result:
    dork: str
    title: str
    link: str
    snippet: str
    source: str
    score: int


def resolve_dorks_path(path: str) -> str:
    if os.path.isfile(path):
        return path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(script_dir, path)
    if os.path.isfile(candidate):
        return candidate
    raise FileNotFoundError(
        f"Dorks file not found: '{path}'. "
        "Pass --dorks-file with an absolute path or run from the repo root."
    )


def load_dorks(path: str) -> List[str]:
    dorks: List[str] = []
    resolved = resolve_dorks_path(path)
    with open(resolved, "r", encoding="utf-8") as handle:
        for line in handle:
            cleaned = line.strip()
            if not cleaned or cleaned.startswith("#"):
                continue
            dorks.append(cleaned)
    return dorks


def compute_score(text: str, keywords: Dict[str, int]) -> int:
    lowered = text.lower()
    score = 0
    for key, weight in keywords.items():
        if key in lowered:
            score += weight
    return score


def serpapi_search(
    query: str, api_key: str, max_results: int, engine: str
) -> List[Dict[str, Any]]:
    params = {
        "engine": engine,
        "q": query,
        "api_key": api_key,
        "num": max_results,
    }
    url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    results = []
    for item in payload.get("organic_results", [])[:max_results]:
        results.append(
            {
                "title": item.get("title", ""),
                "link": item.get("link", ""),
                "snippet": item.get("snippet", ""),
            }
        )
    return results


def shodan_search(query: str, api_key: str, page: int) -> List[Dict[str, Any]]:
    params = {
        "key": api_key,
        "query": query,
        "page": page,
    }
    url = "https://api.shodan.io/shodan/host/search?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    results = []
    for item in payload.get("matches", []):
        ip_str = item.get("ip_str", "")
        title = item.get("product") or item.get("org") or ip_str
        results.append(
            {
                "title": title,
                "link": f"https://www.shodan.io/host/{ip_str}" if ip_str else "",
                "snippet": item.get("data", ""),
            }
        )
    return results


def import_results(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if isinstance(payload, dict) and "results" in payload:
        payload = payload["results"]
    if not isinstance(payload, list):
        raise ValueError("Imported JSON must be a list of results")
    return payload


def parse_result_items(
    payload: Any,
    title_field: str,
    link_field: str,
    snippet_field: str,
    dork: str,
    source: str,
) -> List[Result]:
    if isinstance(payload, dict) and "results" in payload:
        payload = payload["results"]
    if not isinstance(payload, list):
        raise ValueError("External output must be a list of objects or contain a 'results' list")
    results: List[Result] = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        title = str(item.get(title_field, ""))
        link = str(item.get(link_field, ""))
        snippet = str(item.get(snippet_field, ""))
        text = " ".join([title, snippet, link])
        score = compute_score(text, DEFAULT_KEYWORDS)
        results.append(
            Result(
                dork=dork,
                title=title,
                link=link,
                snippet=snippet,
                source=source,
                score=score,
            )
        )
    return results


def external_search(
    query: str,
    command_template: str,
    parse_format: str,
    timeout_s: int,
    title_field: str,
    link_field: str,
    snippet_field: str,
) -> List[Result]:
    command = command_template.format(query=query)
    args = shlex.split(command)
    result = subprocess.run(
        args,
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout_s,
    )
    if parse_format == "json":
        payload = json.loads(result.stdout)
        return parse_result_items(payload, title_field, link_field, snippet_field, query, "external")
    if parse_format == "jsonl":
        lines = [line for line in result.stdout.splitlines() if line.strip()]
        payload = [json.loads(line) for line in lines]
        return parse_result_items(payload, title_field, link_field, snippet_field, query, "external")
    raise ValueError(f"Unsupported external parse format: {parse_format}")


def gather_results(
    dorks: Iterable[str],
    provider: str,
    max_results: int,
    delay_s: float,
    import_path: Optional[str],
    serpapi_engine: str,
    shodan_page: int,
    external_command: Optional[str],
    external_parse: str,
    external_timeout: int,
    external_title_field: str,
    external_link_field: str,
    external_snippet_field: str,
) -> List[Result]:
    results: List[Result] = []
    keywords = DEFAULT_KEYWORDS
    if provider == "import":
        imported = import_results(import_path or "")
        for item in imported:
            text = " ".join(
                [item.get("title", ""), item.get("snippet", ""), item.get("link", "")]
            )
            score = compute_score(text, keywords)
            results.append(
                Result(
                    dork=item.get("dork", ""),
                    title=item.get("title", ""),
                    link=item.get("link", ""),
                    snippet=item.get("snippet", ""),
                    source="import",
                    score=score,
                )
            )
        return results

    if provider == "serpapi":
        api_key = os.getenv("SERPAPI_API_KEY")
        if not api_key:
            raise RuntimeError("SERPAPI_API_KEY is required for provider=serpapi")
        for dork in dorks:
            items = serpapi_search(dork, api_key, max_results, serpapi_engine)
            for item in items:
                text = " ".join([item.get("title", ""), item.get("snippet", ""), item.get("link", "")])
                score = compute_score(text, keywords)
                results.append(
                    Result(
                        dork=dork,
                        title=item.get("title", ""),
                        link=item.get("link", ""),
                        snippet=item.get("snippet", ""),
                        source="serpapi",
                        score=score,
                    )
                )
            time.sleep(delay_s)
        return results

    if provider == "shodan":
        api_key = os.getenv("SHODAN_API_KEY")
        if not api_key:
            raise RuntimeError("SHODAN_API_KEY is required for provider=shodan")
        for dork in dorks:
            items = shodan_search(dork, api_key, shodan_page)
            for item in items:
                text = " ".join([item.get("title", ""), item.get("snippet", ""), item.get("link", "")])
                score = compute_score(text, keywords)
                results.append(
                    Result(
                        dork=dork,
                        title=item.get("title", ""),
                        link=item.get("link", ""),
                        snippet=item.get("snippet", ""),
                        source="shodan",
                        score=score,
                    )
                )
            time.sleep(delay_s)
        return results

    if provider == "external":
        if not external_command:
            raise RuntimeError("--external-command is required for provider=external")
        for dork in dorks:
            results.extend(
                external_search(
                    dork,
                    external_command,
                    external_parse,
                    external_timeout,
                    external_title_field,
                    external_link_field,
                    external_snippet_field,
                )
            )
            time.sleep(delay_s)
        return results

    raise ValueError(f"Unsupported provider: {provider}")


def export_results(results: List[Result], output: str, fmt: str) -> None:
    if fmt == "json":
        payload = [result.__dict__ for result in results]
        with open(output, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
        return

    if fmt == "csv":
        with open(output, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(Result.__annotations__.keys()))
            writer.writeheader()
            for result in results:
                writer.writerow(result.__dict__)
        return

    raise ValueError(f"Unsupported export format: {fmt}")


def render_tui(results: List[Result]) -> None:
    import curses

    sorted_results = sorted(results, key=lambda item: item.score, reverse=True)
    index = 0

    def draw(stdscr):
        nonlocal index
        curses.curs_set(0)
        while True:
            stdscr.erase()
            height, width = stdscr.getmaxyx()
            header = "Dork Runner (authorized use only) - q to quit"
            stdscr.addstr(0, 0, header[: width - 1])
            list_height = max(3, height // 2)
            for row, result in enumerate(sorted_results[: list_height - 1], start=1):
                prefix = ">" if row - 1 == index else " "
                title = result.title or result.link
                line = f"{prefix} [{result.score:02d}] {title}"
                stdscr.addstr(row, 0, line[: width - 1])

            selected = sorted_results[index] if sorted_results else None
            details_row = list_height + 1
            if selected:
                stdscr.addstr(details_row, 0, f"Dork: {selected.dork}"[: width - 1])
                stdscr.addstr(details_row + 1, 0, f"URL: {selected.link}"[: width - 1])
                snippet_lines = selected.snippet.splitlines() or [""]
                for offset, line in enumerate(snippet_lines[: height - details_row - 3]):
                    stdscr.addstr(details_row + 2 + offset, 0, line[: width - 1])

            stdscr.refresh()
            key = stdscr.getch()
            if key in (ord("q"), ord("Q")):
                break
            if key in (curses.KEY_DOWN, ord("j")):
                index = min(index + 1, max(0, len(sorted_results) - 1))
            if key in (curses.KEY_UP, ord("k")):
                index = max(index - 1, 0)

    curses.wrapper(draw)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run authorized dork searches and rank results."
    )
    parser.add_argument(
        "--dorks-file",
        default="DorkList",
        help="Path to dorks list file (default: DorkList)",
    )
    parser.add_argument(
        "--provider",
        choices=["serpapi", "shodan", "external", "import"],
        default="import",
        help="Result source (default: import).",
    )
    parser.add_argument(
        "--import-results",
        help="Path to JSON results when provider=import",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=10,
        help="Maximum results per dork (serpapi only)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between queries in seconds (serpapi/shodan/external only)",
    )
    parser.add_argument(
        "--serpapi-engine",
        default="google",
        choices=["google", "bing", "duckduckgo", "yahoo", "yandex", "baidu"],
        help="SerpAPI engine (default: google)",
    )
    parser.add_argument(
        "--shodan-page",
        type=int,
        default=1,
        help="Shodan page to fetch (default: 1)",
    )
    parser.add_argument(
        "--external-command",
        help="External command template to run per dork, use {query} placeholder",
    )
    parser.add_argument(
        "--external-parse",
        choices=["json", "jsonl"],
        default="json",
        help="External output parse format (default: json)",
    )
    parser.add_argument(
        "--external-timeout",
        type=int,
        default=60,
        help="Timeout in seconds for external command (default: 60)",
    )
    parser.add_argument(
        "--external-title-field",
        default="title",
        help="Field name for title in external JSON (default: title)",
    )
    parser.add_argument(
        "--external-link-field",
        default="link",
        help="Field name for link in external JSON (default: link)",
    )
    parser.add_argument(
        "--external-snippet-field",
        default="snippet",
        help="Field name for snippet in external JSON (default: snippet)",
    )
    parser.add_argument(
        "--export",
        help="Export results to file (json or csv)",
    )
    parser.add_argument(
        "--export-format",
        choices=["json", "csv"],
        default="json",
        help="Export format (default: json)",
    )
    parser.add_argument(
        "--tui",
        action="store_true",
        help="Show results in a TUI view",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    dorks = load_dorks(args.dorks_file)
    results = gather_results(
        dorks,
        provider=args.provider,
        max_results=args.max_results,
        delay_s=args.delay,
        import_path=args.import_results,
        serpapi_engine=args.serpapi_engine,
        shodan_page=args.shodan_page,
        external_command=args.external_command,
        external_parse=args.external_parse,
        external_timeout=args.external_timeout,
        external_title_field=args.external_title_field,
        external_link_field=args.external_link_field,
        external_snippet_field=args.external_snippet_field,
    )
    if args.export:
        export_results(results, args.export, args.export_format)
    if args.tui:
        render_tui(results)
    if not args.export and not args.tui:
        for result in sorted(results, key=lambda item: item.score, reverse=True):
            print(f"[{result.score:02d}] {result.title} - {result.link}")


if __name__ == "__main__":
    main()
