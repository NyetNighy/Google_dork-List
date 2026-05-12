# 🔍 Alternative Search Engines & Dork Reference

> **Coverage:** Censys, Fofa, Quake, ZoomEye, BinaryEdge, Hunter, CrimeFlare, LeakIX, PublicIntelligence, GreyNoise, and more  
> **Last updated:** May 12, 2026  
> **Usage:** OSINT, reconnaissance, threat intel. Use only with permission.

---

## 1. Censys — [censys.io](https://censys.io)

> **Focus:** Internet-wide scanning data (certificates, DNS, web servers, SSL configs)  
> **Free tier:** 10 queries/day on legacy search. New search requires account.

### Search Syntax
```
# Certificates
cert.subject.common_name: target.com
cert.subject.common_name: *.target.com
cert.issuer.organization: "Let's Encrypt"
cert.text_value: "password" or "secret"
cert.extensions.keyUsage: "Digital Signature"
cert.serial: <hex_serial>

# Web Hosts
autonomous_system.asn: 15169
location.country: "United States"
protocols: "443/tls"
services.http.response.headers.server: "nginx"
services.http.title: "Index of /"
services.ssh.software.version: "OpenSSH 7.*"
protocols: "22/ssh"

# SSL/TLS
services.tls.certificates.leaf_data.subject.common_name: "target.com"
services.tls.certificates.leaf_data.issuer.common_name: "DigiCert"
services.tls.version: "TLS 1.2"
services.tls.ja3s: "<ja3_hash>"

# Specific Technologies
services.http.component.name: "jQuery"
services.http.component.version: "3.6.0"
services.banner: "MongoDB"
protocols: "27017/tcp"

# Combined Examples
cert.subject.common_name: "target.com" and location.country: "US"
services.tls.certificates.leaf_data.subject.common_name: "*.target.com"
autonomous_system.asn: 15169 and protocols: "443/tls"
services.http.response.body: "phpMyAdmin"
```

### Censys-Specific Dorks
```
# Subdomains via certificate transparency
cert.subject.common_name: /target\.(com|org|net)/

# Exposed panels via banner
services.http.response.body: "Welcome to phpMyAdmin"
services.http.response.body: "Dashboard [Jenkins]"

# Tech fingerprinting
services.http.headers.set_cookie: "wordpress_logged_in"
services.banner: "ssh-ed25519"
services.tls.certificates.leaf_data.signature.algorithm: "SHA256-RSA"

# Find exposed databases
services.port: 27017 and services.banner: "MongoDB"
services.port: 6379 and services.banner: "redis"
services.port: 9200 and services.banner: "elasticsearch"
services.port: 5432 and services.banner: "postgres"

# Find exposed dashboards
services.http.title: "Grafana"
services.http.title: "Jenkins"
services.http.title: "Kibana"
```

---

## 2. FOFA — [fofa.info](https://fofa.info)

> **Focus:** Global asset discovery — IP, port, protocol, web fingerprinting  
> **API:** Requires paid subscription for API access. Web has rate limits.

### Search Syntax
```
# Basic
domain="target.com"
host=".target.com"
ip="1.2.3.4/24"
port="443"
protocol="http"
server="nginx"
os="Windows"

# Cert-based
cert="target.com"
cert.body="password"
cert.subject="*.target.com"

# Protocol/Service
protocol=="ssh"
protocol=="mysql"
service=="http"
app="Nginx"
lang="Chinese"

# Technology fingerprint
app="Apache"
app="phpMyAdmin"
app="Microsoft-IIS"
framework="Spring"
framework="Laravel"

# Combined
domain="target.com" && port="443"
host="*.target.com" && server="nginx"
ip="1.2.3.0/24" && app="Redis"

# File/Cookie fingerprints
header="PHPSESSID"
header="X-Jenkins"
cookie="wordpress_logged_in"
body="index of /admin"
body="500 Internal Server Error"
```

### FOFA-Specific Dorks
```
# Find dev/staging environments
domain="target.com" && (app="Jenkins" || app="GitLab")
host=".internal.target.com"
domain="target.com" && server="Apache/2.4.41"

# Find exposed panels
app="phpMyAdmin" && port="80"
app="Zabbix" && port="80"
app="Grafana" && port="3000"

# Find technologies by header
header="Server: nginx" && header="X-Powered-By: PHP/7.4"

# Cloud exposures
cloud_azure="true"
cloud_aws="true"
cloud_gcp="true"
```

---

## 3. Quake — [quake.360.cn](https://quake.360.cn)

> **Focus:** Chinese and global asset discovery, ICS/SCADA specialized  
> **API:** Requires registration. Web-based free tier available.

### Search Syntax
```
# Basic
app:"nginx"
app:"Apache"
app:"phpMyAdmin"
os:"Linux"
os:"Windows Server 2019"

# Port-based
port:"443"
port:"22"
port:"3389"
port:"8080"

# Service
service:"ssh"
service:"http"
service:"mysql"
service:"mongodb"

# Combined
app:"Redis" && port:"6379"
app:"Jenkins" && port:"8080"
app:"MongoDB" && port:"27017"

# Location
country:"CN"
country:"US"
city:"Beijing"
```

### Quake-Specific Dorks
```
# ICS / SCADA
app:"Siemens" && os:"SIMATIC"
app:"Modbus" && port:"502"
app:"BACnet" && port:"47808"

# Exposed databases
app:"MongoDB" && country:"US"
app:"Redis" && port:"6379"
app:"Elasticsearch" && port:"9200"

# Webcams / IoT
app:"Hikvision"
app:"Dahua"
app:"Milestone"
app:"Avigilon"
```

---

## 4. ZoomEye — [zoomeye.org](https://zoomeye.org)

> **Focus:** Chinese-developed, strong on web tech and ICS/SCADA  
> **API:** Requires login. Free tier has daily quota.

### Search Syntax
```
# Web technology
app:"nginx"
app:"Apache"
app:"IIS"
app:"phpMyAdmin"
app:"WordPress"

# Device/IoT
device:"router"
device:"camera"
device:"switch"
device:"firewall"

# Service
service:"ssh"
service:"ftp"
service:"telnet"
service:"rdp"

# Combined
app:"phpMyAdmin" + country:"US"
device:"camera" + city:"London"
service:"ssh" + os:"Linux"

# Port filters
port:22,443,80,8080
port:6379
port:27017
```

### ZoomEye-Specific Dorks
```
# Web admin panels
app:"DVR" + port:8000
app:"NVR" + port:8000
app:"IP Camera" + port:80

# Find specific technologies
app:"Apache Shiro" && country:"US"
app:"Struts" && country:"US"
app:"ThinkPHP" && country:"CN"

# Find vulnerable/interesting services
app:"Redis" + country:"US"
app:"MongoDB" + country:"DE"
```

---

## 5. BinaryEdge — [binaryedge.io](https://binaryedge.io)

> **Focus:** Cloud and web exposure data, good for recent vulns  
> **Free tier:** Limited queries per month.

### Search Syntax
```
# Type-based
type:server
type:webcam
type:ics
type:databases
type:mail

# Query examples
query: "target.com"
query: "port:443 and product:nginx"
query: "product:mysql and port:3306"
query: "webcam" and country:"US"

# Tags
tag:ics
tag:scada
tag:cloud
tag:database
tag:camera

# Combined
query: "tag:ics and product:siemens"
query: "tag:database and product:mongodb"
```

### BinaryEdge-Specific Dorks
```
# Exposed cloud storage
query: "port:9000 and product:minio"
query: "port:9000 and product:s3"

# Exposed containers
query: "port:2375 and product:docker"
query: "port:6443 and product:kubernetes"

# Exposed databases
query: "tag:database and product:redis"
query: "tag:database and product:elasticsearch"
```

---

## 6. Hunter.io — [hunter.io](https://hunter.io)

> **Focus:** Email discovery, corporate email patterns, employee enumeration  
> **Free tier:** Limited searches/month. Requires API key for bulk.

### Search Syntax
```
# Domain search
domain: target.com
domain: target.com AND senior

# Email pattern
domain: target.com AND type:personal
domain: target.com AND pattern: {first}.{last}@target.com

# Company searches
company: "Target Inc"
company: "Target Corp" AND senior

# Job title searches
title: "CISO"
title: "IT Manager"
title: "Network Engineer"
```

### Hunter-Specific Dorks
```
# Find corporate email format
domain:target.com "pattern:{f}.{l}@target.com"
domain:target.com "pattern:{first}{last}@target.com"
domain:target.com "pattern:{first}_{last}@target.com"

# Find employees by role
domain:target.com "title:CISO"
domain:target.com "title:VP of Engineering"
domain:target.com "title:IT Administrator"

# Find IT/security contacts
domain:target.com "title:Security"
domain:target.com "title:Network"
domain:target.com "title:System Administrator"
```

---

## 7. LeakIX — [leakix.net](https://leakix.net)

> **Focus:** Open port/asset discovery + reported leaks  
> **Access:** Public beta with limited free access.

### Search Syntax
```
# Basic
tag:exposed
tag:leak
product:mongodb
product:mysql
product:redis

# Port-based
port:27017
port:6379
port:3306
port:5432

# Combined
product:mongodb AND tag:exposed
product:redis AND tag:open
```

### LeakIX-Specific Dorks
```
# Exposed databases
product:mongodb tag:exposed
product:mysql tag:exposed
product:redis tag:exposed

# Exposed services
product:elasticsearch tag:exposed
product:kibana tag:exposed
product:jenkins tag:exposed
```

---

## 8. GreyNoise — [greynoise.io](https://greynoise.io)

> **Focus:** Internet noise — mass scanners, bots, crawlers. Ignore benign, find malicious.  
> **API:** Free tier limited. Community tier available.

### Search Syntax
```
# IP lookup
ip: 1.2.3.4

# Tag-based (mass scanners)
tag: "masscan"
tag: "shodan"
tag: "censys"
tag: "nmap"
tag: "hydra"
tag: "sqlmap"

# Classification
classification: "malicious"
classification: "benign"
classification: "unknown"

# ASN / Country
asn: "AS15169"
country: "CN"

# Last seen
last_seen: "2026-05-01"
last_seen: "7d"

# OS / Category
os: "Linux"
category: "scanner"
```

### GreyNoise-Specific Dorks
```
# Find active scanners in your ASN
asn: AS15169 AND tag:scanner

# Find recent malicious activity
classification:malicious AND last_seen:1d

# Exclude known benign (Shodan/Censys noise)
tag:shodan AND NOT classification:benign

# Find botnets / C2 callbacks
category: "bot" AND last_seen:1d

# Web vulnerability scanners
tag: "sqlmap"
tag: "nikto"
tag: "dirbuster"
```

---

## 9. Shodan — [shodan.io](https://shodan.io)

> **Already documented in COMBINED_DORKS.md — quick reference below**

```
# Basic
port:80,443,8080
product:Apache
http.title:"Index of /"
has_screenshot:true

# Vulns
vuln:CVE-2021-44228
vuln:CVE-2019-19781

# Cloud
"Docker" port:2375
"Kubernetes" port:6443

# IoT / Cameras
port:554 has_screenshot:true
"webcam" port:80,81,8080

# Databases
"MongoDB" port:27017 "authentication disabled"
"redis" port:6379
"elastic" port:9200
```

---

## 10. PublicIntelligence — [publicintelligence.info](https://publicintelligence.info)

> **Focus:** Heavily curated OSINT reference. Useful for dork collections and methodology.

### Search Tips
- Great source for methodology and dork lists, not live scanning
- Good for finding dork collections and cheat sheets
- Browse by category: network, infrastructure, people, documents

---

## 11. CrimeFlare — [crimeflare.net](https://crimeflare.net)

> **Focus:** Cloudflare bypass — find real IP behind CDN/WAF protection  
> **Tools:** Cloudflare enumerator, DNS databases, ssl certificates

### Usage
```
# Find real IP behind Cloudflare
1. Search crimeflare.net for target domain
2. Query their DNS database
3. Cross-reference with Censys certificate search:
   cert.subject.common_name: "target.com"

# Alternative: Censys trick
cert.subject.common_name: "target.com" 
→ look for self-signed/mismatched certs
```

---

## 12. crt.sh — [crt.sh](https://crt.sh)

> **Focus:** Certificate Transparency logs — subdomains, internal hosts, dev environments

### Usage
```
# Subdomain enumeration via CT logs
1. Go to crt.sh
2. Search: %.target.com
3. Export results → parse unique subdomains

# Automation
curl -s "https://crt.sh/?q=%.target.com&output=json" | jq -r '.[].name_value'

# Find internal/dev subdomains
%.dev.target.com
%.staging.target.com
%.test.target.com
%.internal.target.com
%.admin.target.com
%.uat.target.com
```

---

## 13. DNSdumpster — [dnsdumpster.com](https://dnsdumpster.com)

> **Focus:** Passive DNS recon, subdomain discovery, network mapping

### Usage
```
# Real-world usage
1. Enter target.com
2. Review: subdomains, MX, TXT, DNS, host records
3. Download full report (CSV/XLS)
4. Cross-reference with other engines
```

---

## 14. VirusTotal — [virustotal.com](https://virustotal.com)

> **Focus:** Malware scanning, URL analysis, passive DNS, domain relationships

### Search Syntax (GUI-based, but API available)
```
# Subdomains
domain: target.com → View relations

# Historical DNS
target.com → Historical WHOIS → DNS records

# URL scanning
url: "target.com/admin"
url: "target.com/wp-login.php"

# File hashes
hash: <sha256>

# Retro hunt ( hunt for patterns across VT )
keyword: "target.com" category: "payload"
```

---

## 15. SecurityTrails — [securitytrails.com](https://securitytrails.com)

> **Focus:** Historical DNS, WHOIS, subdomain enumeration, passive sensors

### Search Syntax
```
# Subdomains
domain: target.com → Subdomains

# Historical DNS
target.com → Historical → All DNS records

# DNS records
A, AAAA, MX, NS, TXT, CNAME records

# WHOIS
target.com → Registrant, Admin, Tech contacts

# API examples (key required)
curl -G "https://api.securitytrails.com/v1/domain/target.com/subdomains" \
  -H "APIKEY: <key>"
```

---

## 16. FullHunt — [fullhunt.io](https://fullhunt.io)

> **Focus:** Attack surface discovery, threat actor TTP mappings

### Usage
```
# Find exposed attack surface
domain: target.com

# Check for vulnerable instances
target.com (jenkins, gitlab, grafana, etc)

# Track exposed services over time
```

---

## 17. Netlas — [netlas.io](https://netlas.io)

> **Focus:** Asset discovery, technology fingerprinting, DNS records

### Search Syntax
```
# Technology
response:"phpMyAdmin"
response:"Apache"
response:"nginx"

# Certificates
cert.cn:"target.com"
cert.org:"Target Inc"

# DNS
dns:A:"1.2.3.4"
dns:ptr:"*.target.com"

# Combined
response:"nginx" AND geo:"US"
```

---

## 18. Detective — [detective.io](https://detective.io)

> **Focus:** OSINT for investigations, social media, corporate data, dark web mentions

### Usage
```
# Monitor target brand across platforms
target.com → Track mentions, pastebin, breaches, dark web

# Good for attack surface monitoring
```

---

## 19. Spyse — [spyse.com](https://spyse.com)

> **Focus:** Detailed technical OSINT — subdomains, ports, CVE, technologies

### Search Syntax
```
# Subdomains
target.com → Subdomains

# Port scan data
target.com → Ports → All open ports

# Technologies
target.com → Technologies → Stack fingerprint

# CVE
target.com → CVE → Known vulnerabilities
```

---

## 20. Onyphe — [onyphe.io](https://onyphe.io)

> **Focus:** Cyber defense search engine — passive recon, CVE data

### Search Syntax
```
# IP
ip:1.2.3.4

# Domain
dork:domain:target.com

# CVE
cve:CVE-2021-44228

# Product
product:nginx
product:mysql
product:redis

# Category
category:databases
category:ics
category:webcam
```

---

## 21. Buckets by GrayHatWarfare — [buckets.grayhatwarfare.com](https://buckets.grayhatwarfare.com)

> **Focus:** Public cloud storage buckets (AWS S3, Azure Blob, GCP Storage)

### Usage
```
# Search for exposed cloud buckets
target
target.com
target-backup
target-prod
target-dev
target-assets

# Extensions
.pdf
.sql
.backup
.env
```

---

## 22. Thingful — [thingful.net](https://thingful.net)

> **Focus:** IoT search engine — cameras, sensors, devices indexed from Shodan/Censys data

### Usage
```
# Find specific IoT
location: London
camera
sensor
industrial
```

---

## 📊 Quick Comparison Table

| Engine | Focus | Best For | Free Tier |
|--------|-------|----------|-----------|
| **Shodan** | Everything, visual | Network devices, vulns, IoT | Limited, vuln: paid |
| **Censys** | Certs, SSL, ASN | Subdomain enum, cloud, SSL configs | 10/day (legacy) |
| **FOFA** | Global assets | Chinese targets, web tech fingerprint | Limited |
| **Quake** | Chinese assets | ICS/SCADA, Chinese infrastructure | Limited |
| **ZoomEye** | Web + devices | Chinese + global, web tech, IoT | Daily quota |
| **BinaryEdge** | Cloud, web | Recent vulns, cloud storage | Limited/month |
| **Hunter** | Email | Employee enumeration, email patterns | Limited |
| **GreyNoise** | Scanner traffic | Filter noise, find malicious scanners | Limited |
| **LeakIX** | Open ports, leaks | Exposed DBs, recent leaks | Beta limited |
| **Censys (ASM)** | Attack surface | Subdomain takeover, continuous monitoring | Paid |
| **crtsh** | Certificates | Subdomain enum via CT logs | Unlimited |
| **DNSdumpster** | Passive DNS | Subdomain discovery, network mapping | Free |
| **VirusTotal** | Malware, DNS | Cross-reference, historical WHOIS | Limited |
| **SecurityTrails** | Historical DNS | Subdomains, historical records | Limited |
| **Netlas** | Asset discovery | Technology fingerprinting | Limited |
| **Onyphe** | Cyber defense | CVE search, passive recon | Limited |
| **Buckets** | Cloud storage | Public S3/Azure/GCP buckets | Free |

---

## 🔄 Workflow: Combining Engines

```
1. crt.sh → Subdomain enum (CT logs)
2. DNSdumpster → Passive DNS records
3. SecurityTrails → Historical DNS, WHOIS
4. Censys → Cert transparency, SSL configs
5. FOFA / ZoomEye → Web tech fingerprint
6. Shodan / BinaryEdge → Port details, vulns
7. Hunter → Employee/email enumeration
8. GreyNoise → Filter scanner noise
9. LeakIX → Recent exposures
10. Buckets → Cloud storage leaks
```

---

*Compiled by OriResearcher 🔍 | Part of the Google_dork-List OSINT suite*  
*Add new engines as you discover them. Keep this file updated.*