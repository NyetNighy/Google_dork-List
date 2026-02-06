# ⚠️ IMPORTANT DISCLAIMER & LEGAL NOTICE ⚠️

**This repository is provided strictly for EDUCATIONAL and ETHICAL SECURITY RESEARCH purposes only.**

The search queries / dorks / advanced operators shared here (originally inspired by Google Hacking Database techniques and extended to other engines) are intended to help security researchers, penetration testers, bug bounty hunters, red teamers, and website/asset owners identify publicly exposed information, misconfigurations, or unintended data exposure **only on systems they own or have explicit written permission to test**.

**You MUST obtain explicit permission** (preferably in writing, such as through a bug bounty program scope, vulnerability disclosure policy, or signed engagement letter) **before running ANY of these queries against any target, system, domain, IP range, organization, or asset that is not your own property**.

### Scope of Application
These queries may be used (with permission) on:
- General web search engines: Google, Bing, DuckDuckGo, Yahoo, Yandex, Baidu, Brave Search, Ecosia, Qwant, and similar services
- Specialized device / cyberspace / IoT / vulnerability search engines: Shodan, Censys, ZoomEye, FOFA, BinaryEdge, Netlas, Onyphe, and equivalents

Different engines support different syntaxes and operators — always verify the supported syntax for each platform before use (many operators overlap but results, indexing depth, and filtering behavior vary significantly).

### Prohibited Uses
- Do **NOT** use these dorks/operators for unauthorized access, reconnaissance without consent, data theft, scraping personal or sensitive information, harassment, extortion, competitive intelligence gathering without authorization, doxxing, or any other illegal or unethical activity.
- Do **NOT** use them to violate privacy, collect personal data at scale, profile individuals, exploit vulnerabilities without following responsible disclosure practices, or chain them with automated tools for mass-scanning without permission.
- Do **NOT** attempt credential stuffing, brute-forcing, or any form of attack based on information discovered via these techniques.

Misuse of these techniques may violate laws including (but not limited to):
- Computer Fraud and Abuse Act (CFAA) in the US
- Computer Misuse Act 1990 in the UK
- General Data Protection Regulation (GDPR) in the EU
- Data Protection Act / equivalent privacy laws in other jurisdictions
- National cybersecurity / hacking / unauthorized access legislation worldwide

### No Liability
**The author(s) of this repository and any contributors are NOT responsible or liable** for any misuse, damage, legal consequences, civil claims, criminal charges, account bans, or other harm resulting from the use (or misuse) of these queries, operators, or techniques — whether on permitted or non-permitted targets.

By accessing, downloading, cloning, forking, starring, watching, or using any content from this repository, **you agree** that:
- You will use it only in an ethical, legal, and authorized manner.
- You assume full responsibility and liability for your actions.
- You will comply with all applicable local, national, and international laws.
- You will obtain proper written authorization before testing or querying any non-owned systems, domains, IPs, organizations, or assets.
- You understand that different search engines may log queries, block accounts, or report suspicious activity.

If you discover a vulnerability, exposed data, misconfiguration, or security issue using these or similar techniques, **report it responsibly** to the affected party following their coordinated vulnerability disclosure policy or bug bounty program rules — **never exploit, exfiltrate, publicize, sell, or otherwise misuse the finding without explicit permission**.

Stay ethical. Hunt bugs responsibly. Secure the web (and the things connected to it).

Last updated: January 2026

---

## Dork Runner (authorized use only)

This repo now includes a small helper script, `dork_runner.py`, that can:

- Load the dork list from `DorkList`
- Ingest search results from an **authorized** source
- Rank results using a simple keyword-based score
- Export JSON/CSV or display a TUI view

**Do not use this script against targets you do not own or have explicit written permission to test.**

### Quick start (imported results)

1. Save authorized search results to JSON (list of objects with `title`, `link`, `snippet`, and optional `dork`).
2. Run the script using the import provider (from the repo root, or pass `--dorks-file` with a full path):

```bash
python3 dork_runner.py --provider import --import-results results.json --export findings.json
```

To open a TUI view instead:

```bash
python3 dork_runner.py --provider import --import-results results.json --tui
```

### Optional: SerpAPI provider (search engines via API)

If you have a SerpAPI key and permission to run these queries, you can use:

```bash
export SERPAPI_API_KEY=\"your_key_here\"
python3 dork_runner.py --provider serpapi --max-results 5 --delay 1.5 --export findings.json
```

You can also select other supported engines via SerpAPI:

```bash
export SERPAPI_API_KEY=\"your_key_here\"
python3 dork_runner.py --provider serpapi --serpapi-engine bing --max-results 5 --delay 1.5 --export findings.json
```

This uses SerpAPI rather than direct scraping. Ensure you comply with SerpAPI and search-engine terms and your engagement rules.

### Optional: Shodan provider (internet-facing services)

If you have a Shodan API key and permission to run these queries, you can use:

```bash
export SHODAN_API_KEY=\"your_key_here\"
python3 dork_runner.py --provider shodan --shodan-page 1 --delay 1.5 --export findings.json
```

Shodan results are mapped to host pages on shodan.io. Ensure you comply with Shodan terms and your engagement rules.

### Optional: External tool provider (Kali tools)

If you want to use other tools available on Kali, you can run them per-dork and parse their JSON output.
The external command must print JSON (an array of objects) to stdout, and you can map fields to `title`,
`link`, and `snippet`:

```bash
python3 dork_runner.py --provider external \
  --external-command "some-tool --query {query} --json" \
  --external-title-field title \
  --external-link-field link \
  --external-snippet-field snippet \
  --export findings.json
```

For tools that emit JSON Lines, use:

```bash
python3 dork_runner.py --provider external \
  --external-command "some-tool --query {query} --jsonl" \
  --external-parse jsonl \
  --export findings.json
```

Ensure you have explicit authorization and follow the tool and platform terms for any data sources used.
