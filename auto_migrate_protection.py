#!/usr/bin/env python3
"""
Auto-Migrate to Permanent API Key Protection
Automatically converts existing config.json to protected format
"""

import json
import sys
from pathlib import Path

def migrate_to_permanent_protection():
    """Migrate existing config to permanent protection"""
    print("🔐 Auto-Migrating to Permanent API Key Protection")
    print("=" * 50)
    
    try:
        # Import secure loader
        from secure_config_loader import SecureConfigLoader, SecureAPIConfig
        print("✅ Secure protection system available")
        
        # Check if config exists
        config_file = Path('config.json')
        if not config_file.exists():
            print("❌ No config.json found - nothing to migrate")
            return False
        
        # Load existing config
        with open(config_file, 'r') as f:
            config_data = json.load(f)
        
        print("✅ Loaded existing config")
        
        # Create secure config
        secure_config = SecureAPIConfig(
            openai_keys=config_data.get('openai_keys', []),
            gemini_keys=config_data.get('gemini_keys', []),
            mistral_keys=config_data.get('mistral_keys', []),
            llama_keys=config_data.get('llama_keys', []),
            gemini_cli_keys=config_data.get('gemini_cli_keys', [])
        )
        
        print("✅ Created secure config")
        
        # Save with protection
        loader = SecureConfigLoader()
        if loader.save_secure_config(secure_config):
            print("✅ Config migrated to permanent protection")
            
            # Backup original config
            backup_file = Path('config.json.backup')
            config_file.rename(backup_file)
            print(f"✅ Original config backed up to {backup_file}")
            
            print("🔐 Migration complete! Your API keys are now permanently protected.")
            return True
        else:
            print("❌ Failed to save protected config")
            return False
            
    except ImportError:
        print("❌ Secure protection system not available")
        return False
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False

if __name__ == "__main__":
    success = migrate_to_permanent_protection()
    sys.exit(0 if success else 1)
