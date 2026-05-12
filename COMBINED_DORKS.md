# 🔍 Combined Google & Shodan Dork Master List

> **Sources:** NyetNighy's `Google_dork-List` repo + OriResearcher's ongoing OSINT research  
> **Last updated:** May 12, 2026  
> **Usage:** Replace `target.com` with your target. Use only with permission.  
> **Note:** `port:` and `vuln:` operators are **Shodan/BinaryEdge only** — not valid on Google.

---

## 📂 SECTION 1 — Exposed Documents & Files

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
filetype:log "error" "access denied" site:target.com
filetype:txt "api_key" "secret" site:target.com
```

---

## 📂 SECTION 2 — Exposed Directories & Backups

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
intitle:"Index of" ("passwd" OR "passwd.bak" OR "master.passwd")
intitle:"Index of" ".mysql_history"
intitle:"Index of" ("WSFTP.LOG" OR "access_log" OR "service.pwd")
intitle:"Index of" ("finance.xls" OR "finances.xls")
intitle:"Index of" robots.txt
intitle:"Index of" mt-db-pass.cgi
intitle:"Index of" ".htpasswd" "htgroup" -intitle:"dist" -apache -htpasswd.c
intitle:"Index of" global.inc
intitle:"Index of" ("secpasswd" OR "secgroup")
intitle:"index of" ("id_rsa" OR "id_ed25519" OR ".pem") -html
intitle:"index of" ("wallet.dat" OR "keystore.jks" OR "keystore.bks")
intitle:"index of" ("upload.asp" OR "upload.aspx")
intitle:"index of" (".svn" OR ".hg")
intitle:"index of" cgiirc.config
intitle:"index of" web.config
```

---

## 📂 SECTION 3 — Config Files & Secrets / Credential Leaks

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
```

---

## 📂 SECTION 4 — Admin Panels, Login Pages & Dashboards

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
```

---

## 📂 SECTION 5 — Database & Admin Tool Panels

> **Note:** Shodan uses `port:27017`, `port:6379`, `port:9200` — these are **not valid Google operators**. Use the Google-safe versions below.

```
# ⚠️  PORT: IS SHODAN ONLY — USE GOOGLE-SAFE VERSIONS BELOW
# Google has no port filtering — use site: + targeted intext/intitle combos instead
# For actual port scanning, use Shodan (see bottom of this file)

# Google-safe DB panel queries
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
```

---

## 📂 SECTION 6 — Error Pages, Debug Info & Stack Traces

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
```

---

## 📂 SECTION 7 — Cloud & DevOps Misconfigs

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
```

---

## 📂 SECTION 8 — Emails, Contacts & People

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

## 📂 SECTION 9 — Subdomains & Attack Surface

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

## 📂 SECTION 10 — Cameras, IoT & Device Panels

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

## 📂 SECTION 11 — Bug Bounty & Program Discovery

```
inurl:(bug bounty OR security OR vulnerability OR "responsible disclosure") site:target.com
intext:"we welcome responsible disclosure" site:*.target.*
"bugcrowd" OR "hackerone" OR "yeswehack" "target.com"
site:target.com "security.txt" OR "/.well-known/security.txt"
inurl:"security" "responsible disclosure" site:target.com
```

---

## 📂 SECTION 12 — CMS & Forum Detection

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
"Powered by WordPress" -html filetype:php -demo -wordpress.org
"Powered by Drupal"
"Powered by Joomla"
"Powered by Magento"
"Powered by Sitecore" OR "Powered by Sitefinity"
intext:"powered by vbulletin"
intext:"powered by yabb"
intext:"powered by ip.board"
intext:"powered by phpbb"
inanchor:vbulletin OR inanchor:phpbb OR inanchor:smf
inurl:/forum OR inurl:/forums OR inurl:/community
inurl:newthread.php OR inurl:newreply.php
inurl:register.php OR inurl:login.php
intitle:"osCommerce" inurl:admin filetype:php
intitle:"WordPress >" "Login form" inurl:"wp-login.php"
intitle:"osTicket :: Support Ticket System"
intitle:"Gallery in Configuration mode"
intitle:"Samba Web Administration Tool"
intitle:"Web-Based Configurator"
```

---

## 📂 SECTION 13 — Server Config & Test Pages

```
allinurl:install/install.php
aboutprinter.shtml
intitle:"Apache HTTP Server" intitle:"documentation"
intitle:"Welcome to IIS 4.0?"
intitle:"Test Page for Apache" "It Worked!"
intitle:"Default PLESK Page"
intitle:"Under construction" "does not currently have"
intitle:Configuration.File inurl:softcart.exe
"powered by openbsd" + "powered by apache"
intitle:"the page cannot be found" inetmgr
"seeing this instead" intitle:"test page for apache"
"not for distribution" confidential
"robots.txt" + "Disallow:" filetype:txt
"phpinfo.php" -manual
intitle:"Default" "It works!"
intitle:"Welcome to" "nginx" "server at"
intitle:"Welcome to" "Apache" "server at"
intitle:"cacheserverreport for" "This analysis was produced by calamaris"
intitle:"Ganglia" "Cluster Report for"
intitle:"MRTG/RRD" (inurl:mrtg.cgi OR inurl:14all.cgi OR traffic.cgi)
```

---

## 📂 SECTION 14 — Logs, Tokens & Auth Patterns

```
intext:"Bearer " OR "Authorization: Bearer" filetype:log OR filetype:txt OR filetype:json
intext:"password" OR "passwd" OR "pwd" filetype:log OR filetype:txt OR filetype:sql -intext:"example" -intext:"sample"
intext:"INSERT INTO users" OR "INSERT INTO `users`" filetype:sql
intext:"Laravel" "session" filetype:log
intext:"debug" "trace" filetype:log site:target.com
intext:"AWS_ACCESS_KEY" filetype:log
intext:"ERROR" "MySQL" filetype:log
intext:"token" "jwt" filetype:log
intext:"sk_live_" filetype:log OR filetype:txt
intext:"ghp_" OR "github_pat_" filetype:log OR filetype:txt
```

---

## 📂 SECTION 15 — Quick Recon Combos

```
# Replace target.com with your target
site:target.com (ext:xml OR ext:conf OR ext:cnf OR ext:reg OR ext:inf OR ext:rdp OR ext:cfg OR ext:txt OR ext:ora OR ext:inc)
site:target.com (inurl:admin OR inurl:login OR intitle:admin)
intitle:"index of" site:target.com (backup OR .git OR .svn OR .env OR logs)
site:target.com (filetype:sql OR filetype:bak OR filetype:old OR filetype:~) ("password" OR "credential" OR "key")
site:target.com intitle:"index of" ("/admin/" OR "/config/" OR "/uploads/" OR "/private/" OR "/secure/")
site:target.com (inurl:login OR inurl:admin OR inurl:dashboard) (intitle:login OR intitle:admin OR intitle:dashboard)
site:target.com (ext:env OR ext:yml OR ext:yaml OR ext:json) ("secret" OR "key" OR "token" OR "password")
site:target.com (inurl:wp-admin OR inurl:wp-login OR inurl:xmlrpc.php) -inurl:wordpress.com
site:target.com (filetype:pdf OR filetype:docx OR filetype:xlsx) ("confidential" OR "internal" OR "proprietary")
site:target.com (inurl:api OR inurl:graphql OR inurl:rest OR inurl:v1 OR inurl:v2) (intitle:"api" OR intext:"swagger")
site:target.com (intitle:"phpinfo" OR inurl:phpinfo.php OR inurl:test.php OR inurl:info.php)
site:target.com (inurl:jenkins OR inurl:sonarqube OR inurl:nexus OR inurl:artifactory OR inurl:gitlab)
site:target.com (filetype:txt OR filetype:log OR filetype:csv) ("email" OR "@target.com" OR "username" OR "password")
site:target.com (inurl:api OR inurl:graphql OR inurl:rest) (inurl:swagger OR intext:"openapi")
site:target.com (inurl:.git OR inurl:.svn OR inurl:.hg) intitle:"index of"
site:target.com (inurl:phpmyadmin OR inurl:adminer OR inurl:pma)
site:target.com (inurl:env OR inurl:.env) filetype:env
```

---

## 📂 SECTION 16 — Modern Framework & Dev Tool Exposures

```
# Laravel
site:target.com "Laravel Debug mode"
inurl:storage/logs intext:"ALLOWED_HOSTS"
inurl:"/debug" OR inurl:"/trace" OR inurl:"/console"
filetype:env intext:"APP_KEY" OR "DB_PASSWORD"

# Next.js / React SSR
inurl:".next" intitle:"index of"
inurl:"__nuxt" intitle:"index of"
inurl:"__NEXT_DATA" intitle:"index of"
inurl:".vercel" intitle:"index of"

# Spring Boot
inurl:"/actuator" intitle:"Spring Boot"
inurl:"/health" OR inurl:"/info"
intext:"Whitelabel Error Page" "Spring Boot"

# Symfony
intext:"symfony" "prod" debug
inurl:"/console" intitle:"Symfony"

# WordPress
inurl:"wp-config.php" intitle:"index of"
inurl:"wp-json" site:target.com
inurl:"xmlrpc.php" site:target.com

# Drupal
inurl:"/node/1" intitle:"Drupal"
inurl:"/user/login" intitle:"Drupal"

# GitLab CI/CD
inurl:".gitlab-ci.yml" intitle:"index of"
inurl:"/-ci" intitle:"GitLab"
```

---

## 🔎 SHODAN DORKS — port:, vuln:, has_screenshot:, http., etc.

> **⚠️  These operators are SHODAN ONLY. They do NOT work on Google.**
> Use at [shodan.io](https://shodan.io). Free tier limited (page 2 max, `vuln:` requires paid plan).

```
# Basic / Common Filters
port:80,443,8080                  # Common web ports (HTTP/HTTPS)
product:Apache                   # Apache web servers
http.title:"Index of /"          # Open directory listings
has_screenshot:true              # Devices with visual recon (Shodan visual screenshot)
org:"Amazon.com"                 # Devices in a specific organization
country:GB                       # UK targets (2-letter ISO code)
city:"Southend-on-Sea"           # Very local recon

# Web / HTTP Fingerprinting
http.component:"wordpress"       # Sites using WordPress
http.html:"wp-config.php"        # Potential WP config exposure
http.title:"phpMyAdmin"          # Exposed phpMyAdmin panels
http.favicon.hash:81586312       # Common default CMS favicon hashes
x-powered-by:"PHP/5"             # Old/outdated PHP versions (vulnerable)
http.component:"nginx"
http.component:"jquery"          # jQuery version detection
http.headers:"X-Jenkins"         # Jenkins installs

# Vulnerable Services & CVEs
# ⚠️  Replace CVE-YYYY-XXXX with actual CVE numbers
# ⚠️  vuln: requires paid plan — free tier cannot filter by CVE
vuln:CVE-2021-44228              # Log4Shell (still lingers in legacy Java)
vuln:CVE-2019-19781              # Citrix ADC/Gateway RCE
vuln:CVE-2014-0160               # Heartbleed (surprisingly persistent)
vuln:CVE-2021-45046              # Log4j DoS variant
vuln:CVE-2023-44487              # HTTP/2 Rapid Reset (DDoS)
# Add current CVEs as discovered — check cve.mitre.org for latest

# Database & NoSQL (port-based — Shodan-specific)
"MongoDB" "authentication disabled" port:27017
"redis" port:6379
"Memcached" port:11211
"elastic" port:9200
"phpMyAdmin" port:80,443
"MySQL" port:3306
"PostgreSQL" port:5432
"MSSQL" port:1433

# SSH / Remote Access
"SSH-2.0-OpenSSH" "root"         # Root login SSH (dangerous)
"authentication disabled" "RFB 003.008"  # Unauthenticated VNC
"HP-ILO" OR "iLO" port:443        # HP iLO management interfaces
"Android Debug Bridge" port:5555  # Exposed ADB (Android root bridge)
port:23 "root@" -login -password  # Open Telnet with root prompt
"Intel(R) Active Management Technology" port:16992,16993  # Intel AMT (often vuln)

# IoT / Cameras / Devices
port:554 has_screenshot:true     # RTSP cameras with visual screenshot
"webcam" OR "DVR" OR "camera" port:80,81,8080
"NETGEAR" OR "Linksys" "admin"
tag:ics                           # Industrial Control Systems (ML-tagged)
"screenshot.label:ics"            # ICS screenshots via ML
"Server: yawcam" OR "webcamXP" OR "webcam 7"
"Server: IP Webcam Server" "200 OK"
html:"DVR_H264 ActiveX"           # Chinese DVRs (ActiveX vuln-prone)
"Chromecast:" port:8008           # Google Chromecast control port

# Cloud & Container Exposures
"Amazon AWS" port:9200            # Exposed Elasticsearch on AWS
"Docker" port:2375 "Docker Remote API"  # Unprotected Docker daemon
"Kubernetes" port:6443 "kube-apiserver"  # Exposed K8s API server
"Weave Scope" http.favicon.hash:567176827  # Weave dashboard (often unauth)
"Jenkins" "X-Jenkins" http.title:"Dashboard"  # Exposed Jenkins console
"X-Plex-Protocol" port:32400       # Plex media servers

# Ransomware Indicators
"encrypted attention" has_screenshot:true  # Ransomware lock screens (OCR'd)
"your files are encrypted"     # Common ransom note text in banners

# Fun / Legacy / Deprecated
port:17                         # Quote of the Day service (ancient RFC 865)
"HP-UX" OR "Windows 2000"       # Prehistoric OS still online
"printer" "ready"               # Exposed printers (print fun messages?)

# Advanced Combos (Shodan-only)
country:GB port:80,443 has_screenshot:true  # UK web servers with screenshots
has_screenshot:true "default password" OR "admin:admin"  # Devices with creds visible
org:"your-company" -port:443     # Non-HTTPS exposures for your org
has_screenshot:true tag:iot "password"  # IoT devices with screenshots + password hints

# ICS / SCADA (critical infrastructure)
tag:ics OR tag:scada            # ML-tagged industrial systems
"Siemens, SIMATIC" port:161     # Siemens PLCs via SNMP
"Server: CarelDataServer" "200 Document follows"  # Carel refrigeration controllers
"HID VertX" port:4070           # Access control panels
"smart install client active"    # Cisco Smart Install (RCE risk, deprecated but still shows)
"voter system serial" country:US  # Voting machine exposures (disturbing)
```

---

## ⚠️  Syntax Reference — Google vs Shodan

| Operator | Google | Shodan | Notes |
|----------|--------|--------|-------|
| `port:` | ❌ NO | ✅ YES | Shodan primary filter |
| `vuln:CVE-YYYY-XXXX` | ❌ NO | ✅ YES (paid) | CVE filtering |
| `has_screenshot:true` | ❌ NO | ✅ YES | Visual recon |
| `http.html:` | ❌ NO | ✅ YES | HTML body search |
| `http.title:` | ❌ NO | ✅ YES | Page title search |
| `http.component:` | ❌ NO | ✅ YES | Technology fingerprint |
| `http.favicon.hash:` | ❌ NO | ✅ YES | Favicon matching |
| `org:"Org Name"` | ❌ NO | ✅ YES | Organization filter |
| `country:XX` | ❌ NO | ✅ YES | ISO 3166 country code |
| `city:"City"` | ❌ NO | ✅ YES | City name |
| `product:"Name"` | ❌ NO | ✅ YES | Product/service name |
| `os:"OS"` | ❌ NO | ✅ YES | Operating system |
| `tag:` | ❌ NO | ✅ YES | Categorical tags |
| `hostname:` | ⚠️ Partial | ✅ YES | Hostname matching |
| `asn:` | ❌ NO | ✅ YES | ASN number |

**Google:** `site:`, `inurl:`, `intext:`, `filetype:`, `intitle:`, `intitle:`, `allinurl:`, `allintitle:`, `cache:`, `related:`, `link:`, `OR`, `AND`, `-`, `"`, `(` `)`

---

*Compiled by OriResearcher 🔍 from NyetNighy's Google_dork-List + ongoing OSINT research*