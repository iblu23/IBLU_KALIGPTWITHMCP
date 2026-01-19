#!/bin/bash

# 🔥 IBLU API Keys Discovery Script 🔥
# 🚀 Find existing API keys in your system 🚀

echo "🔥 IBLU Professional Hacking Assistant - API Keys Discovery"
echo "======================================================"

echo "🔍 Searching for API keys in common locations..."
echo "============================================"

found_keys=()

# Function to validate API key format
validate_key() {
    local key="$1"
    local provider="$2"
    
    case "$provider" in
        "OpenAI")
            if [[ $key =~ ^sk-[a-zA-Z0-9]{48}$ ]]; then
                return 0
            fi
            ;;
        "Gemini")
            if [[ $key =~ ^AIza[a-zA-Z0-9_-]{35}$ ]]; then
                return 0
            fi
            ;;
        "Mistral")
            if [[ $key =~ ^[a-zA-Z0-9_-]{32,}$ ]]; then
                return 0
            fi
            ;;
    esac
    return 1
}

# Search in config files
echo "📄 Checking configuration files..."
config_files=("config.json" "*.env" ".env.local" "secrets.txt" "api_keys.txt")
for file in "${config_files[@]}"; do
    if [ -f "$file" ]; then
        echo "📄 Checking $file..."
        
        # Search for OpenAI keys
        if grep -q "sk-" "$file" 2>/dev/null; then
            keys=$(grep -o 'sk-[a-zA-Z0-9]{48}' "$file" 2>/dev/null | head -3)
            for key in $keys; do
                if validate_key "$key" "OpenAI"; then
                    found_keys+=("OpenAI:$key")
                    echo "  ✅ Found OpenAI key: ${key:0:8}...${key: -4}"
                fi
            done
        fi
        
        # Search for Gemini keys
        if grep -q "AIza" "$file" 2>/dev/null; then
            keys=$(grep -o 'AIza[a-zA-Z0-9_-]{35}' "$file" 2>/dev/null | head -3)
            for key in $keys; do
                if validate_key "$key" "Gemini"; then
                    found_keys+=("Gemini:$key")
                    echo "  ✅ Found Gemini key: ${key:0:8}...${key: -4}"
                fi
            done
        fi
    fi
done

# Search environment variables
echo ""
echo "🔍 Checking environment variables..."
env_vars=("OPENAI_API_KEY" "GEMINI_API_KEY" "MISTRAL_API_KEY")
for var in "${env_vars[@]}"; do
    if [ -n "${!var}" ]; then
        key="${!var}"
        provider=""
        case "$var" in
            "OPENAI_API_KEY") provider="OpenAI" ;;
            "GEMINI_API_KEY") provider="Gemini" ;;
            "MISTRAL_API_KEY") provider="Mistral" ;;
        esac
        
        if validate_key "$key" "$provider"; then
            found_keys+=("$provider:$key")
            echo "  ✅ Found $provider key in environment: ${key:0:8}...${key -4}"
        fi
    fi
done

# Search common directories
echo ""
echo "📁 Searching common directories..."
common_dirs=("$HOME/.config" "$HOME/.local/share" "$HOME/.cache" "$HOME/.secrets")
for dir in "${common_dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "🔍 Scanning $dir..."
        
        # Search for JSON files with API keys
        json_files=$(find "$dir" -name "*.json" 2>/dev/null | head -5)
        for file in $json_files; do
            if grep -q "sk-" "$file" 2>/dev/null; then
                keys=$(grep -o 'sk-[a-zA-Z0-9]{48}' "$file" 2>/dev/null | head -2)
                for key in $keys; do
                    if validate_key "$key" "OpenAI"; then
                        found_keys+=("OpenAI:$key")
                        echo "  ✅ Found OpenAI key in $file: ${key:0:8}...${key: -4}"
                    fi
                done
            fi
        done
        
        # Search for env files with API keys
        env_files=$(find "$dir" -name "*.env" 2>/dev/null | head -5)
        for file in $env_files; do
            if grep -q "sk-" "$file" 2>/dev/null; then
                keys=$(grep -o 'sk-[a-zA-Z0-9]{48}' "$file" 2>/dev/null | head -2)
                for key in $keys; do
                    if validate_key "$key" "OpenAI"; then
                        found_keys+=("OpenAI:$key")
                        echo "  ✅ Found OpenAI key in $file: ${key:0:8}...${key: -4}"
                    fi
                done
            fi
        done
    fi
done

# Summary
echo ""
echo "📊 API Keys Discovery Summary:"
echo "============================"
if [ ${#found_keys[@]} -eq 0 ]; then
    echo "❌ No API keys found automatically"
    echo ""
    echo "💡 You'll need to add API keys manually:"
    echo "   • OpenAI: https://platform.openai.com/api-keys"
    echo "   • Gemini: https://aistudio.google.com/app/apikey"
    echo "   • Mistral: https://console.mistral.ai/api-keys"
    echo ""
    echo "🔧 Run: ./setup_api_keys.sh to add them manually"
else
    echo "✅ Found ${#found_keys[@]} API key(s):"
    for key_info in "${found_keys[@]}"; do
        provider="${key_info%%:*}"
        key="${key_info##*:}"
        echo "  📋 $provider: ${key:0:8}...${key: -4}"
    done
    
    echo ""
    echo "🔧 Adding found keys to config.json..."
    
    # Backup current config
    cp config.json config.json.backup
    
    # Add found keys to config
    for key_info in "${found_keys[@]}"; do
        provider="${key_info%%:*}"
        key="${key_info##*:}"
        
        case "$provider" in
            "OpenAI")
                sed -i "s/\"openai_keys\": \[\]/\"openai_keys\": [\"$key\"]/" config.json
                ;;
            "Gemini")
                sed -i "s/\"gemini_keys\": \[\]/\"gemini_keys\": [\"$key\"]/" config.json
                ;;
            "Mistral")
                sed -i "s/\"mistral_keys\": \[\]/\"mistral_keys\": [\"$key\"]/" config.json
                ;;
        esac
        echo "  ✅ Added $provider key to config.json"
    done
    
    echo "🎉 API keys automatically added to config.json!"
    echo "💡 You can now run: python3 iblu_assistant.py"
fi

echo ""
echo "🔥 Discovery completed!"
echo "🚀 Ready for professional cybersecurity testing!"
