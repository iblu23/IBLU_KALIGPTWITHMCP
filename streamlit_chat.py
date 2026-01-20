#!/usr/bin/env python3
"""
🚀 IBLU Streamlit Chat App 🚀
💬 Web-based Chat Interface for IBLU Assistant 💬
"""

import streamlit as st
import sys
import os
from pathlib import Path

# Add the project root to Python path to import iblu_assistant
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

try:
    from iblu_assistant import IBLUAssistant
    IBLU_AVAILABLE = True
except ImportError:
    IBLU_AVAILABLE = False
    st.warning("IBLU Assistant not available. Running in demo mode.")

def main():
    """Main Streamlit chat application"""
    st.title("🔥 IBLU Chat App 🔥")
    st.markdown("*Advanced Cybersecurity Automation Platform*")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "iblu_assistant" not in st.session_state and IBLU_AVAILABLE:
        with st.spinner("Initializing IBLU Assistant..."):
            try:
                st.session_state.iblu_assistant = IBLUAssistant()
                st.success("✅ IBLU Assistant ready!")
            except Exception as e:
                st.error(f"❌ Failed to initialize IBLU Assistant: {e}")
                st.session_state.iblu_assistant = None
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Chat mode selection
        chat_mode = st.selectbox(
            "Chat Mode",
            ["Simple Chat", "IBLU Assistant", "Security Tools"],
            help="Choose how the chat should behave"
        )
        
        # Clear chat button
        if st.button("🗑️ Clear Chat", type="secondary"):
            st.session_state.messages = []
            st.rerun()
        
        # Show system info
        st.markdown("---")
        st.markdown("### 📊 System Info")
        st.markdown(f"- **IBLU Available**: {'✅' if IBLU_AVAILABLE else '❌'}")
        st.markdown(f"- **Chat Mode**: {chat_mode}")
        st.markdown(f"- **Messages**: {len(st.session_state.messages)}")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message
        user_message = {"role": "user", "content": prompt}
        st.session_state.messages.append(user_message)
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response based on mode
        with st.chat_message("assistant"):
            if chat_mode == "Simple Chat":
                # Simple echo response
                response = f"You said: {prompt}"
            elif chat_mode == "IBLU Assistant" and IBLU_AVAILABLE and st.session_state.iblu_assistant:
                # Use IBLU Assistant
                with st.spinner("🤔 Thinking..."):
                    try:
                        # This would need to be adapted based on IBLU's actual interface
                        response = "🔥 IBLU Assistant response would go here. Integration needed."
                    except Exception as e:
                        response = f"❌ Error: {str(e)}"
            else:
                # Demo security-focused responses
                if any(word in prompt.lower() for word in ["scan", "hack", "security", "vulnerability"]):
                    response = "🔒 *Security tools mode activated. IBLU Assistant provides comprehensive security scanning capabilities including network reconnaissance, vulnerability assessment, and automated penetration testing workflows.*"
                elif any(word in prompt.lower() for word in ["help", "commands", "what can you do"]):
                    response = """🚀 **IBLU Assistant Capabilities:**
- 🔍 Network Security Scanning
- 🛡️ Vulnerability Assessment  
- 🤖 Automated Penetration Testing
- 📊 Security Report Generation
- 🔧 Tool Integration & Automation
- 💬 Interactive Chat Interface

Type 'scan <target>' to start a security scan or ask for help!"""
                else:
                    response = f"💬 Received: {prompt}\n\n*Try asking about security scans, vulnerability assessment, or type 'help' for more options.*"
            
            st.markdown(response)
        
        # Add assistant message to session state
        assistant_message = {"role": "assistant", "content": response}
        st.session_state.messages.append(assistant_message)

if __name__ == "__main__":
    main()
