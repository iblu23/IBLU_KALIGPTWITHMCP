#!/usr/bin/env python3
"""
🔧 prompt_toolkit Initialization Test 🔧
"""

import sys
import os

def test_prompt_toolkit():
    """Test and initialize prompt_toolkit functionality"""
    
    print("🔧 Testing prompt_toolkit initialization...")
    
    try:
        from prompt_toolkit import prompt
        print("✅ prompt_toolkit imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import prompt_toolkit: {e}")
        print("📦 Installing prompt_toolkit...")
        os.system("pip3 install prompt_toolkit")
        return False
    
    try:
        from prompt_toolkit.history import FileHistory
        from prompt_toolkit.completion import WordCompleter
        print("✅ Additional components imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import components: {e}")
        return False
    
    # Test basic functionality
    try:
        commands = WordCompleter(['hello', 'help', 'exit'], ignore_case=True)
        print("✅ WordCompleter created successfully")
        
        # Test history
        history = FileHistory('test_history.txt')
        print("✅ FileHistory created successfully")
        
        print("\n🎯 Running interactive test...")
        print("💬 Type something and press Enter (or Ctrl+C to exit)")
        
        text = prompt(
            'Test> ',
            completer=commands,
            history=history,
            complete_while_typing=True
        )
        
        print(f"✅ Success! You typed: {text}")
        return True
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        return False

def main():
    """Main initialization function"""
    print("🔥 IBLU prompt_toolkit Initialization 🔥")
    print("-" * 40)
    
    success = test_prompt_toolkit()
    
    if success:
        print("\n✅ prompt_toolkit is ready to use!")
        print("🚀 You can now run:")
        print("   python3 simple_prompt_demo.py")
        print("   python3 interactive_chat.py")
    else:
        print("\n❌ Initialization failed")
        print("🔧 Try manual installation:")
        print("   pip3 install prompt_toolkit")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Test interrupted")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
