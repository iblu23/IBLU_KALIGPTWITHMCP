#!/usr/bin/env python3
"""
🔑 IBLU KALIGPT - Global API Key Configuration & Export System
🌍 Configure and export API keys globally and permanently
"""

import os
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

class GlobalAPIKeyManager:
    """Global API Key Manager for permanent configuration and export"""
    
    def __init__(self):
        self.home_dir = Path.home()
        self.config_dir = self.home_dir / '.iblu' / 'secrets'
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Shell configuration files
        self.bashrc = self.home_dir / '.bashrc'
        self.zshrc = self.home_dir / '.zshrc'
        self.profile = self.home_dir / '.profile'
        
        # Environment file
        self.env_file = self.home_dir / '.iblu' / 'api_keys.env'
        
    def backup_shell_configs(self):
        """Backup existing shell configurations"""
        backups = []
        for config_file in [self.bashrc, self.zshrc, self.profile]:
            if config_file.exists():
                backup_file = config_file.with_suffix('.bak.iblu')
                try:
                    with open(config_file, 'r') as src, open(backup_file, 'w') as dst:
                        dst.write(src.read())
                    backups.append(str(backup_file))
                    print(f"✅ Backed up: {config_file} -> {backup_file}")
                except Exception as e:
                    print(f"❌ Failed to backup {config_file}: {e}")
        return backups
    
    def configure_api_keys_interactive(self):
        """Interactive API key configuration"""
        print("🔑 IBLU KALIGPT - API Key Configuration")
        print("=" * 50)
        
        api_keys = {}
        
        # OpenAI
        print("\n🤖 OpenAI API Key:")
        openai_key = input("Enter your OpenAI API key (or press Enter to skip): ").strip()
        if openai_key and openai_key.startswith('sk-'):
            api_keys['OPENAI_API_KEY'] = openai_key
            print("✅ OpenAI key configured")
        elif openai_key:
            print("⚠️  Invalid OpenAI key format (should start with 'sk-')")
        
        # Gemini
        print("\n🧠 Gemini API Key:")
        gemini_key = input("Enter your Gemini API key (or press Enter to skip): ").strip()
        if gemini_key and len(gemini_key) > 20:
            api_keys['GEMINI_API_KEY'] = gemini_key
            print("✅ Gemini key configured")
        elif gemini_key:
            print("⚠️  Invalid Gemini key format")
        
        # Mistral
        print("\n🌊 Mistral API Key:")
        mistral_key = input("Enter your Mistral API key (or press Enter to skip): ").strip()
        if mistral_key and mistral_key.startswith('Mst-'):
            api_keys['MISTRAL_API_KEY'] = mistral_key
            print("✅ Mistral key configured")
        elif mistral_key:
            print("⚠️  Invalid Mistral key format (should start with 'Mst-')")
        
        # HuggingFace
        print("\n🤗 HuggingFace Token:")
        hf_key = input("Enter your HuggingFace token (or press Enter to skip): ").strip()
        if hf_key and hf_key.startswith('hf_'):
            api_keys['HUGGINGFACE_TOKEN'] = hf_key
            print("✅ HuggingFace token configured")
        elif hf_key:
            print("⚠️  Invalid HuggingFace token format (should start with 'hf_')")
        
        return api_keys
    
    def create_environment_file(self, api_keys: Dict[str, str]):
        """Create environment file with API keys"""
        env_content = "# IBLU KALIGPT - API Keys Environment File\n"
        env_content += "# Generated automatically - DO NOT SHARE\n"
        env_content += "# Export these variables globally\n\n"
        
        for key, value in api_keys.items():
            env_content += f"export {key}='{value}'\n"
        
        env_content += "\n# IBLU KALIGPT Configuration\n"
        env_content += "export IBLU_CONFIGURED=true\n"
        env_content += "export IBLU_VERSION='2.3'\n"
        
        try:
            with open(self.env_file, 'w') as f:
                f.write(env_content)
            
            # Set restrictive permissions
            os.chmod(self.env_file, 0o600)
            print(f"✅ Environment file created: {self.env_file}")
            return True
        except Exception as e:
            print(f"❌ Failed to create environment file: {e}")
            return False
    
    def update_shell_configs(self, env_file_path: str):
        """Update shell configuration files to source the environment"""
        source_line = f"\n# IBLU KALIGPT - API Keys\nsource {env_file_path}\n"
        
        updated_files = []
        
        for config_file in [self.bashrc, self.zshrc, self.profile]:
            if config_file.exists():
                try:
                    # Read existing content
                    with open(config_file, 'r') as f:
                        content = f.read()
                    
                    # Check if IBLU config already exists
                    if "# IBLU KALIGPT - API Keys" not in content:
                        # Append the source line
                        with open(config_file, 'a') as f:
                            f.write(source_line)
                        updated_files.append(str(config_file))
                        print(f"✅ Updated: {config_file}")
                    else:
                        print(f"ℹ️  Already configured: {config_file}")
                        
                except Exception as e:
                    print(f"❌ Failed to update {config_file}: {e}")
        
        return updated_files
    
    def create_iblu_config_json(self, api_keys: Dict[str, str]):
        """Create IBLU configuration JSON file"""
        config = {
            "openai_keys": [api_keys.get('OPENAI_API_KEY', '')] if api_keys.get('OPENAI_API_KEY') else [],
            "gemini_keys": [api_keys.get('GEMINI_API_KEY', '')] if api_keys.get('GEMINI_API_KEY') else [],
            "mistral_keys": [api_keys.get('MISTRAL_API_KEY', '')] if api_keys.get('MISTRAL_API_KEY') else [],
            "llama_keys": ["local"],  # Default local configuration
            "huggingface_models": [],
            "current_provider": "openai" if api_keys.get('OPENAI_API_KEY') else "gemini",
            "rephrasing_mode": True,
            "version": "2.3"
        }
        
        config_file = self.config_dir / 'config.json'
        try:
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            # Set restrictive permissions
            os.chmod(config_file, 0o600)
            print(f"✅ IBLU config created: {config_file}")
            return True
        except Exception as e:
            print(f"❌ Failed to create IBLU config: {e}")
            return False
    
    def export_to_system_profile(self, api_keys: Dict[str, str]):
        """Export API keys to system profile for global access"""
        try:
            # Create /etc/environment entry (requires sudo)
            env_entries = []
            for key, value in api_keys.items():
                env_entries.append(f"{key}='{value}'")
            
            if env_entries:
                print("\n🔧 System-wide export (requires sudo):")
                print("Add these lines to /etc/environment:")
                for entry in env_entries:
                    print(f"  {entry}")
                
                # Attempt to add to /etc/environment
                try:
                    with open('/tmp/iblu_env', 'w') as f:
                        for entry in env_entries:
                            f.write(f"{entry}\n")
                    
                    # Use sudo to append to /etc/environment
                    result = subprocess.run([
                        'sudo', 'bash', '-c', 
                        f'cat /tmp/iblu_env >> /etc/environment && rm /tmp/iblu_env'
                    ], capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        print("✅ Added to /etc/environment (system-wide)")
                    else:
                        print("⚠️  Could not add to /etc/environment (manual setup required)")
                        
                except Exception as e:
                    print(f"⚠️  System export failed: {e}")
        
        except Exception as e:
            print(f"❌ System export error: {e}")
    
    def create_global_scripts(self):
        """Create global scripts for API key management"""
        scripts_dir = Path.home() / '.local' / 'bin'
        scripts_dir.mkdir(parents=True, exist_ok=True)
        
        # Create iblu-config script
        script_content = '''#!/bin/bash
# IBLU KALIGPT - Configuration Script

case "$1" in
    "status")
        echo "🔑 IBLU KALIGPT API Key Status"
        echo "OpenAI: ${OPENAI_API_KEY:+✅ Configured}"
        echo "Gemini: ${GEMINI_API_KEY:+✅ Configured}"
        echo "Mistral: ${MISTRAL_API_KEY:+✅ Configured}"
        echo "HuggingFace: ${HUGGINGFACE_TOKEN:+✅ Configured}"
        ;;
    "reload")
        echo "🔄 Reloading IBLU KALIGPT configuration..."
        source ~/.iblu/api_keys.env
        echo "✅ Configuration reloaded"
        ;;
    "help")
        echo "IBLU KALIGPT Configuration Script"
        echo "Usage: iblu-config [status|reload|help]"
        ;;
    *)
        echo "Usage: iblu-config [status|reload|help]"
        ;;
esac
'''
        
        script_file = scripts_dir / 'iblu-config'
        try:
            with open(script_file, 'w') as f:
                f.write(script_content)
            
            # Make executable
            os.chmod(script_file, 0o755)
            
            # Add to PATH if not already there
            scripts_path = str(scripts_dir)
            if scripts_path not in os.environ.get('PATH', ''):
                print(f"📝 Add {scripts_path} to your PATH")
                print(f"  export PATH=\"$PATH:{scripts_path}\"")
            
            print(f"✅ Created script: {script_file}")
            return True
        except Exception as e:
            print(f"❌ Failed to create script: {e}")
            return False
    
    def verify_configuration(self):
        """Verify the configuration is working"""
        print("\n🔍 Verifying configuration...")
        
        # Check environment file
        if self.env_file.exists():
            print("✅ Environment file exists")
        else:
            print("❌ Environment file missing")
        
        # Check shell configs
        for config_file in [self.bashrc, self.zshrc, self.profile]:
            if config_file.exists():
                with open(config_file, 'r') as f:
                    content = f.read()
                    if "IBLU KALIGPT - API Keys" in content:
                        print(f"✅ {config_file.name} configured")
                    else:
                        print(f"❌ {config_file.name} not configured")
        
        # Test environment variables
        print("\n🌍 Testing environment variables:")
        test_script = f"""
source {self.env_file}
echo "OpenAI: ${{OPENAI_API_KEY:+✅}}"
echo "Gemini: ${{GEMINI_API_KEY:+✅}}"
echo "Mistral: ${{MISTRAL_API_KEY:+✅}}"
echo "HuggingFace: ${{HUGGINGFACE_TOKEN:+✅}}"
"""
        
        try:
            result = subprocess.run(['bash', '-c', test_script], capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"❌ Verification failed: {e}")
    
    def setup_complete_configuration(self):
        """Complete setup process"""
        print("🚀 IBLU KALIGPT - Global API Key Setup")
        print("=" * 50)
        
        # Step 1: Backup existing configs
        print("\n📦 Step 1: Backing up existing configurations...")
        self.backup_shell_configs()
        
        # Step 2: Configure API keys
        print("\n🔑 Step 2: Configure your API keys...")
        api_keys = self.configure_api_keys_interactive()
        
        if not api_keys:
            print("❌ No API keys configured. Exiting.")
            return False
        
        # Step 3: Create environment file
        print("\n📁 Step 3: Creating environment file...")
        if not self.create_environment_file(api_keys):
            return False
        
        # Step 4: Create IBLU config
        print("\n⚙️  Step 4: Creating IBLU configuration...")
        if not self.create_iblu_config_json(api_keys):
            return False
        
        # Step 5: Update shell configurations
        print("\n🐚 Step 5: Updating shell configurations...")
        self.update_shell_configs(str(self.env_file))
        
        # Step 6: Create global scripts
        print("\n📜 Step 6: Creating global scripts...")
        self.create_global_scripts()
        
        # Step 7: System-wide export
        print("\n🌍 Step 7: System-wide export...")
        self.export_to_system_profile(api_keys)
        
        # Step 8: Verification
        print("\n🔍 Step 8: Verification...")
        self.verify_configuration()
        
        print("\n✅ Setup complete!")
        print("\n📋 Next steps:")
        print("1. Restart your terminal or run: source ~/.bashrc")
        print("2. Test with: iblu-config status")
        print("3. Start IBLU KALIGPT: python3 iblu_assistant.py")
        
        return True

def main():
    """Main function"""
    manager = GlobalAPIKeyManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "setup":
            manager.setup_complete_configuration()
        elif command == "status":
            manager.verify_configuration()
        elif command == "backup":
            manager.backup_shell_configs()
        else:
            print("Usage: python3 global_api_setup.py [setup|status|backup]")
    else:
        # Default to setup
        manager.setup_complete_configuration()

if __name__ == "__main__":
    main()
