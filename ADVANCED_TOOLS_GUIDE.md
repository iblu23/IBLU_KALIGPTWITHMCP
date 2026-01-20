# 🔥 Advanced Penetration Testing Tools Guide

## 📋 Overview
This guide covers 50+ advanced penetration testing tools added to your HexStrike platform, organized by category with practical usage examples.

---

## 🕵️ OSINT & Advanced Reconnaissance

### theHarvester
**Purpose:** Gather emails, subdomains, hosts, employee names from public sources

**Installation:**
```bash
sudo apt install theharvester
```

**Usage Examples:**
```bash
# Search all sources for domain
theharvester -d example.com -b all

# Search specific sources
theharvester -d example.com -b google,bing,linkedin

# Save results to file
theharvester -d example.com -b all -f output.html
```

### Amass
**Purpose:** Advanced DNS enumeration & attack surface mapping

**Installation:**
```bash
sudo apt install amass
```

**Usage Examples:**
```bash
# Basic subdomain enumeration
amass enum -d example.com

# Passive enumeration only
amass enum -passive -d example.com

# Active enumeration with brute force
amass enum -active -d example.com -brute

# Output to file
amass enum -d example.com -o subdomains.txt
```

### SpiderFoot
**Purpose:** Automated OSINT framework for comprehensive reports

**Installation:**
```bash
sudo apt install spiderfoot
```

**Usage Examples:**
```bash
# Start SpiderFoot web interface
spiderfoot -l 127.0.0.1:5001

# CLI mode
spiderfoot -s example.com -t DOMAIN
```

### Maltego
**Purpose:** Visual relationship mapping (people, infrastructure, domains)

**Installation:**
```bash
# Download from official site or use installer script
wget https://maltego-downloads.s3.us-east-2.amazonaws.com/linux/Maltego.v4.6.0.deb
sudo dpkg -i Maltego.v4.6.0.deb
```

**Usage:**
- Launch GUI and create transforms
- Map relationships between entities
- Great for visual reporting

### Shodan CLI
**Purpose:** Internet-exposed services intelligence

**Installation:**
```bash
pip3 install shodan
shodan init YOUR_API_KEY
```

**Usage Examples:**
```bash
# Search for Apache servers
shodan search apache

# Get host information
shodan host 8.8.8.8

# Download search results
shodan download results apache country:US
```

---

## 🌐 Web Application Testing (Advanced)

### WhatWeb
**Purpose:** Web technology fingerprinting

**Installation:**
```bash
sudo apt install whatweb
```

**Usage Examples:**
```bash
# Basic scan
whatweb https://example.com

# Aggressive scan
whatweb -a 3 https://example.com

# Scan from file
whatweb -i targets.txt
```

### HTTPx
**Purpose:** Fast HTTP probing & tech detection

**Installation:**
```bash
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

**Usage Examples:**
```bash
# Probe URLs from file
cat urls.txt | httpx

# Technology detection
httpx -l targets.txt -tech-detect

# Extract titles and status codes
httpx -l targets.txt -title -status-code

# Follow redirects
httpx -l targets.txt -follow-redirects
```

### XSStrike
**Purpose:** Advanced XSS detection & exploitation

**Installation:**
```bash
git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike
pip3 install -r requirements.txt
```

**Usage Examples:**
```bash
# Basic XSS scan
python3 xsstrike.py -u "http://example.com/search?q=test"

# Crawl and scan
python3 xsstrike.py -u "http://example.com" --crawl

# Custom payload
python3 xsstrike.py -u "http://example.com/search?q=test" --payload "<script>alert(1)</script>"
```

### Commix
**Purpose:** Command injection testing

**Installation:**
```bash
git clone https://github.com/commixproject/commix.git
cd commix
python3 commix.py --install
```

**Usage Examples:**
```bash
# Test URL for command injection
python3 commix.py --url="http://example.com/page?id=1"

# POST request testing
python3 commix.py --url="http://example.com/login" --data="user=admin&pass=test"

# Cookie-based injection
python3 commix.py --url="http://example.com" --cookie="session=value"
```

### Arjun
**Purpose:** HTTP parameter discovery

**Installation:**
```bash
pip3 install arjun
```

**Usage Examples:**
```bash
# Discover parameters
arjun -u https://example.com/api

# Use custom wordlist
arjun -u https://example.com -w wordlist.txt

# POST method
arjun -u https://example.com -m POST
```

---

## 🛡️ Vulnerability Scanning & Management

### Faraday
**Purpose:** Vulnerability management & collaboration platform

**Installation:**
```bash
pip3 install faraday-client
```

**Usage Examples:**
```bash
# Start Faraday server
faraday-server

# Import nmap results
faraday-client --import nmap_scan.xml
```

### Vulners Scanner
**Purpose:** CVE-focused vulnerability scanning

**Installation:**
```bash
pip3 install vulners
```

**Usage Examples:**
```bash
# Search for vulnerabilities
python3 -c "import vulners; v = vulners.Vulners(); print(v.search('apache 2.4.49'))"
```

### Nuclei (Custom Templates)
**Purpose:** Fast vulnerability scanner with YAML templates

**Installation:**
```bash
sudo apt install nuclei
nuclei -update-templates
```

**Usage Examples:**
```bash
# Scan with all templates
nuclei -u https://example.com

# Scan with specific template
nuclei -u https://example.com -t cves/

# Custom template
nuclei -u https://example.com -t custom-template.yaml

# Scan multiple targets
nuclei -l targets.txt -severity critical,high
```

---

## 💣 Exploitation (Advanced)

### Searchsploit
**Purpose:** Offline Exploit-DB access

**Installation:**
```bash
sudo apt install exploitdb
```

**Usage Examples:**
```bash
# Search for exploits
searchsploit apache 2.4

# Update database
searchsploit -u

# Copy exploit to current directory
searchsploit -m 12345

# Search by CVE
searchsploit --cve 2021-44228
```

### BeEF (Browser Exploitation Framework)
**Purpose:** Browser exploitation framework

**Installation:**
```bash
sudo apt install beef-xss
```

**Usage Examples:**
```bash
# Start BeEF
beef-xss

# Access web interface at http://127.0.0.1:3000/ui/panel
# Default credentials: beef:beef
```

### Empire
**Purpose:** Post-exploitation & C2 (PowerShell focus)

**Installation:**
```bash
cd /opt/Empire
./setup/install.sh
```

**Usage Examples:**
```bash
# Start Empire
./empire

# Create listener
listeners
uselistener http
execute

# Generate stager
usestager windows/launcher_bat
execute
```

### CrackMapExec
**Purpose:** Active Directory exploitation Swiss-army knife

**Installation:**
```bash
pip3 install crackmapexec
```

**Usage Examples:**
```bash
# SMB enumeration
crackmapexec smb 192.168.1.0/24

# Credential spraying
crackmapexec smb 192.168.1.0/24 -u users.txt -p passwords.txt

# Pass-the-hash
crackmapexec smb 192.168.1.10 -u admin -H NTLM_HASH

# Execute commands
crackmapexec smb 192.168.1.10 -u admin -p password -x "whoami"
```

---

## 🎯 Post-Exploitation & Lateral Movement

### BloodHound
**Purpose:** Active Directory attack path mapping

**Installation:**
```bash
sudo apt install bloodhound
```

**Usage Examples:**
```bash
# Start BloodHound
bloodhound

# Collect data with SharpHound
./SharpHound.exe --CollectionMethod All

# Import data into BloodHound
# Use GUI to import JSON files
```

### Responder
**Purpose:** LLMNR/NBT-NS poisoning

**Installation:**
```bash
sudo apt install responder
```

**Usage Examples:**
```bash
# Start Responder
responder -I eth0

# Analyze mode (no poisoning)
responder -I eth0 -A

# Disable specific protocols
responder -I eth0 -w -f
```

### Impacket
**Purpose:** Network protocol exploitation scripts

**Installation:**
```bash
sudo apt install impacket-scripts
```

**Usage Examples:**
```bash
# PSExec
impacket-psexec domain/user:password@192.168.1.10

# SecretsDump
impacket-secretsdump domain/user:password@192.168.1.10

# GetNPUsers (ASREPRoast)
impacket-GetNPUsers domain/ -usersfile users.txt -dc-ip 192.168.1.10
```

### SharpHound
**Purpose:** BloodHound data collector

**Installation:**
```bash
# Download from GitHub
wget https://github.com/BloodHoundAD/BloodHound/releases/latest/download/SharpHound.exe
```

**Usage Examples:**
```bash
# Collect all data
./SharpHound.exe --CollectionMethod All

# Stealth collection
./SharpHound.exe --Stealth

# Specific collection
./SharpHound.exe --CollectionMethod Session,LoggedOn
```

---

## 🔬 Forensics & Incident Response

### Plaso (log2timeline)
**Purpose:** Timeline creation from logs and artifacts

**Installation:**
```bash
sudo apt install plaso
```

**Usage Examples:**
```bash
# Create timeline
log2timeline.py timeline.plaso /path/to/image

# Parse timeline
psort.py -o l2tcsv timeline.plaso -w timeline.csv
```

### Bulk Extractor
**Purpose:** Extract artifacts from disk images

**Installation:**
```bash
sudo apt install bulk-extractor
```

**Usage Examples:**
```bash
# Extract from disk image
bulk_extractor -o output_dir disk_image.dd

# Extract specific features
bulk_extractor -o output_dir -e email -e url disk_image.dd
```

### Foremost
**Purpose:** File carving from disk images

**Installation:**
```bash
sudo apt install foremost
```

**Usage Examples:**
```bash
# Carve all file types
foremost -i disk_image.dd -o output_dir

# Carve specific types
foremost -t jpg,pdf,doc -i disk_image.dd -o output_dir
```

### Guymager
**Purpose:** Forensic disk imaging tool

**Installation:**
```bash
sudo apt install guymager
```

**Usage:**
- GUI-based tool for creating forensic images
- Launch with `sudo guymager`

---

## 📡 Wireless & RF (Advanced Attacks)

### Reaver
**Purpose:** WPS attacks

**Installation:**
```bash
sudo apt install reaver
```

**Usage Examples:**
```bash
# WPS attack
reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv

# Pixie dust attack
reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -K
```

### PixieWPS
**Purpose:** Offline WPS brute forcing

**Installation:**
```bash
sudo apt install pixiewps
```

**Usage Examples:**
```bash
# Used in conjunction with Reaver
pixiewps -e PKE -r PKR -s HASH1 -z HASH2 -a AUTHKEY -n E-NONCE
```

### Bettercap
**Purpose:** Modern MITM framework

**Installation:**
```bash
sudo apt install bettercap
```

**Usage Examples:**
```bash
# Start interactive mode
sudo bettercap -iface eth0

# ARP spoofing
net.probe on
set arp.spoof.targets 192.168.1.10
arp.spoof on

# DNS spoofing
set dns.spoof.domains example.com
dns.spoof on
```

### Airgeddon
**Purpose:** All-in-one Wi-Fi attack automation

**Installation:**
```bash
git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git
cd airgeddon
sudo bash airgeddon.sh
```

**Usage:**
- Menu-driven interface
- Automated WPA/WPA2 attacks
- Evil Twin attacks

---

## 🎭 Social Engineering

### King Phisher
**Purpose:** Phishing campaign framework

**Installation:**
```bash
cd /opt/king-phisher
sudo ./KingPhisherServer
```

**Usage:**
- Web-based interface for phishing campaigns
- Email template management
- Campaign tracking

### Evilginx2
**Purpose:** MFA bypass demonstrations

**Installation:**
```bash
cd /opt/evilginx2
go build
```

**Usage Examples:**
```bash
# Start Evilginx2
./evilginx2

# Create phishlet
phishlets hostname microsoft login.microsoft.com
phishlets enable microsoft
```

### Gophish
**Purpose:** Phishing framework for labs

**Installation:**
```bash
cd /opt/gophish
./gophish
```

**Usage:**
- Access web interface at https://127.0.0.1:3333
- Create campaigns, templates, and landing pages

---

## ⚙️ Utilities & Infrastructure

### tmux
**Purpose:** Terminal session management

**Installation:**
```bash
sudo apt install tmux
```

**Usage Examples:**
```bash
# Start new session
tmux new -s pentest

# Detach: Ctrl+b, d
# Attach: tmux attach -t pentest

# Split panes
# Horizontal: Ctrl+b, "
# Vertical: Ctrl+b, %
```

### Proxychains
**Purpose:** Route tools through proxies

**Installation:**
```bash
sudo apt install proxychains4
```

**Usage Examples:**
```bash
# Edit config
sudo nano /etc/proxychains4.conf

# Use with any tool
proxychains4 nmap -sT 192.168.1.10
proxychains4 curl https://example.com
```

### Chisel
**Purpose:** TCP tunneling over HTTP

**Installation:**
```bash
# Already installed via script
chisel --help
```

**Usage Examples:**
```bash
# Server mode
chisel server -p 8080 --reverse

# Client mode (reverse tunnel)
chisel client SERVER_IP:8080 R:3000:localhost:3000

# Forward tunnel
chisel client SERVER_IP:8080 8000:localhost:8000
```

### SSHuttle
**Purpose:** VPN-like pivoting over SSH

**Installation:**
```bash
sudo apt install sshuttle
```

**Usage Examples:**
```bash
# Route all traffic through SSH
sshuttle -r user@server 0.0.0.0/0

# Route specific subnet
sshuttle -r user@server 192.168.1.0/24

# Auto-detect routes
sshuttle -r user@server --auto-nets
```

---

## 🚀 Quick Start Workflow Examples

### OSINT Reconnaissance Workflow
```bash
# 1. Gather emails and subdomains
theharvester -d target.com -b all -f harvest_results.html

# 2. Advanced subdomain enumeration
amass enum -d target.com -o subdomains.txt

# 3. Check for exposed services
cat subdomains.txt | httpx -tech-detect -status-code -title

# 4. Shodan intelligence
shodan search hostname:target.com
```

### Web Application Testing Workflow
```bash
# 1. Technology fingerprinting
whatweb -a 3 https://target.com

# 2. Parameter discovery
arjun -u https://target.com/api

# 3. Vulnerability scanning
nuclei -u https://target.com -severity critical,high

# 4. XSS testing
python3 xsstrike.py -u "https://target.com/search?q=test" --crawl
```

### Active Directory Pentest Workflow
```bash
# 1. Network enumeration
crackmapexec smb 192.168.1.0/24

# 2. Credential spraying
crackmapexec smb 192.168.1.0/24 -u users.txt -p 'Password123!'

# 3. LLMNR poisoning
responder -I eth0

# 4. BloodHound data collection
./SharpHound.exe --CollectionMethod All

# 5. Import into BloodHound
bloodhound
```

---

## 📊 Tool Categories Summary

| Category | Tools Count | Key Tools |
|----------|-------------|-----------|
| OSINT | 5 | theHarvester, Amass, SpiderFoot, Maltego, Shodan |
| Web Advanced | 5 | WhatWeb, HTTPx, XSStrike, Commix, Arjun |
| Vuln Management | 3 | Faraday, Vulners, Nuclei |
| Exploitation | 4 | SearchSploit, BeEF, Empire, CrackMapExec |
| Post-Exploitation | 4 | BloodHound, Responder, Impacket, SharpHound |
| Forensics | 4 | Plaso, Bulk Extractor, Foremost, Guymager |
| Wireless | 4 | Reaver, PixieWPS, Bettercap, Airgeddon |
| Social Engineering | 3 | King Phisher, Evilginx2, Gophish |
| Utilities | 4 | tmux, Proxychains, Chisel, SSHuttle |

**Total New Tools: 36+**

---

## 🛡️ Best Practices

1. **Always get written authorization** before testing
2. **Document everything** - use tools like Faraday for collaboration
3. **Use tmux** for session persistence during long scans
4. **Proxy your traffic** when needed with Proxychains
5. **Create timelines** with Plaso for forensics work
6. **Map AD environments** with BloodHound before exploitation
7. **Test in lab environments** first (especially social engineering tools)

---

## 📚 Additional Resources

- **Exploit-DB:** https://www.exploit-db.com/
- **Nuclei Templates:** https://github.com/projectdiscovery/nuclei-templates
- **SecLists:** https://github.com/danielmiessler/SecLists
- **PayloadsAllTheThings:** https://github.com/swisskyrepo/PayloadsAllTheThings
- **HackTricks:** https://book.hacktricks.xyz/

---

**Last Updated:** January 2026
**Version:** 2.0
**Maintained by:** IBLU HexStrike Team
