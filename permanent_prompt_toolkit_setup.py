#!/usr/bin/env python3
"""
🔥 Permanent prompt_toolkit Setup & Verification 🔥
"""

import subprocess
import sys
import os
from pathlib import Path

def check_and_install_dependencies():
    """Check and install all required dependencies"""
    print("🔧 Checking dependencies...")
    
    # Check prompt_toolkit
    try:
        import prompt_toolkit
        print("✅ prompt_toolkit available")
    except ImportError:
        print("📦 Installing prompt_toolkit...")
        subprocess.run([sys.executable, "-m", "pip", "install", "prompt_toolkit"], check=True)
    
    # Check other dependencies
    requirements_file = Path(__file__).parent / "requirements.txt"
    if requirements_file.exists():
        print("📦 Installing all requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(requirements_file)], check=True)
    
    print("✅ All dependencies installed!")

def test_integration():
    """Test the prompt_toolkit integration"""
    print("\n🧪 Testing prompt_toolkit integration...")
    
    try:
        # Test basic imports
        from prompt_toolkit import prompt
        from prompt_toolkit.history import FileHistory
        from prompt_toolkit.completion import WordCompleter
        from prompt_toolkit.styles import Style
        print("✅ All prompt_toolkit components imported")
        
        # Test IBLU assistant integration
        sys.path.insert(0, str(Path(__file__).parent))
        try:
            from iblu_assistant import KaliGPTMCPAssistant
            print("✅ IBLU Assistant imported successfully")
            
            # Test configuration loading
            from iblu_assistant import load_config
            config = load_config()
            print("✅ Configuration loaded")
            
            # Test assistant initialization
            assistant = KaliGPTMCPAssistant(config)
            print("✅ Assistant initialized with prompt_toolkit")
            
            # Test prompt_toolkit features
            if hasattr(assistant, 'prompt_toolkit_enabled'):
                if assistant.prompt_toolkit_enabled:
                    print("✅ prompt_toolkit integration enabled")
                    print(f"✅ {len(assistant.commands.words)} commands available for completion")
                    print(f"✅ History file: {assistant.history.history_filename}")
                else:
                    print("⚠️  prompt_toolkit integration disabled")
            
        except ImportError as e:
            print(f"⚠️  IBLU Assistant import error: {e}")
        
        print("\n🎯 Running interactive test...")
        print("💬 Type a command (try 'help' or 'scan') and press Enter")
        print("🔧 Use TAB for auto-completion, Ctrl+C to exit")
        
        # Simple test
        commands = WordCompleter(['help', 'scan', 'exit', 'nmap'], ignore_case=True)
        history = FileHistory('test_setup_history.txt')
        
        test_input = prompt(
            'Test> ',
            completer=commands,
            history=history,
            complete_while_typing=True
        )
        
        print(f"✅ Test successful! You typed: {test_input}")
        
        return True
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False

def create_permanent_setup():
    """Create permanent setup configuration"""
    print("\n🔧 Creating permanent setup...")
    
    # Create history directory if needed
    history_dir = Path.home() / ".iblu"
    history_dir.mkdir(exist_ok=True)
    
    # Create environment file
    env_file = Path(__file__).parent / ".iblu_env"
    with open(env_file, 'w') as f:
        f.write("# IBLU Environment Configuration\n")
        f.write("PROMPT_TOOLKIT_ENABLED=1\n")
        f.write("IBLU_HISTORY_FILE=" + str(history_dir / "chat_history.txt") + "\n")
        f.write("IBLU_AUTO_COMPLETION=1\n")
    
    print(f"✅ Environment configured: {env_file}")
    print(f"✅ History directory: {history_dir}")

def main():
    """Main setup function"""
    print("🔥 IBLU Permanent prompt_toolkit Setup 🔥")
    print("=" * 50)
    
    try:
        # Install dependencies
        check_and_install_dependencies()
        
        # Test integration
        success = test_integration()
        
        if success:
            # Create permanent setup
            create_permanent_setup()
            
            print("\n🎉 SETUP COMPLETE!")
            print("🚀 prompt_toolkit is now permanently integrated!")
            print("\n📖 Usage:")
            print("   python3 iblu_assistant.py          # Main assistant")
            print("   python3 interactive_chat.py        # Standalone chat")
            print("   python3 simple_prompt_demo.py       # Basic demo")
            print("   streamlit run simple_chat.py        # Web interface")
            print("\n🔧 Features:")
            print("   • TAB auto-completion for 50+ commands")
            print("   • Persistent chat history")
            print("   • Styled prompts with colors")
            print("   • Graceful fallback to basic input")
        else:
            print("\n❌ Setup failed. Check the error messages above.")
            
    except KeyboardInterrupt:
        print("\n👋 Setup interrupted")
    except Exception as e:
        print(f"\n❌ Setup error: {e}")

if __name__ == "__main__":
    main()
