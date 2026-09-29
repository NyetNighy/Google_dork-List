# Combined Google & Shodan Dork Master List

> **Sources:** NyetNighy's Google_dork-List + OriResearcher OSINT research + 2025/2026 updates  
> **Last updated:** 2026-09-29  
> **Usage:** Replace `target.com` with your target. Use only with explicit permission.  
> **Note:** `port:` and `vuln:` operators are **Shodan/BinaryEdge only** — not valid on Google.

---

## SECTION 1 — Exposed Documents & Files

```
filetype:pdf site:target.com ("confidential" OR "internal use only" OR "not for distribution")
filetype:xlsx OR filetype:xls OR filetype:csv ("password" OR "credentials" OR "api key")
filetype:docx OR filetype:doc intext:"password list" OR "employee list"
filetype:pdf site:target.com ("budget" OR "financial report" OR "invoice")
filetype:log inurl:"error" OR "access" site:target.com
filetype:sql "MySQL dump" AND ("password" OR "CREATE TABLE") site:target.com
filetype:bak OR filetype:old OR filetype:save OR filetype:~ intext:"backup" site:target.com
filetype:txt intext:"ssh private key" OR "BEGIN RSA PRIVATE KEY"
filetype:json intext:"private_key" OR "client_secret" OR "bearer token"
filetype:pdf site:target.com ("password reset" OR "temporary password" OR "one-time password")
filetype:xls OR filetype:xlsx intext:"username" "password" -template -sample
filetype:doc OR filetype:docx intitle:"meeting notes" OR "action items" "confidential"
filetype:csv site:target.com "email" "phone" "address" "employee"
filetype:log "error" "failed login" OR "authentication failure" site:target.com
filetype:txt OR filetype:log intext:"DB_PASSWORD" OR "DATABASE_URL"
filetype:pdf "resume" OR "cv" "@target.com"
filetype:txt "api_key" "secret" site:target.com
```

---

## SECTION 2 — Exposed Directories & Backups

```
intitle:"index of" ("backup" OR ".git" OR ".env" OR "config")
intitle:"index of" ("DCIM" OR ".git" OR "backup" OR "logs" OR "admin" OR "private")
intitle:"index.of" intext:"Apache" "Server at" -inurl:github
inurl:".env" intitle:"index of"
inurl:"/backup/" intitle:"index of"
intitle:"index of" ("/uploads/" OR "/files/" OR "/downloads/" OR "/media/")
intitle:"index of" (".bak" OR ".old" OR ".sql" OR ".zip" OR ".tar.gz")
intitle:"index of" "/wp-content/uploads/" -inurl:wordpress.org
intitle:"index of /" (".ssh" OR "id_rsa" OR "authorized_keys")
intitle:"index of" ("/config/" OR "/settings/" OR "/private/")
intitle:"index of" intext:"Last modified" "parent directory" ("mongodb" OR "mysql")
intitle:"index of" ("/backup/" OR "/backups/" OR "/db_backup/")
intitle:"index of" ("/log/" OR "/logs/" OR "/error_log")
intitle:"index of" ".git" AND ("HEAD" OR "config")
intitle:"index of" ("/.aws/" OR "/.azure/" OR "/.gcp/")
intitle:"index of" (".htpasswd" OR ".htaccess" OR "web.config")
intitle:"index of" ("sitemanager.xml" OR "FileZilla.xml" OR "recentservers.xml")
intitle:"index of" ("index.html.bak" OR "index.php.bak" OR "index.jsp.bak")
intitle:"index.of" (".bash_history" OR ".sh_history")
intitle:"Index of" (passwd OR passwd.bak OR master.passwd)
intitle:"Index of" .mysql_history
intitle:"Index of" (WSFTP.LOG OR access_log OR service.pwd)
intitle:"Index of" (finance.xls OR finances.xls)
intitle:"Index of" robots.txt
intitle:"Index of" mt-db-pass.cgi
intitle:"Index of" ".htpasswd" "htgroup" -intitle:"dist" -apache -htpasswd.c
intitle:"Index of" global.inc
intitle:"Index of" (secpasswd OR secgroup)
intitle:"index of" ("id_rsa" OR "id_ed25519" OR ".pem") -html
intitle:"index of" ("wallet.dat" OR "keystore.jks" OR "keystore.bks")
intitle:"index of" (upload.asp OR upload.aspx)
intitle:"index of" (".svn" OR ".hg")
intitle:"index of" cgiirc.config
intitle:"index of" web.config
```

---

## SECTION 3 — Config Files & Secrets / Credential Leaks

```
ext:env OR ext:yaml OR ext:yml ("DB_PASSWORD" OR "API_KEY" OR "SECRET_KEY")
inurl:config filetype:xml OR filetype:conf OR filetype:ini
intext:"aws_access_key_id" filetype:txt OR filetype:log
intext:"api_key" OR "secret" OR "token" ext:txt OR ext:json -github
ext:sql OR ext:dmp OR ext:dump intext:"password" OR "pwd" OR "pass"
inurl:".git/config" intitle:"index of"
inurl:".DS_Store" intitle:"index of"
inurl:config/database.yml OR inurl:config/app.php intext:"password"
ext:properties OR ext:props intext:"jdbc.password" OR "db.password"
inurl:".bak" ext:env OR ext:ini OR ext:conf ("DB_USER" OR "API_SECRET")
intext:"-----BEGIN PRIVATE KEY-----" filetype:txt OR filetype:pem OR filetype:key
intext:"sk_live_" OR "pk_live_" OR "sk_test_" filetype:txt OR filetype:js site:target.com
inurl:firebase.json OR inurl:".firebaserc" intext:"apiKey"
intext:"MONGO_URI" OR "MONGODB_URI" OR "MONGOLAB_URI" ext:env OR ext:yaml
filetype:env ("AWS_ACCESS_KEY_ID" OR "AWS_SECRET_ACCESS_KEY")
filetype:env ("AZURE_CLIENT_SECRET" OR "azure_client_id")
filetype:env ("GOOGLE_APPLICATION_CREDENTIALS" OR "private_key")
intext:"api_key" OR "apikey" OR "apiSecret" OR "access_token" filetype:env OR filetype:json OR filetype:yml OR filetype:yaml
intext:"BEGIN PRIVATE KEY" filetype:key OR filetype:pem
"api_key" OR "client_secret" filetype:yaml OR filetype:json
intext:"JWT" "token" filetype:log OR filetype:txt site:target.com
inurl:"credentials.json" intitle:"index of"
intext:"x-goog-credential" filetype:json
filetype:ovpn intext:"auth-user-pass" OR "http-proxy"
filetype:rdp intext:"full address" OR "username" OR "password 51:b"
intext:"-----BEGIN RSA PRIVATE KEY-----" filetype:txt OR filetype:pem
inurl:".firebaserc" intext:"apiKey" filetype:json
"AKIA" filetype:env OR filetype:yml OR filetype:json
"ghp_" OR "gho_" OR "github_pat_" filetype:env OR filetype:txt
"xoxb-" OR "xoxp-" OR "xoxa-" filetype:env OR filetype:txt
"sk-" filetype:env OR filetype:json (openai OR anthropic OR "api_key")
"OPENAI_API_KEY" OR "ANTHROPIC_API_KEY" OR "GROQ_API_KEY" filetype:env
"MISTRAL_API_KEY" OR "COHERE_API_KEY" OR "GEMINI_API_KEY" filetype:env
"REPLICATE_API_TOKEN" OR "TOGETHER_API_KEY" OR "HUGGINGFACE_TOKEN" filetype:env
"STRIPE_SECRET_KEY" OR "sk_live_" filetype:env OR filetype:yml
"TWILIO_AUTH_TOKEN" OR "SENDGRID_API_KEY" OR "MAILGUN_API_KEY" filetype:env
"SUPABASE_SERVICE_ROLE" OR "SUPABASE_ANON_KEY" filetype:env
"PLANETSCALE_SERVICE_TOKEN" OR "NEON_API_KEY" filetype:env
"DIGITALOCEAN_TOKEN" OR "HEROKU_API_KEY" OR "VERCEL_TOKEN" filetype:env
"CLOUDFLARE_API_TOKEN" OR "FASTLY_API_KEY" filetype:env
"NPM_TOKEN" OR "//registry.npmjs.org/:_authToken" filetype:npmrc OR filetype:env
"DOCKER_PASSWORD" OR "DOCKER_AUTH_CONFIG" filetype:env OR filetype:yml
"KUBECONFIG" OR "kubernetes" "token" filetype:yml OR filetype:env
```

---

## SECTION 4 — Admin Panels, Login Pages & Dashboards

```
inurl:admin OR inurl:login OR inurl:signin OR inurl:portal site:target.com
intitle:"login" "powered by" (wordpress OR joomla OR drupal OR magento)
inurl:(wp-login.php OR administrator OR admin.php OR login.aspx)
intitle:"remote management" intext:"please enter password"
inurl:(dashboard OR controlpanel OR cp OR panel OR manage) intitle:"login"
inurl:phpmyadmin OR inurl:adminer OR inurl:pma intitle:"phpMyAdmin"
inurl:(webmail OR roundcube OR squirrelmail OR horde) site:target.com
inurl:/admin/console OR inurl:/admin/login OR inurl:/administrator
intitle:"admin login" "powered by" (drupal OR joomla OR vbulletin OR xenforo)
inurl:".php" intitle:"login" intext:"forgot password" OR "remember me"
inurl:/login/index OR inurl:/signin OR inurl:/auth/login
intitle:"Cpanel" OR intitle:"WHM" OR intitle:"Plesk" intext:"login"
inurl:prometheus OR inurl:grafana intitle:"login" OR "sign in"
inurl:/adminer.php OR inurl:/dbadmin OR inurl:/mysqladmin
inurl:/wp-admin OR inurl:/wp-login.php site:target.com
inurl:/administrator intitle:"Joomla"
intitle:"Login" "Webmin"
inurl:"/admin/console" intitle:"Control Panel"
intitle:"Gateway Configuration Menu"
intitle:"Horde :: My Portal" -"[Tickets"
intitle:"Mail Server CMailServer Webmail" "5.2"
intitle:"Remote Desktop Web Connection"
intitle:"Terminal Services Web Connection"
intitle:"admin" intitle:"login"
inurl:main.php phpMyAdmin
inurl:main.php "Welcome to phpMyAdmin"
intitle:"Remote Management" inurl:"login"
intitle:"Web-Based Management" "password"
inurl:manyservers.htm
inurl:"WBEM" compaq login
"All ADMINS Accounts" inurl:admin.php -mysql_fetch_row
"Welcome to Administration" "General" "Local Domains" "SMTP Authentication" inurl:admin
allinurl:intranet admin
intitle:"phpinfo" "PHP Version" inurl:phpinfo.php
intitle:"Jenkins" "login" intext:"Dashboard"
intitle:"SonarQube" inurl:"login"
intitle:"Nexus" inurl:"login"
intitle:"Artifactory" inurl:"login"
inurl:grafana intitle:"login"
inurl:kibana intitle:"login"
intitle:"Portainer" inurl:login
intitle:"Traefik" inurl:dashboard
intitle:"Rancher" inurl:login
intitle:"Argo CD" OR intitle:"ArgoCD" inurl:login
intitle:"Keycloak" inurl:login
intitle:"Authentik" inurl:login
intitle:"Vault" inurl:ui OR inurl:login
```

---

## SECTION 5 — Database & Admin Tool Panels

```
"Welcome to phpMyAdmin" AND "Create new database"
"supplied argument is not a valid MySQL result resource"
"access denied for user" "using password"
"mysql dump" filetype:sql
"phpMyAdmin" "running on" inurl:"main.php"
"Select a database to view" intitle:"FileMaker Pro"
"phpMyAdmin MySQL-Dump" filetype:txt
"phpMyAdmin MySQL-Dump" "INSERT INTO" -"the"
"Dumping data for table"
intitle:phpMyAdmin "Welcome to phpMyAdmin **" "running on * as root@"
"ASP.NET_SessionId" "data source="
filetype:asp + "[ODBC SQL"
"MYSQL error message: supplied argument"
"Snitz! forums db path error"
"SQL syntax error"
"mySQL error with query"
"You have an error in your SQL syntax near"
"Supplied argument is not a valid PostgreSQL result"
intitle:"pgAdmin" "Login"
intitle:phpMyAdmin "Welcome to phpMyAdmin" -intitle:"login"
inurl:/server-status apache intitle:"apache status"
intext:"Elasticsearch" "You Know, for Search"
inurl:"/debug" OR inurl:"/trace" OR inurl:"/console" site:target.com
intitle:"MongoDB" "Compass" OR "Studio 3T"
intitle:"Redis" "Commander" OR "Insight"
intitle:"ClickHouse" "Play" OR "UI"
```

---

## SECTION 6 — Error Pages, Debug Info & Stack Traces

```
"A syntax error has occurred" filetype:ihtml
"An illegal character has been found in the statement"
"Can't connect to local" intitle:warning
"Chatologica MetaSearch" "stack tracking:"
"detected an internal error [IBM][CLI Driver][DB2/6000]"
"Fatal error: Call to undefined function" -reply -the -next
"Incorrect syntax near"
"ORA-00933: SQL command not properly ended"
"PostgreSQL query failed: ERROR: parser: parse error"
"Syntax error in query expression"
"Unclosed quotation mark before the character string"
"Warning: Cannot modify header information – headers already sent"
"Error Diagnostic Information" intitle:"Error Occurred While"
filetype:asp "Custom Error Message" Category Source
intitle:"the page cannot be found" "internet information services"
intitle:"500 Internal Server Error" "server at"
"ORA-00921: unexpected end of SQL command"
"ORA-00936: missing expression"
"Parse error: parse error, unexpected T_VARIABLE" "on line" filetype:php
"The s?ri?t whose uid is" "is not allowed to access"
"There seems to have been a problem with the"
"Unable to jump to row" "on MySQL result index"
"Warning: Bad arguments to (join|implode) () in" "on line"
"Warning: Division by zero in" "on line"
"Warning: mysql_connect(): Access denied for user" "on line"
"Warning: mysql_query()" "invalid query"
"Warning: pg_connect(): Unable to connect to PostgreSQL server: FATAL"
"Warning: Supplied argument is not a valid File-Handle resource"
"Warning: SAFE MODE Restriction in effect"
"SQL Server Driver][SQL Server]Line 1: Incorrect syntax near"
filetype:log "PHP Parse error" OR "PHP Warning" OR "PHP Error"
filetype:php inurl:"logging.php" "Discuz" error
"Internal Server Error" "server at"
"Invision Power Board Database Error"
"ORA-12541: TNS:no listener" intitle:"error occurred"
intitle:"Apache Tomcat" "Error Report"
intitle:"Error Occurred While Processing Request" +WHERE (SELECT OR INSERT) filetype:cfm
"Error using Hypernews" "Server Software"
"Netscape Application Server Error page"
intitle:"Execution of this s?ri?t not permitted"
"error found handling the request" cocoon filetype:xml
"stack trace" "exception" "error" site:target.com
"DEBUG" "TRACE" filetype:log site:target.com
inurl:(phpinfo.php OR test.php OR info.php)
site:target.com "Laravel Debug mode"
inurl:storage/logs intext:"ALLOWED_HOSTS"
intext:"Django" "Debug = True" OR "ALLOWED_HOSTS"
site:target.com "NestJS" "Exception" OR "DEBUG"
site:target.com "FastAPI" "traceback" OR "uvicorn"
```

---

## SECTION 7 — Cloud & DevOps Misconfigs

```
site:s3.amazonaws.com "target" "index of"
site:storage.googleapis.com "target"
site:blob.core.windows.net "target"
site:digitaloceanspaces.com "target"
site:public.blob.core.windows.net "index of"
"Docker" "Docker Remote API"
"Kubernetes" "kube-apiserver"
"Weave Scope" http.favicon.hash:567176827
"Jenkins" "X-Jenkins" http.title:"Dashboard"
inurl:gitlab intitle:"login"
inurl:sonarqube intitle:"SonarQube"
inurl:nexus intitle:"Nexus Repository"
inurl:artifactory intitle:"Artifactory"
site:raw.githubusercontent.com intext:"password" OR intext:"api_key" OR intext:"secret" (filetype:env OR filetype:json OR filetype:yml OR filetype:js)
site:pastebin.com intext:"AWS_SECRET" OR "private_key" OR "password" after:2025-01-01
inurl:"/.git/config" intitle:"index of"
inurl:"/.git/HEAD" intitle:"index of"
inurl:"/.git/" "index of" site:target.com
inurl:".next" intitle:"index of"
inurl:"__nuxt" intitle:"index of"
inurl:"__NEXT_DATA" intitle:"index of"
inurl:".vercel" intitle:"index of"
site:github.com "target.com" "AWS_ACCESS_KEY_ID"
site:github.com "target.com" "MONGO_URI"
inurl:"/jenkins/script" intitle:"script"
inurl:"/console" intitle:"Jenkins"
inurl:"/actuator" intitle:"Spring Boot"
inurl:"/debug" site:target.com
site:*.s3.amazonaws.com "target"
site:*.blob.core.windows.net "target"
inurl:"/.aws/credentials" intitle:"index of"
inurl:"terraform.tfstate" intitle:"index of"
inurl:"pulumi" "stack" intitle:"index of"
```

---

## SECTION 8 — Emails, Contacts & People

```
site:target.com "@target.com" -inurl:(signup OR login OR career)
"email" OR "@target.com" filetype:xls OR filetype:csv OR filetype:txt
site:target.com intext:"@gmail.com" OR "@yahoo.com" intext:"contact"
intext:"@target.com" intitle:"staff" OR "directory" OR "team"
site:target.com intext:"@target.com" filetype:xlsx OR filetype:csv OR filetype:vcf
"@target.com" intitle:"email list" OR "contact list" OR "distribution list"
site:target.com intext:"@target.com" intext:"tel:" OR "phone:" OR "mobile:"
intext:"@target.com" filetype:pdf intitle:"directory" OR "staff directory"
site:target.com "@" -inurl:(login OR signup OR career OR jobs)
intext:"username" "@target.com" filetype:txt OR filetype:log
site:target.com intext:"e-mail" OR "email address" "contact us"
"@target.com" intitle:"resume" OR "cv" OR "curriculum vitae"
intext:"@target.com" inurl:(about OR team OR staff OR employees)
site:target.com filetype:vcard OR filetype:vcf "@target.com"
filetype:xls username password email
site:target.com intext:"@target.com" "mobile" OR "cell" OR "tel"
```

---

## SECTION 9 — Subdomains & Attack Surface

```
site:*.target.com -www -dev -staging -test -beta
site:target.com -inurl:www
site:target.com inurl:(dev OR staging OR test OR uat OR qa OR beta)
site:*.target.com -www -inurl:(blog OR forum OR shop OR store)
site:target-*.* OR site:*.target-*
site:target.com inurl:(api OR api/v1 OR api/v2 OR graphql OR rest)
site:*.target.com inurl:(jenkins OR sonar OR nexus OR artifactory)
site:dev.target.com OR site:staging.target.com OR site:test.target.com
site:target.com inurl:(kibana OR elasticsearch OR logstash)
site:*.target.com intitle:"default web page" OR "under construction"
site:target.com -inurl:www intext:"server" "hostname"
site:internal.target.com OR site:intranet.target.com
site:*.target.com filetype:php intitle:"phpinfo"
site:target.com inurl:(kibana OR grafana OR prometheus)
site:*.target.com inurl:(api OR graphql OR rest OR swagger OR openapi)
site:target.com -inurl:www intext:"hostname" "server"
```

---

## SECTION 10 — Cameras, IoT & Device Panels

```
inurl:(viewerframe?mode=motion OR view/index.shtml OR axis-cgi/mjpg)
intitle:"Live View / — AXIS" OR "webcamXP" OR "D-Link Internet Camera"
inurl:"top.htm" intitle:"BlueNet Video Server"
intitle:"printer status" intext:"HP LaserJet"
intitle:"Web Viewer" intext:"ID" "Password" (axis OR sony OR panasonic)
inurl:"view/viewer_index.shtml" intext:"Live Video"
intitle:"DVR Login" OR intitle:"NVR Login" intext:"Username" "Password"
inurl:"/cgi-bin/guestimage.html" OR inurl:"/cgi-bin/viewer/video.jpg"
intitle:"GoAhead WebServer" intext:"Login" "Camera"
inurl:"onvif/device_service" OR inurl:"onvif/snapshot"
intitle:"Ricoh" "Printer" intext:"Web Image Monitor"
inurl:"port_37777" OR inurl:"port_554" intitle:"RTSP" "stream"
intitle:"Brother" "Web Based Management" intext:"password"
inurl:"/webcam/" OR inurl:"/mjpg/video.mjpg" OR inurl:"/video.cgi"
intitle:"Live View / - AXIS" OR inurl:view/index.shtml
inurl:"CgiStart?page=" OR inurl:"/viewer/live/en/live.html"
inurl:/mjpg/1 OR intitle:"webcam" "live image"
inurl:"MultiCameraFrame?Mode="
"Active Webcam Page" inurl:8080
inurl:yapboz_detay.asp + View Webcam User Accessing
allinurl:control/multiview
inurl:"ViewerFrame?Mode="
intitle:"WJ-NT104 Main Page"
inurl:netw_tcp.shtml
intitle:"supervisioncam protocol"
"Server: yawcam" OR "webcamXP" OR "webcam 7"
"Server: IP Webcam Server" "200 OK"
html:"DVR_H264 ActiveX"
intitle:"Network Camera" (axis OR sony OR panasonic OR hikvision OR dahua)
```

---

## SECTION 11 — Bug Bounty & Program Discovery

```
inurl:(bug bounty OR security OR vulnerability OR "responsible disclosure") site:target.com
intext:"we welcome responsible disclosure" site:*.target.*
"bugcrowd" OR "hackerone" OR "yeswehack" "target.com"
site:target.com "security.txt" OR "/.well-known/security.txt"
inurl:"security" "responsible disclosure" site:target.com
```

---

## SECTION 12 — CMS & Forum Detection

```
inurl:"member.php?u="
inurl:"index.php?showuser="
inurl:"smf/index.php?action=profile;u="
inurl:"index.php?action=profile"
inurl:"profile.php?mode=viewprofile&u="
inurl:"profile.php?id="
"Powered by PunBB"
"Powered by SMF"
"Powered by phpBB"
"Powered by vBulletin"
"Powered by Invision Power Board"
"Powered by XenForo"
"Powered by WordPress" -html filetype:php -demo
```

---

## SECTION 13 — Modern / AI / 2025-2026 Additions

```
# AI / LLM API keys
"OPENAI_API_KEY" OR "sk-proj-" filetype:env OR filetype:yml
"ANTHROPIC_API_KEY" OR "sk-ant-" filetype:env
"GROQ_API_KEY" OR "gsk_" filetype:env
"MISTRAL_API_KEY" OR "COHERE_API_KEY" filetype:env
"GEMINI_API_KEY" OR "GOOGLE_API_KEY" filetype:env
"REPLICATE_API_TOKEN" OR "r8_" filetype:env
"TOGETHER_API_KEY" OR "HUGGINGFACEHUB_API_TOKEN" filetype:env
"PERPLEXITY_API_KEY" OR "pplx-" filetype:env
"FIREWORKS_API_KEY" OR "DEEPINFRA_API_KEY" filetype:env

# Modern cloud / PaaS
"VERCEL_TOKEN" OR "NETLIFY_AUTH_TOKEN" OR "RAILWAY_TOKEN" filetype:env
"RENDER_API_KEY" OR "FLY_API_TOKEN" OR "HEROKU_API_KEY" filetype:env
"SUPABASE_SERVICE_ROLE_KEY" OR "SUPABASE_ANON_KEY" filetype:env
"PLANETSCALE_SERVICE_TOKEN" OR "NEON_API_KEY" OR "COCKROACH_API_KEY" filetype:env
"UPSTASH_REDIS_REST_TOKEN" OR "UPSTASH_VECTOR_REST_TOKEN" filetype:env
"CLOUDFLARE_API_TOKEN" OR "CF_API_TOKEN" filetype:env
"DIGITALOCEAN_ACCESS_TOKEN" OR "DO_TOKEN" filetype:env

# Modern frameworks / observability
inurl:"/actuator/health" OR inurl:"/actuator/env" site:target.com
inurl:"/metrics" OR inurl:"/prometheus" site:target.com
intitle:"Sentry" "DSN" OR "organization"
intitle:"Datadog" OR intitle:"New Relic" inurl:login
intitle:"Grafana" "Explore" OR "Dashboards"
intitle:"Loki" OR intitle:"Tempo" OR intitle:"Jaeger"

# Next.js / modern JS
inurl:"/_next/static" site:target.com
inurl:"__NEXT_DATA__" site:target.com
inurl:".vercel.app" "target"
inurl:"netlify.app" "target"

# Container / K8s modern
intitle:"Portainer" inurl:"#!/auth"
intitle:"Rancher" "Login"
intitle:"Argo CD" "Login"
intitle:"Lens" OR intitle:"k9s"
inurl:"/api/v1/namespaces" OR inurl:"/apis/apps" site:target.com

# Auth / identity modern
intitle:"Keycloak" "Administration Console"
intitle:"Authentik" "Log in"
intitle:"Auth0" "Universal Login"
intitle:"Okta" "Sign In"
intitle:"Clerk" OR intitle:"Supabase Auth"
```

---

## Syntax Reference — Google vs Shodan

| Operator | Google | Shodan | Notes |
|----------|--------|--------|-------|
| `port:` | No | Yes | Shodan primary filter |
| `vuln:CVE-YYYY-XXXX` | No | Yes (paid) | CVE filtering |
| `has_screenshot:true` | No | Yes | Visual recon |
| `http.html:` | No | Yes | HTML body search |
| `http.title:` | No | Yes | Page title search |
| `http.component:` | No | Yes | Technology fingerprint |
| `http.favicon.hash:` | No | Yes | Favicon matching |
| `org:"Org Name"` | No | Yes | Organization filter |
| `country:XX` | No | Yes | ISO 3166 country code |
| `city:"City"` | No | Yes | City name |
| `product:"Name"` | No | Yes | Product/service name |
| `os:"OS"` | No | Yes | Operating system |
| `tag:` | No | Yes | Categorical tags |
| `hostname:` | Partial | Yes | Hostname matching |
| `asn:` | No | Yes | ASN number |

**Google operators:** `site:`, `inurl:`, `intext:`, `filetype:`, `intitle:`, `allinurl:`, `allintitle:`, `cache:`, `related:`, `link:`, `OR`, `AND`, `-`, `"`, `( )`

---

*Updated 2026-09-29 — combined, deduplicated, and extended with modern AI/cloud/framework patterns.*
