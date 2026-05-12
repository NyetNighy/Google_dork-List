# 🔍 Combined Google & Shodan Dork Master List

> **Sources:** NyetNighy's `Google_dork-List` repo + OriResearcher's ongoing OSINT research  
> **Last updated:** May 12, 2026  
> **Usage:** Replace `target.com` with your target. Use only with permission.

---

## 📂 SECTION 1 — Exposed Documents & Files

```
filetype:pdf site:target.com "confidential" | "internal use only" | "not for distribution"
filetype:xlsx | filetype:xls | filetype:csv "password" | "credentials" | "api key"
filetype:docx | filetype:doc intext:"password list" | "employee list"
filetype:pdf site:target.com "budget" | "financial report" | "invoice"
filetype:log inurl:"error" | "access" site:target.com
filetype:sql "MySQL dump" "password" OR "CREATE TABLE" site:target.com
filetype:bak | filetype:old | filetype:save | filetype:~ intext:"backup" site:target.com
filetype:txt intext:"ssh private key" OR "BEGIN RSA PRIVATE KEY"
filetype:json intext:"private_key" | "client_secret" | "bearer token"
filetype:pdf site:target.com "password reset" | "temporary password" | "one-time password"
filetype:xls | filetype:xlsx intext:"username" "password" -template -sample
filetype:doc | filetype:docx intitle:"meeting notes" | "action items" "confidential"
filetype:csv site:target.com "email" "phone" "address" "employee"
filetype:log "error" "failed login" | "authentication failure" site:target.com
filetype:txt | filetype:log intext:"DB_PASSWORD" OR "DATABASE_URL"
filetype:pdf "resume" | "cv" "@target.com"
filetype:xlsx "site:target.com" "username" "password"
filetype:log "error" "access denied" site:target.com
filetype:txt "api_key" "secret" site:target.com
```

---

## 📂 SECTION 2 — Exposed Directories & Backups

```
intitle:"index of" "parent directory" (backup | .git | .env | config)
intitle:"index of" "DCIM" | ".git" | "backup" | "logs" | "admin" | "private"
intitle:"index.of" intext:"Apache" "Server at" -inurl:github
inurl:".env" intitle:"index of"
inurl:"/backup/" intitle:"index of"
intitle:"index of" "/uploads/" | "/files/" | "/downloads/" | "/media/"
intitle:"index of" ".bak" | ".old" | ".sql" | ".zip" | ".tar.gz"
intitle:"index of" "/wp-content/uploads/" -inurl:wordpress.org
intitle:"index of /" ".ssh" | "id_rsa" | "authorized_keys"
intitle:"index of" "/config/" | "/settings/" | "/private/"
intitle:"index of" intext:"Last modified" "parent directory" "mongodb" | "mysql"
intitle:"index of" "/backup/" | "/backups/" | "/db_backup/"
intitle:"index of" "/log/" | "/logs/" | "/error_log"
intitle:"index of" ".git" "HEAD" OR "config"
intitle:"index of" "/.aws/" | "/.azure/" | "/.gcp/"
intitle:"index of" ".htpasswd" | ".htaccess" | "web.config"
intitle:"index of" "sitemanager.xml" | "FileZilla.xml" | "recentservers.xml"
intitle:"index of" "index.html.bak" | "index.php.bak" | "index.jsp.bak"
intitle:"index.of" ".bash_history" | ".sh_history"
intitle:"Index of" "passwd" | "passwd.bak" | "master.passwd"
intitle:"Index of" ".mysql_history"
intitle:"Index of" "WSFTP.LOG" | "access_log" | "service.pwd"
intitle:"Index of" "finance.xls" | "finances.xls"
intitle:"Index of" "robots.txt"
intitle:"Index of" "mt-db-pass.cgi"
intitle:"Index of" ".htpasswd" "htgroup" -intitle:"dist" -apache -htpasswd.c
intitle:"Index of" "global.inc"
intitle:"Index of" "secpasswd" | "secgroup"
intitle:"index of" "id_rsa" | "id_ed25519" | ".pem" -html
intitle:"index of" "wallet.dat" | "keystore.jks" | "keystore.bks"
intitle:"index of" "upload.asp" | "upload.aspx"
intitle:"index of" ".svn" | ".hg"
intitle:"index of" "cgiirc.config"
intitle:"index of" "web.config"
```

---

## 📂 SECTION 3 — Config Files & Secrets / Credential Leaks

```
ext:env | ext:yaml | ext:yml "DB_PASSWORD" | "API_KEY" | "SECRET_KEY"
inurl:config filetype:xml | filetype:conf | filetype:ini
intext:"aws_access_key_id" filetype:txt | filetype:log
intext:"api_key" | "secret" | "token" ext:txt | ext:json -github
ext:sql | ext:dmp | ext:dump intext:"password" | "pwd" | "pass"
inurl:".git/config" intitle:"index of"
inurl:".DS_Store" intitle:"index of"
inurl:config/database.yml | inurl:config/app.php intext:"password"
ext:properties | ext:props intext:"jdbc.password" | "db.password"
inurl:".bak" ext:env | ext:ini | ext:conf "DB_USER" OR "API_SECRET"
intext:"-----BEGIN PRIVATE KEY-----" filetype:txt | filetype:pem | filetype:key
intext:"sk_live_" | "pk_live_" OR "sk_test_" filetype:txt | filetype:js site:target.com
inurl:firebase.json | inurl:".firebaserc" intext:"apiKey"
intext:"MONGO_URI" | "MONGODB_URI" OR "MONGOLAB_URI" ext:env | ext:yaml
filetype:env "AWS_ACCESS_KEY_ID" OR "AWS_SECRET_ACCESS_KEY"
filetype:env "AZURE_CLIENT_SECRET" OR "azure_client_id"
filetype:env "GOOGLE_APPLICATION_CREDENTIALS" OR "private_key"
intext:"api_key" OR "apikey" OR "apiSecret" OR "access_token" filetype:env OR filetype:json OR filetype:yml OR filetype:yaml
intext:"BEGIN PRIVATE KEY" filetype:key | filetype:pem
"api_key" | "client_secret" filetype:yaml | filetype:json
intext:"JWT" "token" filetype:log | filetype:txt site:target.com
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
inurl:admin | inurl:login | inurl:signin | inurl:portal site:target.com
intitle:"login" "powered by" (wordpress | joomla | drupal | magento)
inurl:(wp-login.php | administrator | admin.php | login.aspx)
intitle:"remote management" intext:"please enter password"
inurl:(dashboard | controlpanel | cp | panel | manage) intitle:"login"
inurl:phpmyadmin | inurl:adminer | inurl:pma intitle:"phpMyAdmin"
inurl:(webmail | roundcube | squirrelmail | horde) site:target.com
inurl:/admin/console | inurl:/admin/login | inurl:/administrator
intitle:"admin login" "powered by" (drupal | joomla | vbulletin | xenforo)
inurl:".php" intitle:"login" intext:"forgot password" | "remember me"
inurl:/login/index | inurl:/signin | inurl:/auth/login
intitle:"Cpanel" | intitle:"WHM" | intitle:"Plesk" intext:"login"
inurl:prometheus | inurl:grafana intitle:"login" | "sign in"
inurl:/adminer.php | inurl:/dbadmin | inurl:/mysqladmin
inurl:/wp-admin | inurl:/wp-login.php site:target.com
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
MYSQL error message: supplied argument
Snitz! forums db path error
SQL syntax error
"mySQL error with query"
"You have an error in your SQL syntax near"
"Supplied argument is not a valid PostgreSQL result"
intitle:"Mongo Express" "Login"
intitle:"Redis" "INFO" port:6379
"Set-Cookie: mongo-express=" "200 OK" port:27017
"redis" port:6379 "Authentication required" -password
"elastic" port:9200 "_cat/indices"
"MongoDB" "authentication disabled" port:27017
intitle:"pgAdmin" "Login"
intitle:"phpMyAdmin" "Welcome to phpMyAdmin" -intitle:"login"
inurl:/server-status apache intitle:"apache status"
intext:"Elasticsearch" "You Know, for Search"
inurl:"/debug" | inurl:"/trace" | inurl:"/console" site:target.com
inurl:server-status intitle:"Apache Status"
inurl:device-status "MongoDB"
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
"PostgreSQL query failed:  ERROR:  parser: parse error"
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
filetype:log "PHP Parse error" | "PHP Warning" | "PHP Error"
filetype:php inurl:"logging.php" "Discuz" error
"Internal Server Error" "server at"
"Invision Power Board Database Error"
"ORA-12541: TNS:no listener" intitle:"error occurred"
"Apache Tomcat" "Error Report"
intitle:"Error Occurred While Processing Request" +WHERE (SELECT|INSERT) filetype:cfm
"Error using Hypernews" "Server Software"
"Netscape Application Server Error page"
intitle:"Execution of this s?ri?t not permitted"
"error found handling the request" cocoon filetype:xml
"stack trace" "exception" "error" site:target.com
"DEBUG" "TRACE" filetype:log site:target.com
inurl:(phpinfo.php | test.php | info.php)
site:target.com "Laravel Debug mode"
inurl:storage/logs intext:"ALLOWED_HOSTS"
intext:"Django" "Debug = True" | "ALLOWED_HOSTS"
```

---

## 📂 SECTION 7 — Cloud & DevOps Misconfigs

```
site:s3.amazonaws.com "target" "index of"
site:storage.googleapis.com "target"
site:blob.core.windows.net "target"
site:digitaloceanspaces.com "target"
site:public.blob.core.windows.net "index of"
"Docker" port:2375 "Docker Remote API"
"Kubernetes" port:6443 "kube-apiserver"
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
inurl:".next" intitle:"index of" (Next.js builds)
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
site:target.com "@target.com" -inurl:(signup | login | career)
"email" OR "@target.com" filetype:xls | filetype:csv | filetype:txt
site:target.com intext:"@gmail.com" "@yahoo.com" intext:"contact"
intext:"@target.com" intitle:"staff" | "directory" | "team"
site:target.com intext:"@target.com" filetype:xlsx | filetype:csv | filetype:vcf
"@target.com" intitle:"email list" | "contact list" | "distribution list"
site:target.com intext:"@target.com" intext:"tel:" | "phone:" | "mobile:"
intext:"@target.com" filetype:pdf intitle:"directory" | "staff directory"
site:target.com "@" -inurl:(login | signup | career | jobs)
intext:"username" "@target.com" filetype:txt | filetype:log
site:target.com intext:"e-mail" | "email address" "contact us"
"@target.com" intitle:"resume" | "cv" | "curriculum vitae"
intext:"@target.com" inurl:(about | team | staff | employees)
site:target.com filetype:vcard | filetype:vcf "@target.com"
filetype:xls username password email
site:target.com intext:"@target.com" "mobile" | "cell" | "tel"
```

---

## 📂 SECTION 9 — Subdomains & Attack Surface

```
site:*.target.com -www -dev -staging -test -beta
site:target.com -inurl:www
site:target.com inurl:(dev | staging | test | uat | qa | beta)
site:*.target.com -www -inurl:(blog | forum | shop | store)
site:target-*.* | site:*.target-*
site:target.com inurl:(api | api/v1 | api/v2 | graphql | rest)
site:*.target.com inurl:(jenkins | sonar | nexus | artifactory)
site:dev.target.com | site:staging.target.com | site:test.target.com
site:target.com inurl:(kibana | elasticsearch | logstash)
site:*.target.com intitle:"default web page" | "under construction"
site:target.com -inurl:www intext:"server" "hostname"
site:internal.target.com | site:intranet.target.com
site:*.target.com filetype:php intitle:"phpinfo"
site:target.com inurl:(kibana | grafana | prometheus)
site:*.target.com inurl:(api | graphql | rest | swagger | openapi)
site:target.com -inurl:www intext:"hostname" "server"
```

---

## 📂 SECTION 10 — Cameras, IoT & Device Panels

```
inurl:(viewerframe?mode=motion | view/index.shtml | axis-cgi/mjpg)
intitle:"Live View / — AXIS" | "webcamXP" | "D-Link Internet Camera"
inurl:"top.htm" intitle:"BlueNet Video Server"
intitle:"printer status" intext:"HP LaserJet"
intitle:"Web Viewer" intext:"ID" "Password" (axis | sony | panasonic)
inurl:"view/viewer_index.shtml" intext:"Live Video"
intitle:"DVR Login" | intitle:"NVR Login" intext:"Username" "Password"
inurl:"/cgi-bin/guestimage.html" | inurl:"/cgi-bin/viewer/video.jpg"
intitle:"GoAhead WebServer" intext:"Login" "Camera"
inurl:"onvif/device_service" | inurl:"onvif/snapshot"
intitle:"Ricoh" "Printer" intext:"Web Image Monitor"
inurl:"port_37777" | inurl:"port_554" intitle:"RTSP" "stream"
intitle:"Brother" "Web Based Management" intext:"password"
inurl:"/webcam/" | inurl:"/mjpg/video.mjpg" | inurl:"/video.cgi"
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
intitle:"Network Camera" port:80,81,8080
"Chromecast:" port:8008
"Intel(R) Active Management Technology" port:16992,16993
"HP-ILO" OR "iLO" port:443
"Android Debug Bridge" port:5555
port:554 has_screenshot:true
```

---

## 📂 SECTION 11 — Bug Bounty & Program Discovery

```
inurl:(bug bounty | security | vulnerability | responsible disclosure) site:target.com
intext:"we welcome responsible disclosure" site:*.target.*
"bugcrowd" | "hackerone" | "yeswehack" "target.com"
site:target.com "security.txt" | "/.well-known/security.txt"
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
"Powered by Sitecore" | "Powered by Sitefinity"
intext:"powered by vbulletin"
intext:"powered by yabb"
intext:"powered by ip.board"
intext:"powered by phpbb"
inanchor:vbulletin | inanchor:phpbb | inanchor:smf
inurl:/forum | inurl:/forums | inurl:/community
inurl:newthread.php | inurl:newreply.php
inurl:register.php | inurl:login.php
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
"powered by openbsd" +"powered by apache"
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
intitle:"MRTG/RRD" inurl:mrtg.cgi | inurl:14all.cgi | traffic.cgi
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
intext:"sk_live_" filetype:log | filetype:txt
intext:"ghp_" | "github_pat_" filetype:log | filetype:txt
```

---

## 📂 SECTION 15 — Quick Recon Combos

```
# Replace target.com with your target
site:target.com (ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:inc)
site:target.com (inurl:admin | inurl:login | intitle:admin)
intitle:"index of" site:target.com (backup | .git | .svn | .env | logs)
site:target.com (filetype:sql | filetype:bak | filetype:old | filetype:~) ("password" OR "credential" OR "key")
site:target.com intitle:"index of" ("/admin/" | "/config/" | "/uploads/" | "/private/" | "/secure/")
site:target.com (inurl:login | inurl:admin | inurl:dashboard) (intitle:login | intitle:admin | intitle:dashboard)
site:target.com (ext:env | ext:yml | ext:yaml | ext:json) ("secret" OR "key" OR "token" OR "password")
site:target.com (inurl:wp-admin | inurl:wp-login | inurl:xmlrpc.php) -inurl:wordpress.com
site:target.com (filetype:pdf | filetype:docx | filetype:xlsx) ("confidential" OR "internal" OR "proprietary")
site:target.com (inurl:api | inurl:graphql | inurl:rest | inurl:v1 | inurl:v2) (intitle:"api" OR intext:"swagger")
site:target.com (intitle:"phpinfo" OR inurl:phpinfo.php OR inurl:test.php OR inurl:info.php)
site:target.com (inurl:jenkins | inurl:sonarqube | inurl:nexus | inurl:artifactory | inurl:gitlab)
site:target.com (filetype:txt | filetype:log | filetype:csv) ("email" OR "@target.com" OR "username" OR "password")
site:target.com (inurl:api | inurl:graphql | inurl:rest) (inurl:swagger | intext:"openapi")
site:target.com (inurl:.git | inurl:.svn | inurl:.hg) intitle:"index of"
site:target.com (inurl:phpmyadmin | inurl:adminer | inurl:pma)
site:target.com (inurl:env | inurl:.env) filetype:env
```

---

## 📂 SECTION 16 — Modern Framework & Dev Tool Exposures

```
# Laravel
site:target.com "Laravel Debug mode"
inurl:storage/logs intext:"ALLOWED_HOSTS"
inurl:"/debug" | inurl:"/trace" | inurl:"/console"
filetype:env intext:"APP_KEY" | "DB_PASSWORD"

# Next.js / React SSR
inurl:".next" intitle:"index of"
inurl:"__nuxt" intitle:"index of"
inurl:"__NEXT_DATA" intitle:"index of"
inurl:".vercel" intitle:"index of"

# Spring Boot
inurl:"/actuator" intitle:"Spring Boot"
inurl:"/health" | inurl:"/info"
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

## 🔎 SHODAN DORKS (Separate Engine — Not Google)

> Use at [shodan.io](https://shodan.io). Free tier has limitations (page 2 max, vuln: requires paid plan).

```
# Basic / Common
port:80,443,8080                  # Common web ports
product:Apache                     # Apache web servers
http.title:"Index of /"            # Open directory listings
has_screenshot:true                # Devices with visual recon
org:"Amazon.com"                   # Specific organization
country:GB                         # UK targets
city:"Southend-on-Sea"             # Very local recon

# Web / HTTP
http.component:"wordpress"         # WordPress sites
http.html:"wp-config.php"          # WP config exposes
"http.title:\"phpMyAdmin\""        # Exposed phpMyAdmin
http.favicon.hash:81586312         # Common default CMS favicon
x-powered-by:"PHP/5"               # Old PHP (vuln-prone)

# Vulnerable Services (recent CVEs)
vuln:CVE-2021-44228               # Log4Shell
vuln:CVE-2019-19781               # Citrix ADC RCE
vuln:CVE-2014-0160                # Heartbleed (still lingers)
vuln:CVE-2025-*                   # Replace with current CVEs

# Database & NoSQL
"MongoDB" "authentication disabled" port:27017
"redis" port:6379
"Memcached" port:11211
"elastic" port:9200 "_cat/indices"
"phpMyAdmin" port:80,443

# SSH / Remote Access
"SSH-2.0-OpenSSH" "root"          # Root login SSH
"authentication disabled" "RFB 003.008"  # Unauth VNC
"HP-ILO" OR "iLO" port:443        # HP iLO management
"Android Debug Bridge" port:5555   # ADB exposed
port:23 "root@" -login -password   # Open Telnet

# IoT / Cameras
port:554 has_screenshot:true       # RTSP cameras
"webcam" OR "DVR" OR "camera" port:80,81,8080
"NETGEAR" OR "Linksys" "admin"
tag:ics                            # Industrial Control Systems
"screenshot.label:ics"             # ML-tagged ICS

# Cloud / Container
"Amazon AWS" port:9200
"Docker" port:2375 "Docker Remote API"
"Kubernetes" port:6443 "kube-apiserver"
"Jenkins" "X-Jenkins" http.title:"Dashboard"
"X-Plex-Protocol" port:32400       # Plex media servers

# Ransomware
"encrypted attention" has_screenshot:true
"your files are encrypted"         # Ransom notes

# Fun / Legacy
port:17                           # Quote of the Day service
"HP-UX" OR "Windows 2000"          # Prehistoric OS still online
"printer" "ready"                  # Exposed printers

# Advanced Combos
country:GB port:80,443 vuln:CVE-*  # UK web servers + recent vulns
has_screenshot:true "default password" OR "admin:admin"
org:"your-company" -port:443        # Non-HTTPS exposures
has_screenshot:true tag:iot "password"

# ICS / SCADA (critical infrastructure)
tag:ics OR tag:scada
"Siemens, SIMATIC" port:161
"Server: CarelDataServer" "200 Document follows"
"HID VertX" port:4070
"smart install client active"      # Cisco Smart Install RCE

# NAS / Storage
"Authentication: disabled" port:445
"220" "230 Login successful." port:21  # Anonymous FTP
```

---

## ⚠️ Tips & Reminders

- **Always replace** `target.com` with your actual target
- **Deduplicate** — your repo has overlap between files; this master list removes duplicates
- **Add `-github -gitlab -pastebin`** when hunting secrets to avoid noise
- **Chain with `site:*.target.com`** for subdomain coverage
- **Shodan's `vuln:`** requires paid plan — free tier can't filter by CVE
- **Use `has_screenshot:true`** on Shodan for fast visual recon of exposed devices
- **Cloud buckets** (AWS/GCP/Azure) often leak via `intitle:"index of"` on public permissions

---

*Compiled by OriResearcher 🔍 from NyetNighy's Google_dork-List + ongoing OSINT research*