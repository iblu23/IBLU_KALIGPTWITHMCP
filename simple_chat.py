#!/usr/bin/env python3
"""
💬 Simple Streamlit Chat App 💬
"""

import streamlit as st

st.title("Chat App")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Type here...")

if user_input:
    st.session_state.messages.append(("You", user_input))

for role, msg in st.session_state.messages:
    st.write(f"**{role}:** {msg}")
