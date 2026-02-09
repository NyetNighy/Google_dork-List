# Curated Google & Shodan Dorks (Categorized)

> **Use only with explicit permission and within authorized scope.**

This list is an expanded, categorized set of dorks compiled from the existing lists in this repository.

## Google Dorks

### 1) Exposed Documents & Files
- `filetype:pdf site:target.com "confidential" | "internal use only" | "not for distribution"`
- `filetype:xlsx | filetype:xls | filetype:csv "password" | "credentials" | "api key"`
- `filetype:docx | filetype:doc intext:"password list" | "employee list"`
- `filetype:pdf site:target.com "budget" | "financial report" | "invoice"`
- `filetype:log inurl:"error" | "access" site:target.com`
- `filetype:sql "MySQL dump" "password" OR "CREATE TABLE" site:target.com`
- `filetype:bak | filetype:old | filetype:save | filetype:~ intext:"backup" site:target.com`
- `filetype:txt intext:"ssh private key" OR "BEGIN RSA PRIVATE KEY"`
- `filetype:json intext:"private_key" OR "client_secret" OR "bearer token"`
- `filetype:pdf site:target.com "password reset" | "temporary password" | "one-time password"`
- `filetype:xls | filetype:xlsx intext:"username" "password" -template -sample`
- `filetype:doc | filetype:docx intitle:"meeting notes" | "action items" "confidential"`
- `filetype:csv site:target.com "email" "phone" "address" "employee"`
- `filetype:log "error" "failed login" | "authentication failure" site:target.com`
- `filetype:txt | filetype:log intext:"DB_PASSWORD" OR "DATABASE_URL"`

### 2) Exposed Directories & Backups
- `intitle:"index of" "parent directory" (backup | .git | .env | config)`
- `intitle:"index of" "DCIM" | ".git" | "backup" | "logs" | "admin" | "private"`
- `intitle:"index.of" intext:"Apache" "Server at" -inurl:github`
- `intitle:"index of" "/backup/" | "/backups/" | "/db_backup/"`
- `intitle:"index of" "/uploads/" | "/files/" | "/downloads/" | "/media/"`
- `intitle:"index of" ".bak" | ".old" | ".sql" | ".zip" | ".tar.gz"`
- `intitle:"index of" "/wp-content/uploads/" -inurl:wordpress.org`
- `intitle:"index of /" ".ssh" | "id_rsa" | "authorized_keys"`
- `inurl:".env" intitle:"index of"`
- `intitle:"index of" "/config/" | "/settings/" | "/private/"`
- `intitle:"index of" intext:"Last modified" "parent directory" "mongodb" | "mysql"`
- `intitle:"index of" "/log/" | "/logs/" | "/error_log"`
- `intitle:"index of" ".git" "HEAD" OR "config"`
- `intitle:"index of" "/.aws/" | "/.azure/" | "/.gcp/"`

### 3) Admin / Login Panels
- `inurl:admin | inurl:login | inurl:signin | inurl:portal site:target.com`
- `intitle:"login" "powered by" (wordpress | joomla | drupal | magento)`
- `inurl:(wp-login.php | administrator | admin.php | login.aspx)`
- `intitle:"remote management" intext:"please enter password"`
- `inurl:(dashboard | controlpanel | cp | panel | manage) intitle:"login"`
- `inurl:"/wp-admin" | inurl:"/wp-login.php" site:target.com`
- `inurl:"/administrator" intitle:"Joomla"`
- `intitle:"Login" "Webmin"`
- `inurl:phpmyadmin | inurl:adminer | inurl:pma intitle:"phpMyAdmin"`
- `inurl:(webmail | roundcube | squirrelmail | horde) site:target.com`
- `inurl:/admin/console | inurl:/admin/login | inurl:/administrator`
- `intitle:"admin login" "powered by" (drupal | joomla | vbulletin | xenforo)`
- `inurl:".php" intitle:"login" intext:"forgot password" | "remember me"`
- `inurl:/login/index | inurl:/signin | inurl:/auth/login`
- `intitle:"Cpanel" | intitle:"WHM" | intitle:"Plesk" intext:"login"`
- `inurl:prometheus | inurl:grafana intitle:"login" | "sign in"`
- `inurl:/adminer.php | inurl:/dbadmin | inurl:/mysqladmin`

### 4) Config & Secret Leaks
- `ext:env | ext:yaml | ext:yml "DB_PASSWORD" | "API_KEY" | "SECRET_KEY"`
- `inurl:config filetype:xml | filetype:conf | filetype:ini`
- `intext:"aws_access_key_id" filetype:txt | filetype:log`
- `intext:"api_key" | "secret" | "token" ext:txt | ext:json -github`
- `ext:sql | ext:dmp | ext:dump intext:"password" | "pwd" | "pass"`
- `inurl:".git/config" intitle:"index of"`
- `inurl:".DS_Store" intitle:"index of"`
- `inurl:config/database.yml | inurl:config/app.php intext:"password"`
- `ext:properties | ext:props intext:"jdbc.password" | "db.password"`
- `inurl:".bak" ext:env | ext:ini | ext:conf "DB_USER" OR "API_SECRET"`
- `intext:"-----BEGIN PRIVATE KEY-----" filetype:txt | filetype:pem`
- `"AWS_ACCESS_KEY_ID" "AWS_SECRET_ACCESS_KEY" filetype:env`
- `filetype:env "AZURE_CLIENT_SECRET" OR "azure_client_id"`
- `filetype:env "GOOGLE_APPLICATION_CREDENTIALS" OR "private_key"`
- `"BEGIN PRIVATE KEY" filetype:key | filetype:pem`
- `"api_key" | "client_secret" filetype:yaml | filetype:json`
- `"JWT" "token" filetype:log | filetype:txt site:target.com`
- `intext:"sk_live_" | "pk_live_" OR "sk_test_" filetype:txt OR filetype:js`
- `inurl:firebase.json | inurl:".firebaserc" intext:"apiKey"`
- `intext:"MONGO_URI" | "MONGODB_URI" OR "MONGOLAB_URI" ext:env | ext:yaml`

### 5) Public Source / Repo Artifacts
- `inurl:".git" "HEAD" OR "config" intitle:"index of"`
- `inurl:"/.git/" "index of" site:target.com`
- `inurl:".svn" intitle:"index of"`
- `inurl:".hg" intitle:"index of"`
- `inurl:".DS_Store" site:target.com`
- `site:raw.githubusercontent.com intext:"password" OR intext:"api_key" OR intext:"secret" (filetype:env OR filetype:json OR filetype:yml OR filetype:js)`
- `site:pastebin.com intext:"AWS_SECRET" OR "private_key" OR "password" after:2025-01-01`

### 6) Error Pages & Debug Data
- `"stack trace" "exception" "error" site:target.com`
- `inurl:"/debug" | inurl:"/trace" | inurl:"/console" site:target.com`
- `"Warning: mysql_" "on line" filetype:php`
- `"Fatal error" "in" "on line" site:target.com`
- `"DEBUG" "TRACE" filetype:log site:target.com`
- `inurl:(phpinfo.php | test.php | info.php)`
- `intitle:"phpinfo" "PHP Version" inurl:phpinfo.php`
- `intext:"MySQL said: Documentation" | "Error establishing a database connection"`
- `inurl:server-status intitle:"Apache Status"`
- `intext:"X-Powered-By: PHP" intitle:"403" | "404" "forbidden"`
- `intext:"Django" "Debug = True" | "ALLOWED_HOSTS"`

### 7) Databases & Admin Tools
- `intitle:"phpMyAdmin" "Welcome to phpMyAdmin"`
- `inurl:"/adminer.php" "Login"`
- `intitle:"Mongo Express" "Login"`
- `intitle:"pgAdmin" "Login"`
- `intitle:"Database Error" "WordPress"`
- `intitle:"Jenkins" "login" intext:"Dashboard"`
- `intext:"Elasticsearch" "You Know, for Search"`
- `inurl:/server-status apache intitle:"apache status"`
- `intext:"phpMyAdmin" "running on" "MySQL"`

### 8) Cloud Storage & Buckets
- `site:s3.amazonaws.com "target" "index of"`
- `site:storage.googleapis.com "target"`
- `site:blob.core.windows.net "target"`
- `site:digitaloceanspaces.com "target"`
- `site:public.blob.core.windows.net "index of"`

### 9) Emails, Usernames & Contacts
- `site:target.com "@target.com" -inurl:(signup | login | career)`
- `"email" OR "@target.com" filetype:xls | filetype:csv | filetype:txt`
- `site:target.com intext:"@gmail.com" "@yahoo.com" intext:"contact"`
- `intext:"@target.com" intitle:"staff" | "directory" | "team"`
- `site:target.com intext:"@target.com" filetype:xlsx | filetype:csv | filetype:vcf`
- `"@target.com" intitle:"email list" | "contact list" | "distribution list"`
- `site:target.com intext:"@target.com" intext:"tel:" | "phone:" | "mobile:"`
- `intext:"@target.com" filetype:pdf intitle:"directory" | "staff directory"`
- `site:target.com "@" -inurl:(login | signup | career | jobs)`
- `intext:"username" "@target.com" filetype:txt | filetype:log`
- `site:target.com intext:"e-mail" | "email address" "contact us"`
- `"@target.com" intitle:"resume" | "cv" | "curriculum vitae"`
- `intext:"@target.com" inurl:(about | team | staff | employees)`
- `site:target.com filetype:vcard | filetype:vcf "@target.com"`

### 10) Subdomains & Related Assets
- `site:*.target.com -www -dev -staging -test -beta`
- `site:target.com -inurl:www`
- `site:target.com inurl:(dev | staging | test | uat | qa | beta)`
- `site:*.target.com -www -inurl:(blog | forum | shop | store)`
- `site:target-*.* | site:*.target-*`
- `site:target.com inurl:(api | api/v1 | api/v2 | graphql | rest)`
- `site:*.target.com inurl:(jenkins | sonar | nexus | artifactory)`
- `site:dev.target.com | site:staging.target.com | site:test.target.com`
- `site:target.com inurl:(kibana | elasticsearch | logstash)`
- `site:*.target.com intitle:"default web page" | "under construction"`
- `site:target.com -inurl:www intext:"server" "hostname"`
- `site:internal.target.com | site:intranet.target.com`
- `site:*.target.com filetype:php intitle:"phpinfo"`

### 11) Tech Signatures & Misconfigurations
- `intext:"powered by" (phpmyadmin | roundcube | webmail)`
- `intitle:"welcome to" "nginx" OR "apache" "server at"`
- `intext:"MySQL dump" (pass | password | pwd) filetype:sql`
- `intext:"Elasticsearch" "You Know, for Search"`
- `intitle:"phpMyAdmin" "Welcome to phpMyAdmin" -intitle:"login"`

### 12) IoT / Camera / Device Panels
- `inurl:(viewerframe?mode=motion | view/index.shtml | axis-cgi/mjpg)`
- `intitle:"Live View / — AXIS" | "webcamXP" | "D-Link Internet Camera"`
- `inurl:"top.htm" intitle:"BlueNet Video Server"`
- `intitle:"printer status" intext:"HP LaserJet"`
- `intitle:"Web Viewer" intext:"ID" "Password" (axis | sony | panasonic)`
- `inurl:"view/viewer_index.shtml" intext:"Live Video"`
- `intitle:"DVR Login" | intitle:"NVR Login" intext:"Username" "Password"`
- `inurl:"/cgi-bin/guestimage.html" | inurl:"/cgi-bin/viewer/video.jpg"`
- `intitle:"GoAhead WebServer" intext:"Login" "Camera"`
- `inurl:"onvif/device_service" | inurl:"onvif/snapshot"`
- `intitle:"Ricoh" "Printer" intext:"Web Image Monitor"`
- `inurl:"port_37777" | inurl:"port_554" intitle:"RTSP" "stream"`
- `intitle:"Brother" "Web Based Management" intext:"password"`
- `inurl:"/webcam/" | inurl:"/mjpg/video.mjpg" | inurl:"/video.cgi"`

### 13) Bug Bounty / Program Discovery
- `inurl:(bug bounty | security | vulnerability | responsible disclosure) site:target.com`
- `intext:"we welcome responsible disclosure" site:*.target.*`
- `"bugcrowd" | "hackerone" | "yeswehack" "target.com"`

### 14) Quick Recon Combos (replace target.com)
- `site:target.com (ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:inc)`
- `site:target.com (inurl:admin | inurl:login | intitle:admin)`
- `intitle:"index of" site:target.com (backup | .git | .svn | .env | logs)`
- `site:target.com (filetype:sql | filetype:bak | filetype:old | filetype:~) ("password" OR "credential" OR "key")`
- `site:target.com intitle:"index of" ("/admin/" | "/config/" | "/uploads/" | "/private/" | "/secure/")`
- `site:target.com (inurl:login | inurl:admin | inurl:dashboard) (intitle:login | intitle:admin | intitle:dashboard)`
- `site:target.com (ext:env | ext:yml | ext:yaml | ext:json) ("secret" OR "key" OR "token" OR "password")`
- `site:target.com (inurl:wp-admin | inurl:wp-login | inurl:xmlrpc.php) -inurl:wordpress.com`
- `site:target.com (filetype:pdf | filetype:docx | filetype:xlsx) ("confidential" OR "internal" OR "proprietary")`
- `site:target.com (inurl:api | inurl:graphql | inurl:rest | inurl:v1 | inurl:v2) (intitle:"api" OR intext:"swagger")`
- `site:target.com (intitle:"phpinfo" OR inurl:phpinfo.php OR inurl:test.php OR inurl:info.php)`
- `site:target.com (inurl:jenkins | inurl:sonarqube | inurl:nexus | inurl:artifactory | inurl:gitlab)`
- `site:target.com (filetype:txt | filetype:log | filetype:csv) ("email" OR "@target.com" OR "username" OR "password")`

### 15) Private Keys, Certs & Wallets
- `intext:"-----BEGIN PRIVATE KEY-----" OR "-----BEGIN RSA PRIVATE KEY-----" filetype:txt OR filetype:pem OR filetype:key`
- `intitle:"index of" "id_rsa" OR "id_ed25519" OR ".pem" -html`
- `intitle:"index of" "wallet.dat" OR "keystore.jks" OR "keystore.bks"`

### 16) Sensitive Config Files
- `intitle:"index of" "sitemanager.xml" OR "FileZilla.xml" OR "recentservers.xml"`
- `intitle:"index of" ".htpasswd" OR ".htaccess" OR "web.config"`
- `filetype:ovpn OR filetype:conf intext:"auth-user-pass" OR "http-proxy"`
- `filetype:rdp intext:"full address" OR "username" OR "password 51:b"`

---

## Shodan Dorks

### 1) Basic Filters & Scope
- `org:"Amazon.com"`
- `country:GB`
- `city:"Southend-on-Sea"`
- `net:8.8.8.0/24`
- `port:80,443,8080`
- `isp:"Comcast Cable"`
- `asn:AS15169`
- `hostname:"vpn.target.com"`
- `product:"Apache httpd"`
- `os:"Windows"`
- `os:"Linux"`
- `before:2024-01-01`
- `after:2025-01-01`

### 2) Web / HTTP Exposures
- `http.title:"Index of /"`
- `http.component:"wordpress"`
- `"http.title:\"phpMyAdmin\""`
- `http.html:"wp-config.php"`
- `x-powered-by:"PHP/5"`
- `http.title:"Welcome to nginx!"`
- `http.title:"Dashboard" http.component:"grafana"`
- `http.html:"/wp-admin" port:80,443`
- `http.title:"Kibana" port:5601`
- `http.title:"GitLab" port:80,443`
- `http.title:"Jenkins" port:8080`
- `http.title:"SonarQube" port:9000`
- `http.title:"RabbitMQ Management" port:15672`
- `http.title:"Prometheus Time Series Collection and Processing Server" port:9090`
- `http.title:"InfluxDB - Admin Interface" port:8086`
- `http.title:"phpMyAdmin" port:80,443`
- `http.title:"OpenVPN Connect" port:943`

### 3) Vulnerable Services & CVE Tags
- `vuln:CVE-2014-0160`
- `vuln:CVE-2021-44228`
- `vuln:CVE-2019-19781`
- `vuln:CVE-2023-*`
- `vuln:CVE-2024-*`
- `"OpenSSL/1.0.1" port:443`
- `"Apache/2.4." vuln:CVE-*`
- `vuln:CVE-2022-*`
- `vuln:CVE-2020-*`
- `vuln:CVE-2017-*`
- `ssl.version:TLSv1`
- `ssl.cert.issuer.cn:"Let's Encrypt"`

### 4) Remote Access & Admin Services
- `ssh port:22`
- `ssh -port:22`
- `"SSH-2.0-OpenSSH" "root"`
- `"authentication disabled" "RFB 003.008"`
- `port:23 "root@" -login -password`
- `"Intel(R) Active Management Technology" port:16992,16993`
- `"HP-ILO" OR "iLO" port:443`
- `"Android Debug Bridge" port:5555`
- `port:3389 os:"Windows"`
- `"RDP" port:3389`
- `port:5900 "VNC Authentication"`
- `"TeamViewer" port:5938`
- `"OpenVPN" port:1194`

### 5) Databases & Caches
- `"MongoDB" "authentication disabled" port:27017`
- `"redis" port:6379`
- `"Memcached" port:11211`
- `"CouchDB" port:5984`
- `"Elasticsearch" port:9200`
- `"MySQL" port:3306`
- `"PostgreSQL" port:5432`
- `"RethinkDB" port:28015`
- `"MariaDB" port:3306`
- `"Oracle" port:1521`
- `"Microsoft SQL Server" port:1433`
- `"Cassandra" port:9042`
- `"Neo4j" port:7474`

### 6) IoT / OT / Device-Specific
- `port:554 has_screenshot:true`
- `"webcam" OR "DVR" OR "camera" port:80,81,8080`
- `"Intel(R) Active Management Technology" port:16992,16993`
- `tag:ics`
- `"Server: HP HTTP" "Serial Number:"`
- `"Server: EPSON-HTTP" OR "EPSON_Linux UPnP"`
- `"Server: CANON HTTP Server"`
- `"Server: KS_HTTP"`
- `"Chromecast:" port:8008`
- `port:1883 "MQTT"`
- `port:47808 "BACnet"`
- `port:502 "Modbus"`
- `port:102 "S7"`
- `port:161 "SNMP"`
- `"Siemens" port:102`
- `"BACnet" "Device"`
- `tag:scada`

### 7) Screenshots & Visual Recon
- `has_screenshot:true`
- `screenshot.label:ics`
- `screenshot.label:webcam`
- `screenshot.label:router`
- `has_screenshot:true http.title:"Login"`
- `has_screenshot:true port:554`
- `has_screenshot:true http.title:"Index of /"`
- `has_screenshot:true http.title:"Dashboard"`
- `has_screenshot:true http.title:"Camera"`

---

## Sources in this repository
- `DorkList`
- `Dorks_Web__List`
- `ShodanDorks`
