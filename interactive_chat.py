#!/usr/bin/env python3
"""
💬 Interactive Chat with Auto-Completion 💬
🔧 Advanced prompt_toolkit integration with history and commands 🔧
"""

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
import os
from pathlib import Path

def main():
    """Interactive chat with auto-completion and history"""
    
    # Define command completions
    commands = WordCompleter(
        ['hello', 'help', 'exit', 'how are you', 'scan', 'hack', 'security', 'vulnerability', 'network', 'port', 'nmap', 'tools', 'status', 'clear', 'quit'],
        ignore_case=True
    )
    
    # Style for the prompt
    style = Style.from_dict({
        'prompt': '#00aa00 bold',
        'completion-menu': 'bg:#008800 #ffffff',
        'completion-menu.completion.current': 'bg:#ffffff #000000',
        'scrollbar.background': 'bg:#88aaaa',
        'scrollbar.button': 'bg:#4444ff',
    })
    
    # Create history file path
    history_file = Path(__file__).parent / 'chat_history.txt'
    
    print("🔥 IBLU Interactive Chat 🔥")
    print("💬 Type 'help' for commands or 'exit' to quit")
    print("🔧 Use TAB for auto-completion")
    print("📜 Chat history is saved automatically")
    print("-" * 50)
    
    while True:
        try:
            # Get user input with auto-completion and history
            text = prompt(
                'You: ',
                completer=commands,
                history=FileHistory(str(history_file)),
                complete_while_typing=True,
                style=style
            )
            
            # Handle exit commands
            if text.lower() in ['exit', 'quit', 'q']:
                print("👋 Goodbye!")
                break
            
            # Handle help command
            if text.lower() == 'help':
                print_help()
                continue
            
            # Handle clear command
            if text.lower() == 'clear':
                os.system('clear' if os.name == 'posix' else 'cls')
                continue
            
            # Echo the input (you can replace this with actual chat logic)
            print(f"🤖 Bot: You typed: {text}")
            
            # Simple responses for demo
            response = get_simple_response(text)
            if response:
                print(f"🤖 Bot: {response}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except EOFError:
            print("\n👋 Goodbye!")
            break

def print_help():
    """Print help information"""
    help_text = """
🔥 **Available Commands:** 🔥
• hello - Greet the bot
• help - Show this help message
• exit/quit - Exit the chat
• how are you - Check bot status
• scan - Start security scan
• hack - Hacking tools menu
• security - Security options
• vulnerability - Vulnerability assessment
• network - Network tools
• port - Port scanning
• nmap - Network mapper
• tools - Available tools
• status - System status
• clear - Clear screen

🔧 **Features:**
• TAB auto-completion
• Command history (↑/↓ arrows)
• Case-insensitive commands
• Persistent chat history
    """
    print(help_text)

def get_simple_response(text):
    """Get simple demo responses"""
    text_lower = text.lower()
    
    responses = {
        'hello': '👋 Hello! How can I help you today?',
        'how are you': '😊 I\'m doing great! Ready to assist with security tasks!',
        'scan': '🔍 Security scanning mode activated. Target?',
        'hack': '🛡️ Hacking tools ready. What would you like to test?',
        'security': '🔒 Security protocols engaged. How can I help?',
        'vulnerability': '🎯 Vulnerability assessment mode. Target system?',
        'network': '🌐 Network tools ready. What network analysis?',
        'port': '🔌 Port scanning mode. Specify target and range?',
        'nmap': '🗺️ Nmap integration ready. Target?',
        'tools': '🔧 Available tools: nmap, sqlmap, dirb, nikto, and more!',
        'status': '📊 System status: All operational. Ready for tasks!'
    }
    
    return responses.get(text_lower)

if __name__ == "__main__":
    main()
