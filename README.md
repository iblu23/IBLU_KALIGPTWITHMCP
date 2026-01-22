# 🔥 IBLU Professional Hacking Assistant v2.3 - AI-Powered Cybersecurity Platform 🔥

## 🎯 **What is IBLU-KALIGPT?**

**IBLU** is a professional cybersecurity assistant that combines **AI intelligence** with **150+ automated security scans** and **50+ integrated security tools** for authorized penetration testing and security research. It's your personal hacking assistant that helps you perform security assessments efficiently with MCP (Model Context Protocol) integration.

### 🚀 **Key Features**
- 🤖 **Multi-AI Support** - Chat with OpenAI, Gemini, Mistral, and Perplexity
- 🛡️ **150+ Automated Scans** - Comprehensive security testing workflows
- 🔧 **50+ Security Tools** - Integrated professional penetration testing tools
- 💬 **Smart Chat Interface** - Persistent conversations with context awareness
- ⚡ **122 Total Commands** - From basic operations to advanced security functions
- 🎨 **Advanced Terminal UI** - Rich formatting with progress bars and visual effects
- 📊 **Real-time Status** - Monitor tools and MCP server connectivity
- 🔧 **Automated Setup** - One-click installation of all security tools
- 🗂️ **Menu System** - Interactive dropdown-style command browser
- 📈 **Usage Statistics** - Track command patterns and favorites

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
| **Perplexity** | https://www.perplexity.ai/settings/api | Pay-as-you-go |

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
1. **🧠 IBLU KALIGPT** - Multi-AI chat with security guidance (OpenAI, Gemini, Mistral, HuggingFace)
2. **🛡️ HexStrike Tools** - Install and manage 90+ security tools
3. **⚙️ Configuration** - Manage API keys and system settings
4. **📦 Install Local Models** - Install uncensored AI models (Dolphin, Gemma, WhiteRabbitNeo)
5. **📊 Check API Keys Status** - View current API configuration
6. **🔄 Reload from Environment** - Load API keys from environment
7. **✏️ Manual Key Entry** - Enter API keys manually
8. **🔗 Test API Connections** - Test all configured endpoints
9. **� LIST Cloud Models** - Show cloud API models
10. **🗑️ DELETE Local LLaMA Models** - Remove local Llama models
11. **🚪 EXIT** - Leave the program

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
- `/huggingface` - Switch to Hugging Face models

#### **Local Model Management**
- `/install_llama` - Install Llama models locally
- `/install_dolphin` - Install Dolphin 3.0 Llama 3.1 8B (uncensored)
- `/install_mistral` - Install Mistral Dolphin model locally
- `/install_gemma` - Install Gemma-2-9B-IT-Abliterated (uncensored)
- `/install_whiterabbit` - Install WhiteRabbitNeo Llama-3 8B v2.0 (uncensored)
- `/llama_models` - List and manage available Llama models
- `/delete_llama` - Delete a local Llama model
- `/install_models` - Install all local models

#### **HexStrike Tool Commands** (90+ tools)
- `/nmap` - Network discovery and security auditing
- `/metasploit` - Penetration testing framework
- `/burpsuite` - Web application security testing
- `/sqlmap` - SQL injection testing tool
- `/nikto` - Web server scanner
- `/gobuster` - Directory/file busting tool
- `/hydra` - Online password cracking tool
- `/john` - John the Ripper password cracker
- `/wireshark` - Network protocol analyzer
- `/aircrack-ng` - Wireless security suite
- `[80+ more tools - use Tab completion to explore]`

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
├── 🐍 iblu_assistant.py          # Main assistant application (532KB)
├── 📦 requirements.txt           # Python dependencies
├── ⚙️ config.json                # Configuration (API keys - gitignored)
├── 🔧 setup.sh                   # Interactive setup script
├── 🛡️ install_hexstrike_tools.sh # Security tools installer
├── 🔑 quick_setup.sh             # Quick API key setup
├── 🔍 find_api_keys.sh           # Auto-discover API keys
├── 🔧 setup_api_keys.sh          # Manual API key configuration
├── 🗂️ menu_options/              # Modular menu system
│   ├── 📋 menu_config.json       # Menu configuration
│   ├── 🧭 navigator.py           # Menu navigation logic
│   └── 📂 [6 subdirectories]     # Feature-specific modules
├── 🎨 visual_effects/            # UI enhancement modules
│   ├── 🌈 hybrid_progress.py     # Advanced progress bars
│   ├── 🎨 stunning_progress.py   # Visual effects
│   └── 📺 [multiple UI modules]  # Terminal interface components
├── 🔧 utility_scripts/           # Helper scripts
│   ├── 🔑 api_key_protection.py # API key security
│   ├── 🛡️ secure_config_loader.py # Secure configuration
│   └── 🧹 cleanup_system.py      # System maintenance
├── 📚 documentation/            # Comprehensive guides
│   ├── 📖 QUICKSTART.md         # Quick start guide
│   ├── 🛠️ TOOLS_ADDED_SUMMARY.md # Tools documentation
│   └── 📋 [multiple guides]     # Detailed documentation
└── 📦 archive_files/            # Archived versions and guides
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
pip3 install colorama requests prompt_toolkit rich alive-progress textual streamlit

# Optional AI providers (install as needed)
pip3 install openai google-generativeai mistralai
```

### **Core Python Modules Used**
- **asyncio** - Asynchronous operations
- **pathlib** - Modern file path handling
- **dataclasses** - Structured data management
- **enum** - Type-safe enumerations
- **threading** - Multi-threading support
- **json** - Configuration and data storage
- **subprocess** - Tool execution and management

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
- 🌈 **Hybrid progress bars** with stunning visual effects
- 🖼️ **Advanced TUI framework** with interactive elements
- 📺 **Multiple interface modes** - Terminal, Web (Streamlit), and Textual

### **Smart Features**
- 🧠 **Intelligent suggestions** that learn from your input
- 📝 **Command history** with arrow key navigation
- 🔍 **Context-aware responses** based on conversation
- 💾 **Persistent storage** of preferences and history
- 🎯 **Tab completion** for all 122 commands
- 📊 **Usage statistics** and command pattern tracking
- 🔧 **Modular menu system** with dropdown navigation
- 🤖 **AI-powered autocomplete** and suggestions

---

## 🔗 **Integration & Architecture**

### **MCP (Model Context Protocol) Integration**
- **150+ automated security scans** through MCP servers
- **Real-time MCP server status** monitoring
- **Automated workflow execution** with MCP tools
- **Professional security testing** automation

### **Security Tools Integration**
- **90+ HexStrike tools** integrated and managed
- **Real-time tool status** monitoring and health checks
- **Automated installation** and configuration management
- **Professional workflow** optimization with tool chaining
- **Categorized tool organization** (Recon, Web, Network, Forensics, etc.)

### **Multi-AI Support**
- **Provider switching** without losing context
- **Fallback mechanisms** for reliability
- **Cost optimization** with smart provider selection
- **Response quality** monitoring and comparison
- **4 AI providers** supported (OpenAI, Gemini, Mistral, HuggingFace)

### **Local AI Model Management**
- **Uncensored models** for offline use (Dolphin, Gemma, WhiteRabbitNeo)
- **Local installation** with automatic configuration
- **Model management** with install/delete capabilities
- **Privacy-focused** local processing without API calls

---

## ⚡ **Performance**

| Metric | Value |
|--------|-------|
| **Startup Time** | < 3 seconds |
| **Memory Usage** | ~60MB |
| **CPU Usage** | < 5% idle |
| **Tools Available** | 90+ HexStrike tools |
| **AI Providers** | 4 (OpenAI, Gemini, Mistral, HuggingFace) |
| **Local Models** | 5+ uncensored models |
| **Response Time** | < 2 seconds |
| **Main File Size** | 532KB (iblu_assistant.py) |
| **Python Modules** | 15+ UI/Utility modules |
| **Menu Options** | 11 main menu choices |
| **Tool Categories** | 6+ (Recon, Web, Network, Forensics, etc.) |

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
- 🔒 **Local processing** - No data sent to external servers (except AI APIs)
- 🔑 **User-controlled API keys** - You manage access
- 🚫 **No tracking** - No usage analytics or telemetry
- 💾 **Local storage** - All data stored locally
- 🔐 **API key protection** - Secure configuration management
- 🛡️ **Config obfuscation** - Protected sensitive data storage

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

#### **"MCP server not responding"**
```bash
# Check MCP server status
/mcp_status

# Restart MCP server
python3 hexstrike_mcp_server.py
```

#### **"Command not found" errors**
```bash
# Check available commands
/help

# Use numbered commands (1-100)
/1  # Shows help
/11 # Nmap scan example
```

### **Getting Help**
- Type `/help` in the assistant for command reference
- Check the [Issues](https://github.com/iblu23/IBLU_KALIGPTWITHMCP/issues) page
- Review the [Wiki](https://github.com/iblu23/IBLU_KALIGPTWITHMCP/wiki) for detailed guides
- Check `QUICKSTART.md` for step-by-step setup
- Review `TOOLS_ADDED_SUMMARY.md` for complete tool list

---

## 🚀 **Advanced Usage**

### **Custom Configuration**
```bash
# Edit configuration
cp config.json.example config.json
nano config.json

# Secure configuration setup
./setup_api_keys.sh

# Test API connections
/test_api_keys
```

### **MCP Server Management**
```bash
# Start MCP server
python3 hexstrike_mcp_server.py

# Check status
/mcp_status

# Restart MCP services
/restart_mcp
```

### **Multiple Interface Modes**
```bash
# Terminal interface (default)
python3 iblu_assistant.py

# Web interface (Streamlit)
./run_streamlit.sh

# Textual TUI interface
python3 textual_progress.py
```

### **Batch Operations**
```bash
# Install all tools at once
sudo ./install_hexstrike_tools.sh

# Update all tools
git pull origin main
sudo ./install_hexstrike_tools.sh

# Test all interfaces
./test_all_interfaces.sh
```

## 📊 **Version History & Updates**

### **Current Version: v2.3**
- ✅ **90+ HexStrike Tools** - Comprehensive security tool integration
- ✅ **11 Main Menu Options** - Complete feature access
- ✅ **4 AI Providers** - OpenAI, Gemini, Mistral, HuggingFace
- ✅ **Advanced UI** - Hybrid progress bars and visual effects
- ✅ **Local Model Support** - 5+ uncensored AI models
- ✅ **Visual Menu System** - Professional terminal interface
- ✅ **API Key Management** - Secure configuration system

### **Recent Changes**
- 🔧 Fixed configuration status display errors
- 🔧 Enhanced uncensored model detection
- 🔧 Complete API key structure migration
- 🔧 Improved menu system and method handling

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

🔥 **IBLU Professional Hacking Assistant v2.3**  
🚀 *AI-Powered • 90+ Tools • 4 AI Providers • Professional Interface*  
🛡️ *Authorized cybersecurity testing platform only*

💡 **Type '/' and Tab to explore all 90+ HexStrike tools!**  
🔒 **Professional security testing for authorized use only**  
🧠 **Multi-AI support with local model management**
