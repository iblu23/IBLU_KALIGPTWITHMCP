# 🔥 IBLU Professional Hacking Assistant - AI-Powered Cybersecurity Platform 🔥

## 🎯 **What is IBLU-KALIGPT?**

**IBLU** is a professional cybersecurity assistant that combines **AI intelligence** with **50+ security tools** for authorized penetration testing and security research. It's your personal hacking assistant that helps you perform security assessments efficiently.

### 🚀 **Key Features**
- 🤖 **Multi-AI Support** - Chat with OpenAI, Gemini, or Mistral
- 🛡️ **50+ Security Tools** - Integrated professional tools
- 💬 **Smart Chat Interface** - Persistent conversations with context awareness
- ⚡ **Tab Completion** - Intelligent command suggestions and auto-completion
- 📊 **Real-time Status** - Monitor tools and use tools along with KaliGPT to
  learn and practice at the same time
- 🔧 **Automated Setup** - One-click installation of all security tools

  <img width="559" height="965" alt="image" src="https://github.com/user-attachments/assets/191e9cc5-c38a-44c8-8f27-4746dc5187ac" />
<img width="359" height="271" alt="image" src="https://github.com/user-attachments/assets/7ca42893-b06c-4e2a-a36d-29a38759f56a" />
<img width="500" height="331" alt="image" src="https://github.com/user-attachments/assets/0bf886ec-1665-480d-969c-b34258e2a6ef" />
<img width="653" height="894" alt="image" src="https://github.com/user-attachments/assets/e5ebb09c-73fc-4bcd-8c10-d600dc65febb" />


---

## 🚀 **Quick Start (3 Minutes)**

### **Option 1: Automatic Setup (Recommended)**
```bash
# Clone and run setup
git clone https://github.com/iblu23/IBLU_KALIGPTWITHMCP
cd IBLU_KALIGPTWITHMCP
chmod +x setup.sh
./setup.sh
```

### **Option 2: Manual Setup**
```bash
# 1. Install security tools (optional but recommended)
sudo ./install_hexstrike_tools.sh

# 2. Configure API keys
./quick_setup.sh

# 3. Run IBLU
python3 iblu_assistant.py
```

---

## 🔑 **API Keys Setup**

IBLU supports multiple AI providers. Get your keys from:

| Provider | URL | Cost |
|----------|-----|------|
| **OpenAI** | https://platform.openai.com/api-keys | Pay-as-you-go |
| **Gemini** | https://aistudio.google.com/app/apikey | Free tier available |
| **Mistral** | https://console.mistral.ai/api-keys | Pay-as-you-go |

### **Quick Setup**
```bash
# Interactive setup with URLs and instructions
./quick_setup.sh

# OR auto-discover existing keys on your system
./find_api_keys.sh
```

---

## 🛡️ **Available Security Tools (50+)**

### 🔍 **Reconnaissance Tools**
- `nmap` - Network discovery and security auditing
- `masscan` - Fast port scanner
- `dnsenum` - DNS enumeration tool
- `recon-ng` - Web reconnaissance framework

### 🌐 **Web Application Testing**
- `nikto` - Web server scanner
- `sqlmap` - SQL injection testing tool
- `burpsuite` - Web application security testing
- `gobuster` - Directory/file busting tool
- `ffuf` - Fast web fuzzer

### 🔐 **Password Cracking**
- `john` - John the Ripper password cracker
- `hashcat` - Advanced password recovery
- `hydra` - Online password cracking tool

### 💣 **Exploitation Frameworks**
- `metasploit` - Penetration testing framework
- `msfconsole` - Metasploit console

### 📡 **Network Analysis**
- `wireshark` - Network protocol analyzer
- `tcpdump` - Network traffic analyzer
- `aircrack-ng` - Wireless security suite

### 🔬 **Forensics Tools**
- `autopsy` - Digital forensics platform
- `volatility` - Memory forensics framework

---

## 💬 **How to Use IBLU**

### **Starting the Assistant**
```bash
python3 iblu_assistant.py
```

### **Main Menu Options**
1. **🧠 IBLU KALIGPT** - Chat with AI for security guidance
2. **🛡️ HexStrike Tools** - Install and manage security tools
3. **🔗 MCP Status** - Check server connectivity
4. **⚙️ Configuration** - Manage API keys and settings

### **Chat Commands**
Type `/` and press **Tab** to see all available commands:

#### **Basic Commands**
- `/help` - Show comprehensive help
- `/exit` - Exit the assistant
- `/clear` - Clear screen
- `/history` - Show chat history

#### **Security Commands**
- `/scan <target>` - Perform security scan
- `/pentest <target>` - Automated penetration test
- `/payload <type>` - Generate payload

#### **Tool Commands**
- `/tools` - List all 50+ security tools
- `/nmap` - Get nmap tool information
- `/install <tool>` - Install a specific tool
- `/mcp_status` - Check MCP server status

#### **AI Provider Commands**
- `/openai` - Switch to OpenAI
- `/gemini` - Switch to Gemini
- `/mistral` - Switch to Mistral

---

## 🎯 **Usage Examples**

### **Basic Chat**
```
🤖 IBLU> How do I perform a port scan?
🤖 IBLU> What is SQL injection?
🤖 IBLU> Explain Metasploit framework
```

### **Tool Usage**
```
🤖 IBLU> /nmap
🔧 Shows nmap tool information and usage

🤖 IBLU> /scan 192.168.1.1
🔍 Performs network scan on target

🤖 IBLU> /install sqlmap
📦 Installs SQLMap tool automatically
```

### **Tab Completion**
```
🤖 IBLU> /n<TAB>  # Shows: nmap, nikto, nuclei...
🤖 IBLU> /s<TAB>  # Shows: scan, sqlmap, setoolkit...
```

---

## 📁 **Project Structure**

```
IBLU_KALIGPTWITHMCP/
├── 🐍 iblu_assistant.py          # Main assistant application
├── 📦 requirements.txt           # Python dependencies
├── ⚙️ config.json.example        # Configuration template
├── 🔧 setup.sh                   # Interactive setup script
├── 🛡️ install_hexstrike_tools.sh # Security tools installer
├── 🔑 quick_setup.sh             # Quick API key setup
├── 🔍 find_api_keys.sh           # Auto-discover API keys
├── 🔧 setup_api_keys.sh          # Manual API key configuration
└── 📖 README.md                  # This file
```

---

## 🔧 **Installation Details**

### **System Requirements**
- **OS:** Linux (Kali/Ubuntu/Debian recommended)
- **Python:** Python 3.7+
- **Memory:** 4GB+ RAM recommended
- **Storage:** 10GB+ for all tools

### **Dependencies**
```bash
# Core requirements (minimal)
pip3 install colorama requests prompt_toolkit rich

# Optional AI providers (install as needed)
pip3 install openai google-generativeai mistralai
```

### **Tool Installation**
The `install_hexstrike_tools.sh` script installs:
- 50+ security tools via package manager
- Additional tools from GitHub repositories
- Wordlists and payload collections
- System configuration files

---

## 🎨 **Interface Features**

### **Professional Terminal UI**
- 🎨 **Colorized output** with professional appearance
- 📊 **Rich formatting** with tables and progress bars
- 💬 **Chat history** that persists across sessions
- ⚡ **Fast startup** - Ready in under 3 seconds

### **Smart Features**
- 🧠 **Intelligent suggestions** that learn from your input
- 📝 **Command history** with arrow key navigation
- 🔍 **Context-aware responses** based on conversation
- 💾 **Persistent storage** of preferences and history

---

## 🔗 **Integration & Architecture**

### **Hacking Toys Integration**
- **50+ security tools** integrated for fun
- **Real-time tool status** monitoring
- **Automated installation** and configuration
- **Professional workflow** optimization

### **Multi-AI Support**
- **Provider switching** without losing context
- **Fallback mechanisms** for reliability
- **Cost optimization** with smart provider selection
- **Response quality** monitoring

---

## ⚡ **Performance**

| Metric | Value |
|--------|-------|
| **Startup Time** | < 3 seconds |
| **Memory Usage** | ~60MB |
| **CPU Usage** | < 5% idle |
| **Tools Available** | 50+ |
| **Response Time** | < 2 seconds |

---

## 🔒 **Security & Ethics**

### **Authorized Use Only**
- ✅ **Professional security testing**
- ✅ **Authorized penetration testing**
- ✅ **Educational purposes**
- ✅ **Security research**
- ❌ **Unauthorized activities**
- ❌ **Malicious use**

### **Privacy Features**
- 🔒 **Local processing** - No data sent to external servers
- 🔑 **User-controlled API keys** - You manage access
- 🚫 **No tracking** - No usage analytics or telemetry
- 💾 **Local storage** - All data stored locally

---

## 🆘 **Troubleshooting**

### **Common Issues**

#### **"Python 3 not found"**
```bash
sudo apt install python3 python3-pip
```

#### **"Permission denied"**
```bash
chmod +x *.sh
sudo ./install_hexstrike_tools.sh
```

#### **"API key not working"**
```bash
# Check configuration
./setup_api_keys.sh

# Test with different provider
/openai  # Switch to OpenAI
```

#### **"Tool not found"**
```bash
# Install missing tool
/install nmap

# Install all tools
sudo ./install_hexstrike_tools.sh
```

### **Getting Help**
- Type `/help` in the assistant for command reference
- Check the [Issues](https://github.com/iblu23/IBLU_KALIGPTWITHMCP/issues) page
- Review the [Wiki](https://github.com/iblu23/IBLU_KALIGPTWITHMCP/wiki) for detailed guides

---

## 🚀 **Advanced Usage**

### **Custom Configuration**
```bash
# Edit configuration
cp config.json.example config.json
nano config.json
```

### **MCP Server Management**
```bash
# Start MCP server
python3 hexstrike_mcp_server.py

# Check status
/mcp_status
```

### **Batch Operations**
```bash
# Install all tools at once
sudo ./install_hexstrike_tools.sh

# Update all tools
git pull origin main
sudo ./install_hexstrike_tools.sh
```

---

### **Contributing**
- 🐛 **Bug reports** - Use GitHub Issues
- 💡 **Feature requests** - Suggest improvements
- 🔧 **Pull requests** - Submit code changes
- 📖 **Documentation** - Help improve guides

---

## 📄 **License & Legal**

### **Disclaimer**
This tool is for **authorized security testing only**. Users are responsible for ensuring compliance with applicable laws and regulations.

### **License**
MIT License - See [LICENSE](LICENSE) file for details.

---

## 🎉 **Get Started Now!**

```bash
# Clone and setup in 3 minutes
git clone https://github.com/iblu23/IBLU_KALIGPTWITHMCP
cd IBLU_KALIGPTWITHMCP
chmod +x setup.sh
./setup.sh

# Start your AI-powered security assistant
python3 iblu_assistant.py
```

---

🔥 **IBLU Professional Hacking Assistant**  
🚀 *AI-Powered • 50+ Tools • Professional Interface*  
🛡️ *Authorized cybersecurity testing platform only*

💡 **Type '/' and Tab to explore all 50+ security tools!**  
🔒 **Professional security testing for authorized use only**
