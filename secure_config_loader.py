#!/usr/bin/env python3
"""
Secure Configuration Loader for IBLU KALIGPT
Integrates API key protection with existing system
"""

import os
import json
import hashlib
import base64
from pathlib import Path
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import getpass

class SecureAPIConfig(BaseModel):
    """Secure API configuration with protection"""
    openai_keys: List[str] = Field(default_factory=list, description="OpenAI API keys")
    gemini_keys: List[str] = Field(default_factory=list, description="Gemini API keys")
    mistral_keys: List[str] = Field(default_factory=list, description="Mistral API keys")
    llama_keys: List[str] = Field(default_factory=list, description="Llama API keys")
    gemini_cli_keys: List[str] = Field(default_factory=list, description="Gemini CLI API keys")
    huggingface_models: List[Dict] = Field(default_factory=list, description="Hugging Face models")
    rephrasing_mode: bool = Field(default=False, description="Auto-rephrasing mode")
    
    class Config:
        extra = "allow"

class SecureConfigLoader:
    """Secure configuration loader with multiple protection layers"""
    
    def __init__(self):
        self.config_dir = Path.home() / '.iblu' / 'secrets'
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.encrypted_config = self.config_dir / 'config.enc'
        self.key_derivation_file = self.config_dir / 'key_derivation'
        
    def _get_environment_key(self) -> str:
        """Get environment-based encryption key"""
        # Combine multiple environment factors
        env_factors = [
            os.environ.get('USER', ''),
            os.environ.get('HOME', ''),
            os.environ.get('PATH', '')[:100],  # First 100 chars of PATH
            str(os.getuid()) if hasattr(os, 'getuid') else '',
            str(os.getgid()) if hasattr(os, 'gid') else '',
        ]
        
        env_string = '|'.join(env_factors)
        return hashlib.sha256(env_string.encode()).hexdigest()
    
    def _obfuscate_key(self, key_data: str, method: str = 'xor') -> str:
        """Obfuscate API key using various methods"""
        if method == 'xor':
            # XOR with rotating key
            xor_key = "IBLU_SECURE_2024_WORLD_HACK"
            obfuscated = []
            for i, char in enumerate(key_data):
                obfuscated.append(chr(ord(char) ^ ord(xor_key[i % len(xor_key)])))
            return base64.b64encode(''.join(obfuscated).encode()).decode()
        
        elif method == 'reverse':
            # Simple reversal with base64
            return base64.b64encode(key_data[::-1].encode()).decode()
        
        elif method == 'split':
            # Split and interleave
            half = len(key_data) // 2
            first_half = key_data[:half]
            second_half = key_data[half:]
            interleaved = ''.join(a + b for a, b in zip(first_half, second_half))
            return base64.b64encode(interleaved.encode()).decode()
        
        return key_data
    
    def _deobfuscate_key(self, obfuscated_key: str, method: str = 'xor') -> str:
        """Deobfuscate API key"""
        if method == 'xor':
            xor_key = "IBLU_SECURE_2024_WORLD_HACK"
            decoded = base64.b64decode(obfuscated_key.encode()).decode()
            deobfuscated = []
            for i, char in enumerate(decoded):
                deobfuscated.append(chr(ord(char) ^ ord(xor_key[i % len(xor_key)])))
            return ''.join(deobfuscated)
        
        elif method == 'reverse':
            decoded = base64.b64decode(obfuscated_key.encode()).decode()
            return decoded[::-1]
        
        elif method == 'split':
            decoded = base64.b64decode(obfuscated_key.encode()).decode()
            # De-interleave
            first_half = decoded[::2]
            second_half = decoded[1::2]
            return first_half + second_half
        
        return obfuscated_key
    
    def protect_api_keys(self, config: SecureAPIConfig) -> SecureAPIConfig:
        """Protect API keys by obfuscating them"""
        protected_config = config.copy(deep=True)
        
        # Protect each API key
        for key_type in ['openai_keys', 'gemini_keys', 'mistral_keys', 'llama_keys', 'gemini_cli_keys']:
            keys = getattr(protected_config, key_type, [])
            protected_keys = []
            
            for key in keys:
                if key and not key.startswith('fake-'):
                    # Use different obfuscation methods for variety
                    method = ['xor', 'reverse', 'split'][hash(key) % 3]
                    protected_key = self._obfuscate_key(key, method)
                    protected_keys.append(protected_key)
                else:
                    protected_keys.append(key)
            
            setattr(protected_config, key_type, protected_keys)
        
        return protected_config
    
    def unprotect_api_keys(self, config: SecureAPIConfig) -> SecureAPIConfig:
        """Unprotect API keys by deobfuscating them"""
        unprotected_config = config.copy(deep=True)
        
        # Unprotect each API key
        for key_type in ['openai_keys', 'gemini_keys', 'mistral_keys', 'llama_keys', 'gemini_cli_keys']:
            keys = getattr(unprotected_config, key_type, [])
            unprotected_keys = []
            
            for key in keys:
                if key and not key.startswith('fake-'):
                    # Try different deobfuscation methods
                    for method in ['xor', 'reverse', 'split']:
                        try:
                            unprotected_key = self._deobfuscate_key(key, method)
                            # Validate key format (basic check)
                            if unprotected_key.startswith(('sk-', 'AIza', 'gsk_')):
                                unprotected_keys.append(unprotected_key)
                                break
                        except:
                            continue
                    else:
                        # If none worked, keep original
                        unprotected_keys.append(key)
                else:
                    unprotected_keys.append(key)
            
            setattr(unprotected_config, key_type, unprotected_keys)
        
        return unprotected_config
    
    def load_secure_config(self) -> SecureAPIConfig:
        """Load configuration with security measures"""
        # Try encrypted config first
        if self.encrypted_config.exists():
            try:
                with open(self.encrypted_config, 'rb') as f:
                    encrypted_data = f.read()
                
                # Simple decryption using environment key
                env_key = self._get_environment_key()
                key_hash = hashlib.sha256(env_key.encode()).digest()
                
                # XOR decrypt
                decrypted_data = bytearray()
                for i, byte in enumerate(encrypted_data):
                    decrypted_byte = byte ^ key_hash[i % len(key_hash)]
                    decrypted_data.append(decrypted_byte)
                
                config_data = json.loads(decrypted_data.decode())
                config = SecureAPIConfig(**config_data)
                
                # Unprotect API keys
                return self.unprotect_api_keys(config)
                
            except Exception as e:
                print(f"⚠️ Failed to load encrypted config: {e}")
        
        # Fallback to regular config files
        config_files = [
            'config.json',
            '.config.json',
            Path.home() / '.iblu' / 'config.json',
            Path.home() / '.config' / 'iblu' / 'config.json'
        ]
        
        for config_file in config_files:
            try:
                config_path = Path(config_file)
                if config_path.exists():
                    with open(config_path, 'r') as f:
                        config_data = json.load(f)
                    
                    config = SecureAPIConfig(**config_data)
                    return config
            except Exception as e:
                continue
        
        # Return empty config if nothing found
        return SecureAPIConfig()
    
    def save_secure_config(self, config: SecureAPIConfig) -> bool:
        """Save configuration with protection"""
        try:
            # Protect API keys
            protected_config = self.protect_api_keys(config)
            config_data = protected_config.dict()
            
            # Encrypt using environment key
            env_key = self._get_environment_key()
            key_hash = hashlib.sha256(env_key.encode()).digest()
            
            # Convert to JSON and encrypt
            json_data = json.dumps(config_data, indent=2)
            encrypted_data = bytearray()
            
            for i, byte in enumerate(json_data.encode()):
                encrypted_byte = byte ^ key_hash[i % len(key_hash)]
                encrypted_data.append(encrypted_byte)
            
            # Save encrypted config
            with open(self.encrypted_config, 'wb') as f:
                f.write(encrypted_data)
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to save encrypted config: {e}")
            return False
    
    def add_fake_keys(self, config: SecureAPIConfig) -> SecureAPIConfig:
        """Add fake keys for distraction"""
        fake_config = config.copy(deep=True)
        
        # Add fake keys to each provider
        fake_openai = [
            f"sk-fake-key-{hashlib.md5(os.urandom(8)).hexdigest()[:24]}",
            f"sk-decoy-{hashlib.md5(os.urandom(8)).hexdigest()[:24]}"
        ]
        fake_gemini = [
            f"AIzaFakeKey{hashlib.md5(os.urandom(8)).hexdigest()[:32]}"
        ]
        fake_mistral = [
            f"gsk_fake_{hashlib.md5(os.urandom(8)).hexdigest()[:24]}"
        ]
        
        fake_config.openai_keys.extend(fake_openai)
        fake_config.gemini_keys.extend(fake_gemini)
        fake_config.mistral_keys.extend(fake_mistral)
        
        return fake_config
    
    def migrate_to_secure(self) -> bool:
        """Migrate existing config to secure format"""
        try:
            # Load existing config
            old_config_file = 'config.json'
            if not Path(old_config_file).exists():
                print("❌ No existing config.json found")
                return False
            
            with open(old_config_file, 'r') as f:
                config_data = json.load(f)
            
            config = SecureAPIConfig(**config_data)
            
            # Save in secure format
            if self.save_secure_config(config):
                print("✅ Configuration migrated to secure format")
                print(f"🔒 Secure config saved to: {self.encrypted_config}")
                print("💡 You can now delete or rename config.json")
                
                # Ask if user wants to delete old config
                delete_old = input("Delete old config.json? (y/N): ").strip().lower()
                if delete_old == 'y':
                    Path(old_config_file).unlink()
                    print("🗑️ Old config.json deleted")
                
                return True
            else:
                print("❌ Failed to save secure config")
                return False
                
        except Exception as e:
            print(f"❌ Migration failed: {e}")
            return False

# Integration function for existing codebase
def load_config():
    """Secure configuration loader - drop-in replacement"""
    loader = SecureConfigLoader()
    return loader.load_secure_config()

def save_config(config):
    """Secure configuration saver"""
    loader = SecureConfigLoader()
    return loader.save_secure_config(config)

if __name__ == "__main__":
    """Interactive setup"""
    loader = SecureConfigLoader()
    
    print("🔐 IBLU KALIGPT Secure Configuration")
    print("=" * 40)
    
    while True:
        print("\n1. Migrate existing config to secure format")
        print("2. Load and display current config")
        print("3. Add fake keys for distraction")
        print("4. Test obfuscation/deobfuscation")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            loader.migrate_to_secure()
        
        elif choice == '2':
            config = loader.load_secure_config()
            print("📋 Current Configuration:")
            print(f"OpenAI keys: {len(config.openai_keys)}")
            print(f"Gemini keys: {len(config.gemini_keys)}")
            print(f"Mistral keys: {len(config.mistral_keys)}")
            print(f"Llama keys: {len(config.llama_keys)}")
            print(f"Rephrasing mode: {config.rephrasing_mode}")
        
        elif choice == '3':
            config = loader.load_secure_config()
            config_with_fakes = loader.add_fake_keys(config)
            loader.save_secure_config(config_with_fakes)
            print("✅ Fake keys added for distraction")
        
        elif choice == '4':
            test_key = "sk-1234567890abcdef1234567890abcdef12345678"
            obfuscated = loader._obfuscate_key(test_key)
            deobfuscated = loader._deobfuscate_key(obfuscated)
            print(f"Original: {test_key}")
            print(f"Obfuscated: {obfuscated}")
            print(f"Deobfuscated: {deobfuscated}")
            print(f"✅ Success: {test_key == deobfuscated}")
        
        elif choice == '5':
            break
        
        else:
            print("❌ Invalid choice")
