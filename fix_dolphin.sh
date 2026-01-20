#!/bin/bash

echo "🔧 Fixing Dolphin censorship issue..."

# Create proper config.json
cat > config.json << 'EOF'
{
    "llama_keys": ["local"],
    "openai_keys": [],
    "gemini_keys": [],
    "mistral_keys": [],
    "gemini_cli_keys": []
}
EOF

echo "✅ Config updated - Now restart IBLU and use /llama command"

# Test detection
python3 -c "
from iblu_assistant import KaliGPTMCPAssistant, load_config

config = load_config()
assistant = KaliGPTMCPAssistant(config)
assistant.current_ai_provider = assistant.current_ai_provider.LLAMA

print('🎯 DETECTION RESULTS:')
print(f'Provider: {assistant.current_ai_provider.value}')
print(f'Model: {assistant.get_current_model_name()}')
print(f'Uncensored: {assistant.is_current_model_uncensored()}')
print()
if assistant.is_current_model_uncensored():
    print('🎉 DOLPHIN IS READY - Use /llama command!')
else:
    print('❌ Still having issues')
"
