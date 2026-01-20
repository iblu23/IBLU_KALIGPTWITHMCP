#!/bin/bash
"""
🧪 Complete Interface Test Suite 🧪
"""

echo "🔥 IBLU Interface Testing Suite 🔥"
echo "=================================="

# Test 1: Simple prompt_toolkit demo
echo ""
echo "📝 Test 1: Simple prompt_toolkit Demo"
echo "Type 'hello' and press Enter, then Ctrl+C to continue"
python3 simple_prompt_demo.py

# Test 2: Interactive chat
echo ""
echo "📝 Test 2: Interactive Chat (Enhanced)"
echo "Type 'help' for commands, then 'exit' to continue"
python3 interactive_chat.py

# Test 3: Streamlit (if available)
echo ""
echo "📝 Test 3: Streamlit Web Interface"
echo "Starting web interface on http://localhost:8501"
echo "Press Ctrl+C to stop and continue"
streamlit run simple_chat.py --server.port 8501 --server.headless true &
STREAMLIT_PID=$!

# Wait a bit for Streamlit to start
sleep 3

echo "✅ Streamlit should be running at http://localhost:8501"
echo "Press Enter to stop Streamlit and continue..."
read

# Stop Streamlit
kill $STREAMLIT_PID 2>/dev/null

echo ""
echo "🎉 All tests completed!"
echo "🚀 Your interfaces are ready to use:"
echo "   • CLI Chat: python3 interactive_chat.py"
echo "   • Simple Demo: python3 simple_prompt_demo.py"
echo "   • Web Interface: streamlit run simple_chat.py"
