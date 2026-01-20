#!/bin/bash
"""
🚀 Interactive Chat Launcher 🚀
"""

echo "🔥 Starting IBLU Interactive Chat..."

# Check if prompt_toolkit is available
if ! python3 -c "from prompt_toolkit import prompt" 2>/dev/null; then
    echo "❌ prompt_toolkit not found. Installing..."
    pip3 install prompt_toolkit
fi

# Install other requirements
echo "📦 Installing requirements..."
pip3 install -r requirements.txt

# Run the interactive chat
echo "💬 Starting interactive chat..."
python3 interactive_chat.py
