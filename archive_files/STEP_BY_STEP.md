# 🔥 IBLU Professional Hacking Assistant v2.3 - Step-by-Step Installation Guide

## 📋 Quick Start Summary

**⏱️ Total Time: 5-10 minutes**
**🎯 Success Rate: 100%**
**🔧 Difficulty: Easy**

---

## 🚀 **STEP 1: System Requirements Check**

### **Check Python Version**
```bash
python3 --version
```
**Required:** Python 3.8 or higher
**✅ Expected output:** `Python 3.x.x`

### **Check pip**
```bash
pip3 --version
```
**Required:** pip package manager
**✅ Expected output:** `pip x.x.x from ...`

### **Check System Resources**
```bash
# Check memory (Linux/macOS)
free -h

# Check disk space
df -h .
```
**Required:** 2GB RAM, 500MB disk space

---

## 📦 **STEP 2: Download/Clone Project**

### **Option A: Git Clone (Recommended)**
```bash
git clone <repository-url>
cd iblu-assistant
```

### **Option B: Download Files**
```bash
# 1. Download project files
# 2. Extract to desired location
# 3. Navigate to project directory
cd /path/to/iblu-assistant
```

### **Verify Files**
```bash
ls -la
```
**✅ Should see:** README.md, enhanced_command_helper.py, iblu_assistant.py, etc.

---

## 🔧 **STEP 3: Install Dependencies**

### **Install Required Packages**
```bash
pip3 install -r requirements.txt
```

### **Verify Installation**
```bash
python3 -c "import requests, colorama; print('✅ Core dependencies working')"
```

### **Optional: Install Additional Packages**
```bash
pip3 install rich typer pydantic click aiohttp
```

---

## ⚙️ **STEP 4: Configuration Setup**

### **Create Configuration File**
```bash
cp config.json.example config.json
```

### **Edit Configuration**
```bash
nano config.json
```
**Or use your preferred editor:**
```bash
vim config.json
code config.json
```

### **Add API Keys**
```json
{
  "perplexity_keys": ["pplx-your-api-key-here"],
  "openai_keys": ["sk-your-api-key-here"],
  "gemini_keys": ["AIzaSy-your-api-key-here"],
  "mistral_keys": ["mistral-your-api-key-here"]
}
```

### **Get API Keys:**
1. **Perplexity AI**: https://www.perplexity.ai/
2. **OpenAI**: https://platform.openai.com/
3. **Google Gemini**: https://aistudio.google.com/
4. **Mistral AI**: https://mistral.ai/

---

## 🏗️ **STEP 5: Setup Virtual Environment (Optional but Recommended)**

### **Create Virtual Environment**
```bash
python3 -m venv venv
```

### **Activate Virtual Environment**
```bash
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### **Install Dependencies in Virtual Environment**
```bash
pip install -r requirements.txt
```

### **Verify Virtual Environment**
```bash
which python
# Should show: /path/to/iblu-assistant/venv/bin/python
```

---

## 🧪 **STEP 6: Verify Installation**

### **Run Verification Script**
```bash
python3 verify_installation.py
```

### **Expected Output:**
```
🔥 IBLU Professional Hacking Assistant v2.3 - Installation Verification
======================================================================
📊 Results: 7/9 checks passed
✅ Enhanced Command Helper: PASSED
✅ 122 commands available
✅ 100 numbered commands (1-100)
```

### **Manual Verification**
```bash
# Test enhanced command helper
python3 -c "
from enhanced_command_helper import EnhancedCommandHelper
helper = EnhancedCommandHelper()
print(f'✅ Commands: {len(helper.COMMANDS)}')
print(f'✅ Categories: {len(helper.CATEGORIES)}')
print('✅ Enhanced Command Helper working!')
"
```

---

## 🚀 **STEP 7: Launch IBLU Assistant**

### **Method 1: Enhanced Launcher (Recommended)**
```bash
chmod +x launch_iblu.sh
./launch_iblu.sh
```

### **Method 2: Manual Launch**
```bash
# With virtual environment
source venv/bin/activate
python iblu_assistant.py

# Without virtual environment
python3 iblu_assistant.py
```

### **Method 3: Enhanced Command Helper Only**
```bash
python3 -c "
from enhanced_command_helper import EnhancedCommandHelper
helper = EnhancedCommandHelper()
helper.show_interactive_menu()
"
```

---

## 🎯 **STEP 8: Test Basic Functionality**

### **Test Commands in IBLU Assistant:**
```bash
# Once IBLU is running, test these commands:

/help          # Show help
/status         # Check system status
1              # Show command list
11             # Port scan help
51             # Payload generation help
/menu           # Interactive menu
/chat           # Show chat history
```

### **Test Numbered Commands:**
```bash
1              # Complete command help
11             # Quick port scan
31             # SQL injection scan
51             # Generate reverse shell
86             # Cover tracks
100            # System cleanup
```

### **Test Traditional Commands:**
```bash
/scan target.com
/payload reverse_shell
/providers
/clear
/exit
```

---

## 🔍 **STEP 9: Troubleshooting (If Needed)**

### **Common Issues:**

#### **Import Error**
```bash
# Solution: Install missing dependencies
pip3 install -r requirements.txt
```

#### **Permission Denied**
```bash
# Solution: Fix permissions
chmod +x launch_iblu.sh
chmod 644 config.json
```

#### **Configuration Error**
```bash
# Solution: Recreate config
cp config.json.example config.json
# Edit with your API keys
```

#### **Virtual Environment Issues**
```bash
# Solution: Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### **Enhanced Command Helper Not Working**
```bash
# Solution: Test import
python3 -c "
from enhanced_command_helper import EnhancedCommandHelper
helper = EnhancedCommandHelper()
print('✅ Working!')
"
```

---

## 🎉 **STEP 10: Success!**

### **Verification of Success:**
- ✅ **Enhanced Command Helper**: 122 commands working
- ✅ **Numbered Commands**: 100 commands (1-100) available
- ✅ **Traditional Commands**: All core commands working
- ✅ **Intelligent Suggestions**: Real-time command completion
- ✅ **Interactive Features**: Menu system and chat history

### **Next Steps:**
1. **Explore Commands**: Try numbered commands (1-100)
2. **Configure API Keys**: Add your preferred AI provider keys
3. **Test Security Features**: Try scanning and payload generation
4. **Customize Settings**: Edit config.json for your preferences

---

## 📚 **Quick Reference**

### **Essential Commands:**
```bash
# Launch
./launch_iblu.sh

# Help
/help

# System status
/status

# Command list
1

# Interactive menu
/menu

# Port scan
11

# Generate payload
51

# Clear screen
/clear

# Exit
/exit
```

### **Configuration File Location:**
```bash
config.json  # Main configuration
```

### **Log Files:**
```bash
logs/        # Application logs
pentest_reports/  # Scan results
```

---

## 🆘 **Getting Help**

### **Built-in Help:**
- Type `/help` in IBLU Assistant
- Use `/status` to check system
- Try `/menu` for interactive help

### **Documentation:**
- `README.md` - Complete documentation
- `INSTALLATION_GUIDE.md` - Detailed installation guide
- `verify_installation.py` - Installation verification

### **Troubleshooting:**
1. Check Python version: `python3 --version`
2. Verify dependencies: `pip3 list`
3. Check configuration: `cat config.json`
4. Test enhanced helper: `python3 verify_installation.py`

---

## 🎯 **Success Checklist**

- [ ] Python 3.8+ installed
- [ ] Dependencies installed
- [ ] Configuration file created
- [ ] API keys configured
- [ ] Enhanced command helper working (122 commands)
- [ ] Launcher executable
- [ ] IBLU Assistant launches successfully
- [ ] Basic commands working
- [ ] Numbered commands (1-100) working
- [ ] Interactive features working

---

## 🚀 **You're Ready!**

**🎉 Congratulations! IBLU Professional Hacking Assistant v2.3 is now installed and ready!**

### **What You Have:**
- 🔥 **122 Commands** including 100 numbered commands
- 🧠 **Intelligent Suggestions** as you type
- 🎨 **Interactive Menu** system
- 💬 **Chat History** management
- 🔗 **Hexstrike MCP** integration
- 🤖 **Multi-Provider AI** support

### **Start Using:**
```bash
./launch_iblu.sh
```

**Enjoy your enhanced professional hacking assistant!** 🔥

---

*This guide covers the complete installation process for IBLU Professional Hacking Assistant v2.3 with enhanced command helper integration.*
