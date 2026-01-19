#!/bin/bash

# 🔥 Quick API Keys Setup Script 🔥
# 🚀 Simple manual setup for IBLU Assistant 🚀

echo "🔥 IBLU Professional Hacking Assistant - Quick API Keys Setup"
echo "============================================================"

echo ""
echo "📋 API Key Setup Instructions:"
echo "=============================="
echo ""
echo "💡 You'll need to add API keys manually:"
echo "   • OpenAI: https://platform.openai.com/api-keys"
echo "   • Gemini: https://aistudio.google.com/app/apikey"
echo "   • Mistral: https://console.mistral.ai/api-keys"
echo ""

# Interactive setup
echo "🔧 Add your API keys (press Enter to skip):"
echo "========================================="

# OpenAI
echo ""
echo "🔑 OpenAI API Key:"
read -p "➡️  Enter your OpenAI API key (or press Enter to skip): " openai_key
if [ -n "$openai_key" ]; then
    # Update config
    sed -i "s/\"openai_keys\": \[\"your-openai-api-key-here\"\]/\"openai_keys\": [\"$openai_key\"]/" config.json
    echo "✅ OpenAI key added!"
fi

# Gemini
echo ""
echo "🔑 Gemini API Key:"
read -p "➡️  Enter your Gemini API key (or press Enter to skip): " gemini_key
if [ -n "$gemini_key" ]; then
    # Update config
    sed -i "s/\"gemini_keys\": \[\"your-gemini-api-key-here\"\]/\"gemini_keys\": [\"$gemini_key\"]/" config.json
    echo "✅ Gemini key added!"
fi

# Mistral
echo ""
echo "🔑 Mistral API Key:"
read -p "➡️  Enter your Mistral API key (or press Enter to skip): " mistral_key
if [ -n "$mistral_key" ]; then
    # Update config
    sed -i "s/\"mistral_keys\": \[\"your-mistral-api-key-here\"\]/\"mistral_keys\": [\"$mistral_key\"]/" config.json
    echo "✅ Mistral key added!"
fi

echo ""
echo "📊 Configuration Summary:"
echo "========================"
echo ""
echo "📄 Current config.json:"
cat config.json
echo ""

# Count configured keys
openai_count=$(grep -o "openai_keys.*your-openai-api-key-here" config.json | wc -l)
gemini_count=$(grep -o "gemini_keys.*your-gemini-api-key-here" config.json | wc -l)
mistral_count=$(grep -o "mistral_keys.*your-mistral-api-key-here" config.json | wc -l)

total_keys=$((3 - openai_count - gemini_count - mistral_count))

echo "🔑 Configured API Keys: $total_keys/3"
echo "   • OpenAI: $([ "$openai_count" -eq 0 ] && echo "✅" || echo "❌")"
echo "   • Gemini: $([ "$gemini_count" -eq 0 ] && echo "✅" || echo "❌")"
echo "   • Mistral: $([ "$mistral_count" -eq 0 ] && echo "✅" || echo "❌")"

echo ""
if [ $total_keys -gt 0 ]; then
    echo "🎉 API keys setup completed!"
    echo "💡 You can now run: python3 iblu_assistant.py"
    echo ""
    echo "🔥 Ready for professional cybersecurity testing with AI!"
else
    echo "⚠️  No API keys were added"
    echo "💡 You can still run the assistant, but AI features will be limited"
    echo "🔧 Run this script again when you have API keys"
fi

echo ""
echo "🚀 Quick Start:"
echo "============="
echo "python3 iblu_assistant.py"
echo ""
echo "🎯 Menu Options:"
echo "  1. IBLU KALIGPT - Use AI providers"
echo "  2. HexStrike Tools - Install security tools"
echo "  3. MCP Status - Check connection"
echo "  4. Configuration - Manage settings"
echo ""
echo "🔥 Happy hacking! (Ethically Only!)"
