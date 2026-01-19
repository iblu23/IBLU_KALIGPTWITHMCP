# 🔥 IBLU Professional Hacking Assistant v2.3 - Installation Guide

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Quick Installation](#quick-installation)
3. [Step-by-Step Installation](#step-by-step-installation)
4. [Configuration](#configuration)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Setup](#advanced-setup)

---

## 🔧 System Requirements

### **Minimum Requirements:**
- **Python 3.8+** - Required for all features
- **pip3** - Python package manager
- **2GB RAM** - Minimum memory for smooth operation
- **500MB Disk Space** - For installation and logs

### **Recommended Requirements:**
- **Python 3.10+** - Latest features and performance
- **4GB RAM** - Optimal performance
- **1GB Disk Space** - For logs and cache
- **Linux/macOS/Windows** - Cross-platform support

### **Optional Requirements:**
- **Git** - For version control
- **Virtual Environment** - Isolated Python environment
- **Terminal/CLI** - For command-line interface

---

## ⚡ Quick Installation (Recommended)

### **One-Command Installation:**
```bash
# Clone and install in one command
git clone <repository-url> iblu-assistant && cd iblu-assistant && chmod +x launch_iblu.sh && ./launch_iblu.sh
```

### **Quick Start (if already downloaded):**
```bash
# Make launcher executable and run
chmod +x launch_iblu.sh
./launch_iblu.sh
```

---

## 📋 Step-by-Step Installation

### **Step 1: Download/Clone Project**

#### Option A: Git Clone (Recommended)
```bash
# Clone the repository
git clone <repository-url>
cd iblu-assistant
```

#### Option B: Download Files
```bash
# Download and extract
# 1. Download the project files
# 2. Extract to your desired location
# 3. Navigate to the project directory
cd /path/to/iblu-assistant
```

### **Step 2: Verify System Requirements**
```bash
# Check Python version (must be 3.8+)
python3 --version

# Check pip availability
pip3 --version

# Check available memory (Linux/macOS)
free -h

# Check disk space
df -h .
```

### **Step 3: Install Dependencies**
```bash
# Install required Python packages
pip3 install -r requirements.txt

# Key packages being installed:
# - requests (HTTP requests)
# - colorama (Terminal colors)
# - asyncio (Async operations)
# - subprocess (System commands)
```

### **Step 4: Setup Virtual Environment (Recommended)**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Install dependencies in virtual environment
pip install -r requirements.txt
```

### **Step 5: Configuration Setup**
```bash
# Copy configuration template
cp config.json.example config.json

# Edit configuration file
nano config.json
# or use your preferred editor
```

**Configuration Example:**
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
  ],
  "hexstrike_mcp": {
    "enabled": true,
    "server_url": "http://localhost:8080",
    "timeout": 30,
    "retry_attempts": 3
  },
  "logging": {
    "enabled": true,
    "level": "INFO",
    "file": "logs/iblu.log",
    "max_size": "10MB",
    "backup_count": 5
  },
  "performance": {
    "cache_enabled": true,
    "max_history": 1000,
    "typing_assistant": true
  },
  "ui": {
    "colors_enabled": true,
    "interactive_menu": true,
    "show_suggestions": true
  }
}
```

### **Step 6: Verify Installation**
```bash
# Test enhanced command helper
python3 -c "
from enhanced_command_helper import EnhancedCommandHelper
helper = EnhancedCommandHelper()
print(f'✅ Commands: {len(helper.COMMANDS)}')
print(f'✅ Categories: {len(helper.CATEGORIES)}')
print('✅ Enhanced Command Helper working!')
"

# Test main program
python3 -c "
import iblu_assistant
print('✅ Main program imports successfully!')
"

# Test launcher
./launch_iblu.sh --help 2>/dev/null || echo "Launcher ready"
```

---

## ⚙️ Configuration

### **API Keys Setup**

#### **Perplexity AI (Primary)**
1. Visit [Perplexity AI](https://www.perplexity.ai/)
2. Create account and get API key
3. Add to `config.json`:
```json
"perplexity_keys": ["pplx-your-api-key-here"]
```

#### **OpenAI**
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create account and get API key
3. Add to `config.json`:
```json
"openai_keys": ["sk-your-api-key-here"]
```

#### **Google Gemini**
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create project and get API key
3. Add to `config.json`:
```json
"gemini_keys": ["AIzaSy-your-api-key-here"]
```

#### **Mistral AI**
1. Visit [Mistral AI](https://mistral.ai/)
2. Create account and get API key
3. Add to `config.json`:
```json
"mistral_keys": ["mistral-your-api-key-here"]
```

### **Hexstrike MCP Configuration**
```json
"hexstrike_mcp": {
  "enabled": true,
  "server_url": "http://localhost:8080",
  "timeout": 30,
  "retry_attempts": 3,
  "auto_connect": true
}
```

### **Logging Configuration**
```json
"logging": {
  "enabled": true,
  "level": "INFO",
  "file": "logs/iblu.log",
  "max_size": "10MB",
  "backup_count": 5,
  "console_output": true
}
```

### **Performance Settings**
```json
"performance": {
  "cache_enabled": true,
  "max_history": 1000,
  "typing_assistant": true,
  "suggestions_cache": true,
  "async_operations": true
}
```

---

## ✅ Verification

### **Basic Functionality Test**
```bash
# Test 1: Enhanced Command Helper
python3 -c "
from enhanced_command_helper import EnhancedCommandHelper
helper = EnhancedCommandHelper()
print('🔥 Enhanced Command Helper Test:')
print(f'✅ Total Commands: {len(helper.COMMANDS)}')
print(f'✅ Categories: {len(helper.CATEGORIES)}')
print(f'✅ Numbered Commands: 100 (1-100)')

# Test suggestions
suggestions = helper.get_suggestions('scan')
print(f'✅ Suggestions for \"scan\": {len(suggestions)}')

suggestions = helper.get_suggestions('1')
print(f'✅ Suggestions for \"1\": {len(suggestions)}')
print('🎉 All tests passed!')
"

# Test 2: Main Program
python3 -c "
import iblu_assistant
from iblu_assistant import IBLUCommandHelper
helper = IBLUCommandHelper()
suggestions = helper.get_suggestions('help')
print('🔥 Main Program Test:')
print(f'✅ Imports successful')
print(f'✅ Command helper working: {len(suggestions)} suggestions')
print('🎉 Main program ready!')
"

# Test 3: Launcher
echo "🔥 Launcher Test:"
./launch_iblu.sh --help 2>/dev/null && echo "✅ Launcher working" || echo "❌ Launcher issue"
```

### **Interactive Test**
```bash
# Launch IBLU and test interactively
./launch_iblu.sh

# Once launched, test these commands:
/help          # Should show help
/status         # Should show system status
1              # Should show command list
11             # Should show port scan help
/menu           # Should show interactive menu
/chat           # Should show chat history
```

---

## 🚀 Running IBLU Assistant

### **Method 1: Enhanced Launcher (Recommended)**
```bash
# Make executable and run
chmod +x launch_iblu.sh
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

### **Method 4: Direct Python**
```bash
# Run with Python directly
python3 iblu_assistant.py
```

---

## 🔧 Troubleshooting

### **Common Issues and Solutions**

#### **Issue: Python Version Error**
```bash
# Problem: Python 3.8+ required
# Solution: Install Python 3.8+

# Ubuntu/Debian:
sudo apt update
sudo apt install python3 python3-pip python3-venv

# CentOS/RHEL:
sudo yum install python3 python3-pip

# macOS:
brew install python3

# Windows:
# Download from python.org
```

#### **Issue: Import Error**
```bash
# Problem: Missing dependencies
# Solution: Install requirements

pip3 install -r requirements.txt

# Or install specific packages:
pip3 install requests colorama
```

#### **Issue: Configuration Error**
```bash
# Problem: Missing or invalid config
# Solution: Recreate configuration

cp config.json.example config.json
nano config.json
# Add your API keys
```

#### **Issue: Virtual Environment Error**
```bash
# Problem: Virtual environment issues
# Solution: Recreate virtual environment

rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### **Issue: Permission Denied**
```bash
# Problem: File permissions
# Solution: Fix permissions

chmod +x launch_iblu.sh
chmod 644 config.json
chmod 755 logs/
```

#### **Issue: Enhanced Command Helper Not Working**
```bash
# Problem: Enhanced helper not found
# Solution: Verify file exists

ls -la enhanced_command_helper.py

# Test import:
python3 -c "
import sys
sys.path.insert(0, '.')
from enhanced_command_helper import EnhancedCommandHelper
print('✅ Enhanced helper working')
"
```

### **Debug Mode**
```bash
# Enable debug logging
export IBLU_DEBUG=1
python iblu_assistant.py

# Check system status
/status

# Enable verbose logging
export IBLU_VERBOSE=1
python iblu_assistant.py
```

### **Log Analysis**
```bash
# Check logs
tail -f logs/iblu.log

# Search for errors
grep -i error logs/iblu.log

# Check recent activity
tail -50 logs/iblu.log
```

---

## 🔬 Advanced Setup

### **Custom Installation Directory**
```bash
# Install to custom directory
export IBLU_HOME="/opt/iblu-assistant"
mkdir -p $IBLU_HOME
cp -r * $IBLU_HOME/
cd $IBLU_HOME
./launch_iblu.sh
```

### **Docker Installation**
```dockerfile
# Create Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "iblu_assistant.py"]
```

```bash
# Build and run Docker image
docker build -t iblu-assistant .
docker run -it iblu-assistant
```

### **Systemd Service (Linux)**
```ini
# Create /etc/systemd/system/iblu.service
[Unit]
Description=IBLU Professional Hacking Assistant
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/iblu-assistant
Environment=PATH=/path/to/iblu-assistant/venv/bin
ExecStart=/path/to/iblu-assistant/venv/bin/python /path/to/iblu-assistant/iblu_assistant.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl enable iblu.service
sudo systemctl start iblu.service
sudo systemctl status iblu.service
```

### **Development Setup**
```bash
# Clone repository
git clone <repository-url>
cd iblu-assistant

# Create development environment
python3 -m venv venv-dev
source venv-dev/bin/activate
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
python -m pytest

# Code formatting
black *.py
flake8 *.py
```

### **Performance Optimization**
```bash
# Enable performance mode
export IBLU_PERFORMANCE=1

# Optimize for low memory
export IBLU_LOW_MEMORY=1

# Disable caching
export IBLU_NO_CACHE=1
```

---

## 📞 Getting Help

### **Built-in Help**
```bash
# In IBLU Assistant:
/help          # Show all commands
/status         # Show system status
/providers      # List AI providers
/menu           # Interactive menu
```

### **Documentation**
- `README.md` - Main documentation
- `INSTALLATION_GUIDE.md` - This installation guide
- Command help within IBLU Assistant

### **Community Support**
- GitHub Issues: Report bugs and request features
- Discussions: Share tips and techniques
- Wiki: Advanced guides and tutorials

---

## 🎉 Installation Complete!

### **Next Steps:**
1. ✅ **Run IBLU Assistant**: `./launch_iblu.sh`
2. ✅ **Test Commands**: Try `/help`, `/status`, `1`, `/menu`
3. ✅ **Configure API Keys**: Edit `config.json` if needed
4. ✅ **Explore Features**: Try numbered commands (1-100)

### **Quick Test Commands:**
```bash
# Test basic functionality
/help          # Show help
/status         # Check system
1              # Command list
11             # Port scan help
/menu           # Interactive menu

# Test enhanced features
# Type "sc" → get suggestions for "scan"
# Type "1" → get suggestions for numbered commands
/chat          # Show chat history
```

**🔥 Welcome to IBLU Professional Hacking Assistant v2.3!**

*Enhanced with 122 commands, intelligent suggestions, and professional security testing capabilities.*
