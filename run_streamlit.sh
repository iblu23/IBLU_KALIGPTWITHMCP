#!/bin/bash
"""
🚀 Streamlit Chat App Launcher 🚀
"""

echo "🔥 Starting IBLU Streamlit Chat App... 🔥"

# Check if streamlit is installed
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "❌ Streamlit not found. Installing..."
    pip3 install streamlit
fi

# Check if requirements are met
echo "📦 Installing requirements..."
pip3 install -r requirements.txt

# Start the Streamlit app
echo "🌐 Launching web interface..."
streamlit run streamlit_chat.py --server.port 8501 --server.headless false

echo "✅ Chat app should be available at http://localhost:8501"
