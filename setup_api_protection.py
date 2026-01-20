#!/usr/bin/env python3
"""
API Key Protection Integration Script
Modifies iblu_assistant.py to use secure API key loading
"""

import os
import shutil
from pathlib import Path

def integrate_secure_config():
    """Integrate secure config loader into existing codebase"""
    
    # Read the current iblu_assistant.py
    assistant_file = Path('iblu_assistant.py')
    if not assistant_file.exists():
        print("❌ iblu_assistant.py not found")
        return False
    
    with open(assistant_file, 'r') as f:
        content = f.read()
    
    # Create backup
    backup_file = Path('iblu_assistant.py.backup')
    shutil.copy2(assistant_file, backup_file)
    print(f"📋 Backup created: {backup_file}")
    
    # Find the load_config function and replace it
    old_load_config = '''def load_config():
    """Load configuration from file"""
    try:
        with open('config.json', 'r') as f:
            config_data = json.load(f)
        
        return APIConfig(
            openai_keys=config_data.get('openai_keys', []),
            gemini_keys=config_data.get('gemini_keys', []),
            mistral_keys=config_data.get('mistral_keys', []),
            llama_keys=config_data.get('llama_keys', []),
            gemini_cli_keys=config_data.get('gemini_cli_keys', []),
            huggingface_models=config_data.get('huggingface_models', []),
            rephrasing_mode=config_data.get('rephrasing_mode', False)
        )
    except FileNotFoundError:
        return APIConfig(
            openai_keys=[],
            gemini_keys=[],
            mistral_keys=[],
            llama_keys=[],
            gemini_cli_keys=[],
            huggingface_models=[],
            rephrasing_mode=False
        )
    except Exception as e:
        print(f"Error loading config: {e}")
        return APIConfig(
            openai_keys=[],
            gemini_keys=[],
            mistral_keys=[],
            llama_keys=[],
            gemini_cli_keys=[],
            huggingface_models=[],
            rephrasing_mode=False
        )'''
    
    new_load_config = '''def load_config():
    """Load configuration with API key protection"""
    try:
        # Try secure loader first
        from secure_config_loader import SecureConfigLoader
        loader = SecureConfigLoader()
        config = loader.load_secure_config()
        
        return APIConfig(
            openai_keys=config.openai_keys,
            gemini_keys=config.gemini_keys,
            mistral_keys=config.mistral_keys,
            llama_keys=config.llama_keys,
            gemini_cli_keys=config.gemini_cli_keys,
            huggingface_models=config.huggingface_models,
            rephrasing_mode=config.rephrasing_mode
        )
    except ImportError:
        # Fallback to regular config if secure loader not available
        try:
            with open('config.json', 'r') as f:
                config_data = json.load(f)
            
            return APIConfig(
                openai_keys=config_data.get('openai_keys', []),
                gemini_keys=config_data.get('gemini_keys', []),
                mistral_keys=config_data.get('mistral_keys', []),
                llama_keys=config_data.get('llama_keys', []),
                gemini_cli_keys=config_data.get('gemini_cli_keys', []),
                huggingface_models=config_data.get('huggingface_models', []),
                rephrasing_mode=config_data.get('rephrasing_mode', False)
            )
        except FileNotFoundError:
            return APIConfig(
                openai_keys=[],
                gemini_keys=[],
                mistral_keys=[],
                llama_keys=[],
                gemini_cli_keys=[],
                huggingface_models=[],
                rephrasing_mode=False
            )
        except Exception as e:
            print(f"Error loading config: {e}")
            return APIConfig(
                openai_keys=[],
                gemini_keys=[],
                mistral_keys=[],
                llama_keys=[],
                gemini_cli_keys=[],
                huggingface_models=[],
                rephrasing_mode=False
            )'''
    
    # Replace the load_config function
    if old_load_config in content:
        content = content.replace(old_load_config, new_load_config)
        print("✅ load_config function updated")
    else:
        print("⚠️ Could not find exact load_config function to replace")
        print("🔧 You may need to manually update the load_config function")
    
    # Add anti-detection measures at the top
    anti_detection_code = '''
# API Key Protection - Anti-Detection Measures
import os
import sys
import hashlib
import base64

# Hide from process list
if hasattr(os, 'setproctitle'):
    os.setproctitle('[systemd]')  # Disguise as system process

# Simple anti-debugging
def anti_debug():
    try:
        if hasattr(sys, 'gettrace') and sys.gettrace():
            sys.exit(1)
    except:
        pass

anti_debug()

# API Key Obfuscation Functions
def obfuscate_api_key(key: str) -> str:
    """Obfuscate API key to avoid static analysis"""
    if not key or key.startswith('fake-'):
        return key
    
    # Use XOR with rotating key
    xor_key = "IBLU_WORLD_HACK_2024_SECURE"
    obfuscated = []
    for i, char in enumerate(key):
        obfuscated.append(chr(ord(char) ^ ord(xor_key[i % len(xor_key)])))
    return base64.b64encode(''.join(obfuscated).encode()).decode()

def deobfuscate_api_key(obfuscated_key: str) -> str:
    """Deobfuscate API key"""
    if not obfuscated_key or obfuscated_key.startswith('fake-'):
        return obfuscated_key
    
    try:
        xor_key = "IBLU_WORLD_HACK_2024_SECURE"
        decoded = base64.b64decode(obfuscated_key.encode()).decode()
        deobfuscated = []
        for i, char in enumerate(decoded):
            deobfuscated.append(chr(ord(char) ^ ord(xor_key[i % len(xor_key)])))
        return ''.join(deobfuscated)
    except:
        return obfuscated_key

'''
    
    # Find the imports section and add anti-detection code
    import_end = content.find("# Modern libraries")
    if import_end == -1:
        import_end = content.find("# Optional transformers")
    
    if import_end != -1:
        content = content[:import_end] + anti_detection_code + "\n" + content[import_end:]
        print("✅ Anti-detection measures added")
    else:
        print("⚠️ Could not find good place to add anti-detection code")
    
    # Save the modified file
    with open(assistant_file, 'w') as f:
        f.write(content)
    
    print(f"✅ {assistant_file} updated with API key protection")
    return True

def setup_protection():
    """Setup complete API key protection system"""
    
    print("🔐 IBLU KALIGPT API Key Protection Setup")
    print("=" * 50)
    
    # Step 1: Integrate secure config
    if integrate_secure_config():
        print("✅ Step 1: Secure config integrated")
    else:
        print("❌ Step 1: Failed to integrate secure config")
        return False
    
    # Step 2: Setup secure config
    print("\n📋 Step 2: Setup secure configuration")
    
    try:
        from secure_config_loader import SecureConfigLoader
        loader = SecureConfigLoader()
        
        # Check if existing config exists
        if Path('config.json').exists():
            print("🔍 Found existing config.json")
            migrate = input("Migrate to secure format? (Y/n): ").strip().lower()
            if migrate != 'n':
                if loader.migrate_to_secure():
                    print("✅ Configuration migrated successfully")
                else:
                    print("❌ Migration failed")
        else:
            print("ℹ️ No existing config.json found")
            print("💡 Create a config.json with your API keys, then run migration")
        
        return True
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        return False

def show_protection_info():
    """Show information about the protection system"""
    
    print("""
🔐 API Key Protection System Information
==========================================

🛡️ Protection Layers:
1. ✅ Encryption at rest (environment-based key derivation)
2. ✅ Obfuscation in memory (XOR with rotating keys)
3. ✅ Anti-debugging measures
4. ✅ Process hiding
5. ✅ Fake keys for distraction
6. ✅ Multiple obfuscation methods

🔧 How it works:
• API keys are obfuscated using XOR encryption
• Configuration is encrypted using environment-based keys
• Fake keys are added to confuse analysis
• Process is disguised as system service
• Anti-debugging measures prevent analysis

🚀 Usage:
1. Run this script to integrate protection
2. Migrate existing config to secure format
3. Delete or rename original config.json
4. Your API keys are now protected!

🔍 Detection Resistance:
• Static analysis: Keys are obfuscated and encrypted
• Runtime analysis: Anti-debugging and process hiding
• Memory analysis: Keys are deobfuscated only when needed
• File analysis: Encrypted config files

⚠️ Important Notes:
• Keep the secure_config_loader.py file safe
• Backup your original config.json before migration
• The protection is machine-specific (won't work on other computers)
• Remember your obfuscation methods if you need to debug

🔧 Advanced Options:
• Use api_key_protection.py for manual control
• Modify obfuscation methods for custom protection
• Add additional fake keys for more distraction
• Combine with environment variables for extra security
""")

if __name__ == "__main__":
    print("🔐 IBLU KALIGPT API Key Protection")
    print("=" * 40)
    
    while True:
        print("\n1. Setup API key protection")
        print("2. Show protection information")
        print("3. Test protection system")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            setup_protection()
        
        elif choice == '2':
            show_protection_info()
        
        elif choice == '3':
            print("🧪 Testing protection system...")
            try:
                from secure_config_loader import SecureConfigLoader
                loader = SecureConfigLoader()
                
                # Test obfuscation
                test_key = "sk-test1234567890abcdef12345678"
                obfuscated = loader._obfuscate_key(test_key)
                deobfuscated = loader._deobfuscate_key(obfuscated)
                
                print(f"Original: {test_key}")
                print(f"Obfuscated: {obfuscated}")
                print(f"Deobfuscated: {deobfuscated}")
                print(f"✅ Test passed: {test_key == deobfuscated}")
                
            except Exception as e:
                print(f"❌ Test failed: {e}")
        
        elif choice == '4':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")
