# 🔥 IBLU PROFESSIONAL HACKING ASSISTANT - Quick Start Guide 🔥

## 📋 Quick Setup Instructions

### ✅ If You Already Cloned the Repository:

```bash
# Navigate to the directory
cd IBLU_KALIGPTWITHMCP

# Update to latest version
git pull origin main

# Make scripts executable
chmod +x *.sh

# Run the interactive setup
./setup.sh
```

### 🆕 If You Haven't Cloned Yet:

```bash
# Clone the repository
git clone https://github.com/iblu23/IBLU_KALIGPTWITHMCP
cd IBLU_KALIGPTWITHMCP

# Run the interactive setup
chmod +x setup.sh
./setup.sh
```

### 🚀 Manual Setup (Alternative):

#### 1. Install HexStrike Tools (Optional):
```bash
chmod +x install_hexstrike_tools.sh
sudo ./install_hexstrike_tools.sh
```

#### 2. Configure API Keys:
```bash
# Quick manual setup (recommended)
./quick_setup.sh

# OR auto-discover existing keys
./find_api_keys.sh
```

#### 3. Run the Assistant:
```bash
python3 iblu_assistant.py
```

## 🔑 Get Your API Keys:

- **Perplexity:** https://www.perplexity.ai/settings/api
- **OpenAI:** https://platform.openai.com/api-keys
- **Gemini:** https://aistudio.google.com/app/apikey
- **Mistral:** https://console.mistral.ai/api-keys

## 🎯 Main Menu Options:

1. **🧠 IBLU KALIGPT** - Multi-AI Assistant with rephrasing mode
2. **🛡️ HexStrike Tools** - Install 50+ security tools
3. **🔗 MCP Status** - Verify MCP server connection
4. **⚙️ Configuration** - Manage API keys and settings
5. **🚪 Exit** - Exit the assistant

## 💡 Common Issues:

### "Directory already exists" error:
```bash
# Just navigate to the existing directory
cd IBLU_KALIGPTWITHMCP
git pull origin main
```

### "install_hexstrike_tools.sh not found":
```bash
# Make sure you're in the correct directory
cd IBLU_KALIGPTWITHMCP
ls -la  # Should show install_hexstrike_tools.sh
```

### Python package errors:
```bash
# Install required packages
pip3 install -r requirements.txt

# OR use system packages
sudo apt install python3-colorama python3-requests
```

## 🔥 Ready to Start!

The assistant is now ready for professional cybersecurity testing!

**⚠️ AUTHORIZED USE ONLY** - For legitimate security research and authorized testing only.
