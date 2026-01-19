#!/bin/bash

# 🔥 IBLU KALIGPT Setup Guide 🔥
# Quick setup instructions for IBLU Professional Hacking Assistant

echo "🔥 IBLU PROFESSIONAL HACKING ASSISTANT - SETUP GUIDE"
echo "======================================================"
echo ""

# Check if already in IBLU_KALIGPTWITHMCP directory
if [ -d ".git" ] && [ -f "iblu_assistant.py" ]; then
    echo "✅ Already in IBLU_KALIGPTWITHMCP directory"
    echo ""
else
    echo "📁 Step 1: Clone or Navigate to Repository"
    echo "==========================================="
    echo ""
    echo "If not cloned yet:"
    echo "  git clone https://github.com/iblu23/IBLU_KALIGPTWITHMCP"
    echo "  cd IBLU_KALIGPTWITHMCP"
    echo ""
    echo "If already cloned:"
    echo "  cd IBLU_KALIGPTWITHMCP"
    echo "  git pull origin main  # Get latest updates"
    echo ""
    exit 1
fi

echo "📦 Step 2: Install HexStrike Tools (Optional)"
echo "============================================="
echo ""
echo "The install_hexstrike_tools.sh script installs 50+ security tools."
echo ""
read -p "Do you want to install HexStrike tools now? (y/n): " install_tools

if [ "$install_tools" = "y" ] || [ "$install_tools" = "Y" ]; then
    if [ -f "install_hexstrike_tools.sh" ]; then
        chmod +x install_hexstrike_tools.sh
        echo "🔧 Running HexStrike tools installation..."
        echo "⚠️  This requires sudo privileges and may take several minutes"
        sudo ./install_hexstrike_tools.sh
    else
        echo "❌ install_hexstrike_tools.sh not found!"
        echo "💡 Make sure you're in the IBLU_KALIGPTWITHMCP directory"
    fi
else
    echo "⏭️  Skipping HexStrike tools installation"
    echo "💡 You can install them later with: sudo ./install_hexstrike_tools.sh"
fi

echo ""
echo "🔑 Step 3: Configure API Keys"
echo "=============================="
echo ""
echo "Choose an option:"
echo "  1. Quick manual setup (recommended)"
echo "  2. Auto-discover existing keys"
echo "  3. Skip for now"
echo ""
read -p "Enter choice (1-3): " api_choice

case $api_choice in
    1)
        if [ -f "quick_setup.sh" ]; then
            chmod +x quick_setup.sh
            ./quick_setup.sh
        else
            echo "❌ quick_setup.sh not found!"
        fi
        ;;
    2)
        if [ -f "find_api_keys.sh" ]; then
            chmod +x find_api_keys.sh
            ./find_api_keys.sh
        else
            echo "❌ find_api_keys.sh not found!"
        fi
        ;;
    3)
        echo "⏭️  Skipping API key setup"
        echo "💡 You can configure them later with: ./quick_setup.sh"
        ;;
    *)
        echo "❌ Invalid choice"
        ;;
esac

echo ""
echo "🚀 Step 4: Run IBLU Assistant"
echo "=============================="
echo ""
echo "Starting IBLU Professional Hacking Assistant..."
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 iblu_assistant.py
else
    echo "❌ Python 3 not found!"
    echo "💡 Install with: sudo apt install python3"
fi
