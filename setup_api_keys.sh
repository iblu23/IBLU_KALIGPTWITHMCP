#!/bin/bash

# 🔥 IBLU API Keys Configuration Script 🔥
# 🚀 Easy setup for AI providers 🚀

echo "🔥 IBLU Professional Hacking Assistant - API Keys Setup"
echo "======================================================"

# Check if config.json exists
if [ ! -f "config.json" ]; then
    echo "❌ config.json not found!"
    echo "📁 Creating new config file..."
    echo '{"perplexity_keys": [], "openai_keys": [], "gemini_keys": [], "mistral_keys": []}' > config.json
    echo "✅ config.json created!"
fi

echo ""
echo "🔑 Current API Keys Configuration:"
echo "--------------------------------"

# Show current keys (masked)
if command -v jq >/dev/null 2>&1; then
    echo "📋 Perplexity Keys: $(jq -r '.perplexity_keys | length' config.json) configured"
    echo "📋 OpenAI Keys: $(jq -r '.openai_keys | length' config.json) configured"
    echo "📋 Gemini Keys: $(jq -r '.gemini_keys | length' config.json) configured"
    echo "📋 Mistral Keys: $(jq -r '.mistral_keys | length' config.json) configured"
else
    echo "⚠️  jq not installed. Install with: sudo apt install jq"
    echo "📄 Showing raw config.json:"
    cat config.json
fi

echo ""
echo "🔧 API Key Setup Options:"
echo "-------------------------"
echo "1. Add Perplexity API Key"
echo "2. Add OpenAI API Key"
echo "3. Add Gemini API Key"
echo "4. Add Mistral API Key"
echo "5. Show current config"
echo "6. Exit"

read -p "🎯 Choose option (1-6): " choice

case $choice in
    1)
        echo ""
        echo "🔑 Perplexity API Key Setup"
        echo "------------------------"
        echo "💡 Get your API key from: https://www.perplexity.ai/settings/api"
        read -p "🔑 Enter your Perplexity API key: " key
        if [ -n "$key" ]; then
            # Update config with jq if available, otherwise use sed
            if command -v jq >/dev/null 2>&1; then
                jq --arg key "$key" '.perplexity_keys += [$key]' config.json > temp.json && mv temp.json config.json
            else
                # Fallback to sed (less reliable but works)
                sed -i "s/\"perplexity_keys\": \[\]/\"perplexity_keys\": [\"$key\"]/" config.json
            fi
            echo "✅ Perplexity API key added!"
        else
            echo "❌ No key provided!"
        fi
        ;;
    2)
        echo ""
        echo "🔑 OpenAI API Key Setup"
        echo "---------------------"
        echo "💡 Get your API key from: https://platform.openai.com/api-keys"
        read -p "🔑 Enter your OpenAI API key: " key
        if [ -n "$key" ]; then
            if command -v jq >/dev/null 2>&1; then
                jq --arg key "$key" '.openai_keys += [$key]' config.json > temp.json && mv temp.json config.json
            else
                sed -i "s/\"openai_keys\": \[\]/\"openai_keys\": [\"$key\"]/" config.json
            fi
            echo "✅ OpenAI API key added!"
        else
            echo "❌ No key provided!"
        fi
        ;;
    3)
        echo ""
        echo "🔑 Gemini API Key Setup"
        echo "---------------------"
        echo "💡 Get your API key from: https://aistudio.google.com/app/apikey"
        read -p "🔑 Enter your Gemini API key: " key
        if [ -n "$key" ]; then
            if command -v jq >/dev/null 2>&1; then
                jq --arg key "$key" '.gemini_keys += [$key]' config.json > temp.json && mv temp.json config.json
            else
                sed -i "s/\"gemini_keys\": \[\]/\"gemini_keys\": [\"$key\"]/" config.json
            fi
            echo "✅ Gemini API key added!"
        else
            echo "❌ No key provided!"
        fi
        ;;
    4)
        echo ""
        echo "🔑 Mistral API Key Setup"
        echo "----------------------"
        echo "💡 Get your API key from: https://console.mistral.ai/api-keys"
        read -p "🔑 Enter your Mistral API key: " key
        if [ -n "$key" ]; then
            if command -v jq >/dev/null 2>&1; then
                jq --arg key "$key" '.mistral_keys += [$key]' config.json > temp.json && mv temp.json config.json
            else
                sed -i "s/\"mistral_keys\": \[\]/\"mistral_keys\": [\"$key\"]/" config.json
            fi
            echo "✅ Mistral API key added!"
        else
            echo "❌ No key provided!"
        fi
        ;;
    5)
        echo ""
        echo "📄 Current Configuration:"
        echo "----------------------"
        cat config.json
        ;;
    6)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice!"
        ;;
esac

echo ""
echo "🎉 API Keys setup completed!"
echo "💡 You can now run: python3 iblu_assistant.py"
echo "🔥 Ready for professional cybersecurity testing!"
