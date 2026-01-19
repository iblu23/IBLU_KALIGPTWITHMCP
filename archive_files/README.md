# 🔥 KaliGPT MCP Enhanced - 150 Automated Scans 🔥

**KaliGPT MCP Enhanced** is an advanced cybersecurity automation platform designed for Kali Linux, providing 150+ automated security scans through Model Context Protocol (MCP) integration. It combines intelligent AI assistance with comprehensive penetration testing workflows for ethical hackers and cybersecurity professionals.

## 🚀 **Latest Updates (v2.3) - 150 Automated Scans**

### 🔥 **Enhanced MCP Integration:**
- ✅ **150+ Automated Scans** - Comprehensive security testing workflows
- ✅ **122 Total Commands** - From ~30 to 122 commands
- ✅ **100 Numbered Commands** - Quick access (1-100) for all security functions
- ✅ **Intelligent Typing Assistant** - Real-time command suggestions as you type
- ✅ **Interactive Menu System** - Beautiful dropdown-style command browser
- ✅ **12 Color-Coded Categories** - Perfect organization by function
- ✅ **Chat History Management** - Track conversations with timestamps
- ✅ **Usage Statistics** - Monitor command patterns and favorites

### 🎯 **Command Categories:**
1. **Basic Commands (1-10)** - Help, system info, configuration
2. **Reconnaissance (11-30)** - Port scans, subdomain enum, DNS analysis
3. **Vulnerability Scanning (31-50)** - SQLi, XSS, CSRF, XXE, SSRF, buffer overflows
4. **Exploitation & Payloads (51-70)** - Reverse shells, exploits, custom payloads
5. **Post-Exploitation (71-85)** - System enum, persistence, lateral movement
6. **Defense & Evasion (86-100)** - Anti-forensics, encryption, stealth techniques

### 🛠️ **Enhanced Features:**
- 🧠 **AI-Powered Suggestions** - Smart command completion
- 🎨 **Modern UI** - Color-coded, professional interface
- 📊 **Analytics Dashboard** - Command usage tracking
- 💬 **Conversation History** - Persistent chat management
- 🔢 **Quick Access** - Both `1` and `/1` formats work
- 📱 **Interactive Help** - Detailed command documentation

## ⚡ **Quick Start**

### **Option 1: Quick Launch (Recommended)**
```bash
./launch_iblu.sh
```
Instant launch with all features enabled.

### **Option 2: Manual Launch**
```bash
source venv/bin/activate
python iblu_assistant.py
```

### **Option 3: Enhanced Command Helper Only**
```bash
python3 -c "
from enhanced_command_helper import EnhancedCommandHelper
helper = EnhancedCommandHelper()
helper.show_interactive_menu()
"
```

## 🎯 **Core Features**

### 🤖 **Multi-AI Support**
- **OpenAI** - General purpose AI assistance
- **Google Gemini** - Google's advanced AI model
- **Mistral AI** - Efficient, fast responses

### 🔗 **Hexstrike MCP Integration**
- **Automated Security Testing** - Complete penetration testing workflows
- **Real-time Scanning** - Port analysis, service enumeration
- **Payload Generation** - Security testing payloads on demand
- **Professional Reporting** - Comprehensive assessment documentation

### 💡 **Enhanced Command Helper v2.3**
```bash
# Numbered Commands (1-100)
1              # Show complete command help
11             # Quick port scan
31             # SQL injection scan
51             # Generate reverse shell payload
86             # Cover tracks and clear logs
100            # Complete system cleanup

# Traditional Commands
/help          # Show help
/scan target   # Port scanning
/payload 51    # Generate payload
/menu          # Interactive menu
/chat          # Show chat history

# Enhanced Features
# Type "sc" → get suggestions for "scan"
# Type "1" → get suggestions for numbered commands
# Real-time intelligent suggestions
```

## 📋 **Project Structure**

```
📁 IBLU Professional Hacking Assistant v2.3/
├── 📄 README.md                   # This documentation
├── 📄 enhanced_command_helper.py # 🔥 122 commands (53KB)
├── 📄 iblu_assistant.py           # Main program (62KB)
├── 📄 mcp_server.py               # MCP server (17KB)
├── 📄 config.json                 # Configuration (2.5KB)
├── 📄 config.json.example         # Configuration template
├── 📄 requirements.txt            # Dependencies (1.5KB)
├── 📄 launch_iblu.sh              # Quick launcher (1.7KB)
├── 📄 .gitignore                  # Git ignore rules
├── 📁 logs/                       # Log files
├── 📁 pentest_reports/           # Scan results
└── 📁 venv/                       # Virtual environment
```

## 🛠️ **Installation Guide**

### **Step 1: System Requirements**
```bash
# Required: Python 3.8+
python3 --version

# Required: pip (Python package manager)
pip --version

# Optional: git (for version control)
git --version
```

### **Step 2: Clone/Download Project**
```bash
# If cloning from git repository
git clone <repository-url>
cd iblu-assistant

# Or download and extract the project files
# Navigate to the project directory
cd /path/to/iblu-assistant
```

### **Step 3: Install Dependencies**
```bash
# Install required Python packages
pip install -r requirements.txt

# Key dependencies include:
# - requests (HTTP requests)
# - colorama (Terminal colors)
# - asyncio (Async operations)
# - subprocess (System commands)
```

### **Step 4: Configuration Setup**
```bash
# Copy configuration template
cp config.json.example config.json

# Edit configuration with your API keys
nano config.json
```

**Configuration Example:**
```json
{
  "openai_keys": ["your-openai-api-key"],
  "gemini_keys": ["your-gemini-api-key"],
  "mistral_keys": ["your-mistral-api-key"],
  "hexstrike_mcp": {
    "enabled": true,
    "server_url": "http://localhost:8080"
  },
  "logging": {
    "enabled": true,
    "level": "INFO"
  }
}
```

### **Step 5: Virtual Environment (Recommended)**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies in virtual environment
pip install -r requirements.txt
```

## 🚀 **Running IBLU Assistant**

### **Method 1: Quick Launch (Recommended)**
```bash
# Make launcher executable
chmod +x launch_iblu.sh

# Launch IBLU
./launch_iblu.sh
```

### **Method 2: Manual Launch**
```bash
# Activate virtual environment
source venv/bin/activate

# Run main program
python iblu_assistant.py
```

### **Method 3: Enhanced Command Helper Only**
```bash
# Test enhanced command helper
python3 -c "
from enhanced_command_helper import EnhancedCommandHelper
helper = EnhancedCommandHelper()
helper.show_interactive_menu()
"
```

## 📖 **Usage Guide**

### **First Time Setup**
```bash
# 1. Launch IBLU
./launch_iblu.sh

# 2. Check system status
/status

# 3. Test command helper
/help

# 4. Try numbered commands
1              # Show all commands
11             # Quick port scan
51             # Generate payload
```

### **Basic Commands**
```bash
/help          # Show help
/clear          # Clear screen
/exit           # Exit program
/status         # System status
/history        # Command history
/menu           # Interactive menu
```

### **AI Provider Switching**
```bash
/openai         # Switch to OpenAI
/gemini         # Switch to Gemini
/mistral        # Switch to Mistral
/providers      # List available providers
```

### **Security Testing**
```bash
# Scanning
/scan target.com port        # Port scan
/scan target.com subdomain   # Subdomain enumeration
/scan target.com directory   # Directory enumeration

# Payloads
/payload reverse_shell 192.168.1.100 4444
/payload bind_shell
/payload custom

# Automated testing
/autopentest target.com
```

### **Numbered Commands (1-100)**
```bash
# Basic (1-10)
1    # Complete command help
2    # System information
3    # Network connectivity test
4    # List available tools
5    # Show configuration

# Reconnaissance (11-30)
11   # Quick port scan
12   # Full port scan
13   # Service version detection
16   # Subdomain enumeration
18   # WHOIS information
20   # SSL/TLS analysis

# Vulnerability Scanning (31-50)
31   # SQL injection scan
32   # XSS detection
33   # Directory traversal
35   # Authentication bypass
37   # Command injection
39   # SSRF detection

# Exploitation (51-70)
51   # Generate reverse shell
52   # Generate bind shell
53   # Generate meterpreter
54   # Generate custom payload
56   # SQL injection payload
57   # XSS payload

# Post-Exploitation (71-85)
71   # System enumeration
72   # User and group enumeration
76   # File system search
77   # Password hash extraction
84   # Privilege escalation

# Defense & Evasion (86-100)
86   # Cover tracks
87   # Create stealth backdoor
89   # Encryption setup
92   # Process hiding
94   # Encrypted communication
97   # Fileless malware
100  # Complete system cleanup
```

### **Enhanced Features**
```bash
# Interactive menu
/menu

# Chat history
/chat
/chat 5        # Last 5 messages

# Command suggestions (type and press tab)
sc            # Suggests "scan"
1             # Suggests numbered commands
pay           # Suggests "payload"
```

## 🔧 **Configuration**

### **API Keys Setup**
```json
{
  "perplexity_keys": [
    "pplx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ],
  "openai_keys": [
    "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ],
  "gemini_keys": [
    "AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ],
  "mistral_keys": [
    "mistralxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ]
}
```

### **Hexstrike MCP Configuration**
```json
{
  "hexstrike_mcp": {
    "enabled": true,
    "server_url": "http://localhost:8080",
    "timeout": 30,
    "retry_attempts": 3
  }
}
```

### **Logging Configuration**
```json
{
  "logging": {
    "enabled": true,
    "level": "INFO",
    "file": "logs/iblu.log",
    "max_size": "10MB",
    "backup_count": 5
  }
}
```

## 🛡️ **Security Features**

### **Ethical Hacking Focus**
- ✅ **Authorized Testing Only** - All tools for legitimate security testing
- ✅ **Professional Methodologies** - Industry-standard penetration testing
- ✅ **Compliance Support** - NIST, OWASP, PTES frameworks
- ✅ **Documentation** - Comprehensive reporting and evidence collection

### **Advanced Capabilities**
- 🔍 **Information Gathering** - Reconnaissance and OSINT
- 🌐 **Web Security Testing** - OWASP Top 10, API security
- 🔐 **Network Security** - Protocol analysis, wireless security
- 💥 **Exploitation** - Metasploit, custom payloads
- 🎯 **Post-Exploitation** - Privilege escalation, persistence
- 🛡️ **Defense** - Anti-forensics, encryption, stealth

## 📊 **Performance Features**

### **Optimized Command System**
- ⚡ **Intelligent Caching** - Fast command suggestions
- 🧠 **Smart Prioritization** - Recently used commands first
- 📈 **Usage Analytics** - Track command patterns
- 🎯 **Context-Aware** - Suggestions based on current context

### **Resource Management**
- 💾 **Memory Efficient** - Optimized data structures
- 🔄 **Lazy Loading** - Commands loaded on demand
- 📝 **Persistent History** - Command and chat history
- 🧹 **Automatic Cleanup** - Old entries removed

## 🔍 **Troubleshooting**

### **Common Issues**

**Issue: Import Error**
```bash
# Solution: Install dependencies
pip install -r requirements.txt

# Or install specific packages
pip install requests colorama
```

**Issue: API Key Error**
```bash
# Solution: Check configuration
python3 -c "
import json
with open('config.json') as f:
    config = json.load(f)
    print('API Keys configured:', bool(config.get('perplexity_keys')))
"
```

**Issue: MCP Connection Failed**
```bash
# Solution: Check MCP server
python3 -c "
from mcp_server import start_hexstrike_mcp
print('MCP server available')
"
```

**Issue: Command Suggestions Not Working**
```bash
# Solution: Test enhanced command helper
python3 -c "
from enhanced_command_helper import EnhancedCommandHelper
helper = EnhancedCommandHelper()
suggestions = helper.get_suggestions('scan')
print('Suggestions working:', len(suggestions))
"
```

### **Debug Mode**
```bash
# Enable debug logging
export IBLU_DEBUG=1
python iblu_assistant.py

# Check system status
/status
```

## 📈 **Advanced Usage**

### **Custom Command Integration**
```python
from enhanced_command_helper import EnhancedCommandHelper

# Create custom helper
helper = EnhancedCommandHelper()

# Get suggestions
suggestions = helper.get_suggestions('custom_query')

# Show interactive menu
helper.show_interactive_menu()

# Access command database
commands = helper.COMMANDS
categories = helper.CATEGORIES
```

### **Batch Operations**
```bash
# Multiple scans
for target in target1.com target2.com target3.com; do
    echo "/scan $target port" | python iblu_assistant.py
done

# Payload generation
for port in 4444 5555 6666; do
    echo "/payload reverse_shell 192.168.1.100 $port" | python iblu_assistant.py
done
```

### **Integration with Other Tools**
```bash
# Combine with nmap
nmap -sS target.com | python iblu_assistant.py

# Use with metasploit
msfconsole -q -x "use auxiliary/scanner/portscan/tcp" | python iblu_assistant.py
```

## 🤝 **Contributing**

### **Development Setup**
```bash
# Clone repository
git clone <repository-url>
cd iblu-assistant

# Setup development environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
python enhanced_command_helper.py
```

### **Adding New Commands**
```python
# Add to enhanced_command_helper.py COMMANDS dictionary
"new_command": {
    "category": "custom",
    "description": "New custom command",
    "usage": "new_command <args>",
    "examples": ["new_command target"],
    "icon": "🆕"
}
```

## 📞 **Support**

### **Getting Help**
- Use `/help` command in IBLU
- Check `/status` for system information
- Review this documentation
- Check troubleshooting section

### **Community**
- GitHub Issues: Report bugs and request features
- Discussions: Share usage tips and techniques
- Wiki: Advanced guides and tutorials

## 📄 **License**

This project is provided for **educational and authorized security testing purposes only**. Users are responsible for ensuring compliance with applicable laws and regulations.

### **Authorized Use Only**
- ✅ Ethical hacking and penetration testing
- ✅ Security research and education
- ✅ Authorized system testing
- ✅ Bug bounty programs

### **Prohibited Use**
- ❌ Unauthorized system access
- ❌ Malicious activities
- ❌ Illegal hacking
- ❌ Privacy violations

---

## 🔥 **Quick Start Summary**

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API keys
cp config.json.example config.json
# Edit config.json with your API keys

# 3. Launch IBLU
./launch_iblu.sh

# 4. Start using commands
1              # Show all commands
11             # Quick port scan
/help          # Get help
/status         # Check system
```

**🎉 Welcome to IBLU Professional Hacking Assistant v2.3!**

*Enhanced with 122 commands, intelligent suggestions, and professional security testing capabilities.*
