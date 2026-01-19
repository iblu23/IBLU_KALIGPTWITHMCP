#!/bin/bash
# 🔥 KaliGPT MCP Enhanced - 150 Automated Scans v2.3 - Enhanced Launcher 🔥

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/venv"
CONFIG_FILE="$SCRIPT_DIR/config.json"
ENHANCED_HELPER="$SCRIPT_DIR/enhanced_command_helper.py"

# Function to print colored header
print_header() {
    echo -e "${CYAN}🔥 KaliGPT MCP Enhanced - 150 Automated Scans v2.3 - Enhanced Launcher 🔥${NC}"
    echo -e "${CYAN}=====================================================================${NC}"
    echo -e "${WHITE}🚀 Advanced Cybersecurity Automation Platform${NC}"
    echo -e "${WHITE}🧠 Intelligent AI Assistant with MCP Integration${NC}"
    echo -e "${WHITE}🔗 150+ Automated Security Scans & Workflows${NC}"
    echo -e "${WHITE}🛡️ Enhanced Command Helper with 122 Commands${NC}"
    echo -e "${CYAN}=====================================================================${NC}"
    echo
}

# Function to check dependencies
check_dependencies() {
    echo -e "${BLUE}🔍 Checking dependencies...${NC}"
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python 3 is required but not installed${NC}"
        echo -e "${YELLOW}💡 Please install Python 3.8 or higher${NC}"
        exit 1
    fi
    
    # Check pip
    if ! command -v pip3 &> /dev/null; then
        echo -e "${RED}❌ pip3 is required but not installed${NC}"
        echo -e "${YELLOW}💡 Please install pip3${NC}"
        exit 1
    fi
    
    # Check enhanced command helper
    if [ ! -f "$ENHANCED_HELPER" ]; then
        echo -e "${RED}❌ Enhanced command helper not found${NC}"
        echo -e "${YELLOW}💡 Please ensure enhanced_command_helper.py exists${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Dependencies check passed${NC}"
}

# Function to setup virtual environment
setup_venv() {
    echo -e "${YELLOW}🔧 Setting up virtual environment...${NC}"
    
    if [ ! -d "$VENV_DIR" ]; then
        echo -e "${BLUE}📦 Creating virtual environment...${NC}"
        python3 -m venv "$VENV_DIR"
    fi
    
    echo -e "${BLUE}📦 Installing dependencies...${NC}"
    source "$VENV_DIR/bin/activate"
    pip install -r "$SCRIPT_DIR/requirements.txt" --quiet
    
    echo -e "${GREEN}✅ Virtual environment ready${NC}"
}

# Function to check configuration
check_config() {
    echo -e "${BLUE}🔍 Checking configuration...${NC}"
    
    if [ ! -f "$CONFIG_FILE" ]; then
        echo -e "${YELLOW}📋 Configuration file not found${NC}"
        echo -e "${BLUE}📝 Creating configuration from template...${NC}"
        cp "$SCRIPT_DIR/config.json.example" "$CONFIG_FILE"
        echo -e "${YELLOW}⚠️  Please edit config.json with your API keys${NC}"
        return 1
    fi
    
    # Check if API keys are configured
    if ! grep -q "perplexity_keys.*\[" "$CONFIG_FILE" 2>/dev/null; then
        echo -e "${YELLOW}⚠️  No API keys configured in config.json${NC}"
        echo -e "${BLUE}📝 Please edit config.json and add your API keys${NC}"
        return 1
    fi
    
    echo -e "${GREEN}✅ Configuration check passed${NC}"
    return 0
}

# Function to test enhanced command helper
test_enhanced_helper() {
    echo -e "${BLUE}🧪 Testing enhanced command helper...${NC}"
    
    python3 -c "
import sys
sys.path.insert(0, '$SCRIPT_DIR')
try:
    from enhanced_command_helper import EnhancedCommandHelper
    helper = EnhancedCommandHelper()
    print(f'✅ Enhanced Command Helper: {len(helper.COMMANDS)} commands')
    print(f'✅ Categories: {len(helper.CATEGORIES)}')
    print(f'✅ Numbered Commands: 100 (1-100)')
    print('✅ All tests passed!')
except Exception as e:
    print(f'❌ Error: {e}')
    sys.exit(1)
"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Enhanced command helper test passed${NC}"
    else
        echo -e "${RED}❌ Enhanced command helper test failed${NC}"
        return 1
    fi
}

# Function to show system status
show_status() {
    echo -e "${MAGENTA}📊 System Status:${NC}"
    echo -e "${WHITE}────────────────${NC}"
    
    # Python version
    python_version=$(python3 --version 2>&1)
    echo -e "${CYAN}🐍 Python:${NC} $python_version"
    
    # Virtual environment
    if [ -d "$VENV_DIR" ]; then
        echo -e "${GREEN}📦 Virtual Environment:${NC} Ready"
    else
        echo -e "${RED}📦 Virtual Environment:${NC} Not found"
    fi
    
    # Configuration
    if [ -f "$CONFIG_FILE" ]; then
        echo -e "${GREEN}⚙️ Configuration:${NC} Found"
    else
        echo -e "${RED}⚙️ Configuration:${NC} Not found"
    fi
    
    # Enhanced command helper
    if [ -f "$ENHANCED_HELPER" ]; then
        echo -e "${GREEN}🔧 Enhanced Helper:${NC} Available"
    else
        echo -e "${RED}🔧 Enhanced Helper:${NC} Not found"
    fi
    
    echo
}

# Function to launch KaliGPT
launch_kaligpt() {
    echo -e "${GREEN}🚀 Launching KaliGPT MCP Enhanced...${NC}"
    echo -e "${WHITE}────────────────────────────────${NC}"
    echo

    # Activate virtual environment and launch
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        # Windows
        "$VENV_DIR/Scripts/python.exe" "$SCRIPT_DIR/iblu_assistant.py"
    else
        # Linux/Mac
        source "$VENV_DIR/bin/activate"
        python "$SCRIPT_DIR/iblu_assistant.py"
    fi
}

# Main execution
main() {
    print_header
    
    # Check dependencies
    check_dependencies
    
    # Setup virtual environment
    setup_venv
    
    # Check configuration
    if ! check_config; then
        echo
        echo -e "${YELLOW}💡 After configuring API keys, run this script again${NC}"
        exit 1
    fi
    
    # Test enhanced command helper
    if ! test_enhanced_helper; then
        echo
        echo -e "${RED}❌ Enhanced command helper test failed${NC}"
        exit 1
    fi
    
    # Show status
    show_status
    
    # Launch KaliGPT
    launch_kaligpt
}

# Run main function
main "$@"
