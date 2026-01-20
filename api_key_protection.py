#!/usr/bin/env python3
"""
API Key Protection System for IBLU KALIGPT
Protects API keys from detection and unauthorized access
"""

import os
import json
import base64
import hashlib
import subprocess
import sys
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass

class APIKeyProtector:
    """Advanced API key protection system"""
    
    def __init__(self):
        self.config_dir = Path.home() / '.iblu' / 'secrets'
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.key_file = self.config_dir / 'master.key'
        self.encrypted_file = self.config_dir / 'api_keys.enc'
        self.salt_file = self.config_dir / 'salt.key'
        
    def _get_machine_fingerprint(self):
        """Generate unique machine fingerprint"""
        try:
            # Combine multiple machine identifiers
            import platform
            import uuid
            
            # Get MAC address
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                           for elements in range(0, 2*6, 2)][::-1])
            
            # Get hostname and system info
            hostname = platform.node()
            system = platform.system()
            
            # Create fingerprint
            fingerprint_data = f"{mac}-{hostname}-{system}"
            fingerprint = hashlib.sha256(fingerprint_data.encode()).hexdigest()
            
            return fingerprint[:32]  # Use first 32 chars
        except:
            # Fallback to simple fingerprint
            return hashlib.sha256(os.environ.get('USER', 'user').encode()).hexdigest()[:32]
    
    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive encryption key from password and salt"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    
    def _generate_master_key(self):
        """Generate or load master encryption key"""
        fingerprint = self._get_machine_fingerprint()
        
        if self.key_file.exists():
            try:
                with open(self.key_file, 'rb') as f:
                    stored_fingerprint, encrypted_key = f.read().split(b':')
                
                if stored_fingerprint.decode() == fingerprint:
                    # Decrypt stored key
                    salt = self.salt_file.read_bytes() if self.salt_file.exists() else os.urandom(16)
                    if not self.salt_file.exists():
                        self.salt_file.write_bytes(salt)
                    
                    key = self._derive_key(fingerprint, salt)
                    fernet = Fernet(key)
                    master_key = fernet.decrypt(encrypted_key)
                    return master_key
            except:
                pass
        
        # Generate new master key
        master_key = os.urandom(32)
        salt = os.urandom(16)
        self.salt_file.write_bytes(salt)
        
        # Encrypt and store master key
        key = self._derive_key(fingerprint, salt)
        fernet = Fernet(key)
        encrypted_master_key = fernet.encrypt(master_key)
        
        with open(self.key_file, 'wb') as f:
            f.write(f"{fingerprint}:".encode() + encrypted_master_key)
        
        return master_key
    
    def encrypt_api_keys(self, api_keys: dict) -> bool:
        """Encrypt API keys dictionary"""
        try:
            master_key = self._generate_master_key()
            fernet = Fernet(base64.urlsafe_b64encode(master_key))
            
            # Convert to JSON and encrypt
            json_data = json.dumps(api_keys)
            encrypted_data = fernet.encrypt(json_data.encode())
            
            # Store encrypted data
            with open(self.encrypted_file, 'wb') as f:
                f.write(encrypted_data)
            
            return True
        except Exception as e:
            print(f"❌ Error encrypting API keys: {e}")
            return False
    
    def decrypt_api_keys(self) -> dict:
        """Decrypt API keys dictionary"""
        try:
            if not self.encrypted_file.exists():
                return {}
            
            master_key = self._generate_master_key()
            fernet = Fernet(base64.urlsafe_b64encode(master_key))
            
            # Read and decrypt data
            with open(self.encrypted_file, 'rb') as f:
                encrypted_data = f.read()
            
            decrypted_data = fernet.decrypt(encrypted_data)
            api_keys = json.loads(decrypted_data.decode())
            
            return api_keys
        except Exception as e:
            print(f"❌ Error decrypting API keys: {e}")
            return {}
    
    def obfuscate_string(self, text: str) -> str:
        """Obfuscate string to avoid static analysis"""
        # Simple XOR obfuscation with rotating key
        key = "IBLU_KALIGPT_2024"
        obfuscated = []
        
        for i, char in enumerate(text):
            obfuscated_char = chr(ord(char) ^ ord(key[i % len(key)]))
            obfuscated.append(obfuscated_char)
        
        return ''.join(obfuscated)
    
    def deobfuscate_string(self, obfuscated_text: str) -> str:
        """Deobfuscate string"""
        return self.obfuscate_string(obfuscated_text)  # XOR is symmetric
    
    def generate_fake_keys(self) -> dict:
        """Generate fake API keys for distraction"""
        fake_keys = {
            "openai_keys": [
                "sk-fake-key-for-distraction-only-" + hashlib.md5(os.urandom(16)).hexdigest()[:32],
                "sk-another-fake-key-" + hashlib.md5(os.urandom(16)).hexdigest()[:32]
            ],
            "gemini_keys": [
                "fake-gemini-key-" + hashlib.md5(os.urandom(16)).hexdigest()[:40]
            ],
            "mistral_keys": [
                "fake-mistral-key-" + hashlib.md5(os.urandom(16)).hexdigest()[:32]
            ]
        }
        return fake_keys
    
    def create_secure_config_loader(self):
        """Create a secure configuration loader function"""
        loader_code = '''
def secure_load_config():
    """Securely load configuration with protected API keys"""
    import os
    import json
    from pathlib import Path
    
    # Check for encrypted config first
    encrypted_config = Path.home() / '.iblu' / 'secrets' / 'api_keys.enc'
    
    if encrypted_config.exists():
        # Use the protector to decrypt
        protector = APIKeyProtector()
        return protector.decrypt_api_keys()
    
    # Fallback to regular config
    config_files = ['config.json', '.config.json', '~/.iblu/config.json']
    
    for config_file in config_files:
        try:
            config_path = Path(config_file).expanduser()
            if config_path.exists():
                with open(config_path, 'r') as f:
                    return json.load(f)
        except:
            continue
    
    return {"openai_keys": [], "gemini_keys": [], "mistral_keys": [], "llama_keys": []}
'''
        return loader_code
    
    def hide_from_memory(self, sensitive_data):
        """Attempt to hide sensitive data from memory dumps"""
        try:
            # Overwrite the memory location
            if isinstance(sensitive_data, str):
                # Convert to bytearray and overwrite
                data_array = bytearray(sensitive_data.encode())
                for i in range(len(data_array)):
                    data_array[i] = 0
            elif isinstance(sensitive_data, (bytes, bytearray)):
                for i in range(len(sensitive_data)):
                    sensitive_data[i] = 0
        except:
            pass  # Best effort
    
    def add_runtime_protection(self):
        """Add runtime protection techniques"""
        protection_code = '''
# Runtime protection techniques
import sys
import os

# Hide from process list if possible
if hasattr(os, 'setproctitle'):
    os.setproctitle('[systemd]')  # Disguise as system process

# Anti-debugging techniques
def anti_debug():
    """Simple anti-debugging measures"""
    try:
        # Check for debugger
        import sys
        if hasattr(sys, 'gettrace') and sys.gettrace():
            sys.exit(1)  # Exit if debugger attached
        
        # Check for common debugging tools
        debuggers = ['gdb', 'lldb', 'strace', 'ltrace']
        for debugger in debuggers:
            try:
                if subprocess.run(['pgrep', debugger], capture_output=True).returncode == 0:
                    sys.exit(1)
            except:
                pass
    except:
        pass

# Call anti-debug at startup
anti_debug()
'''
        return protection_code

def main():
    """Interactive setup for API key protection"""
    protector = APIKeyProtector()
    
    print("🔐 IBLU KALIGPT API Key Protection System")
    print("=" * 50)
    
    while True:
        print("\n1. Encrypt existing API keys")
        print("2. Decrypt and view API keys")
        print("3. Generate obfuscated code")
        print("4. Create secure config loader")
        print("5. Add runtime protection")
        print("6. Exit")
        
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == '1':
            # Encrypt existing keys
            config_file = 'config.json'
            if Path(config_file).exists():
                with open(config_file, 'r') as f:
                    api_keys = json.load(f)
                
                if protector.encrypt_api_keys(api_keys):
                    print("✅ API keys encrypted successfully!")
                    print(f"🔒 Encrypted file: {protector.encrypted_file}")
                    print("💡 You can now delete or rename config.json")
                else:
                    print("❌ Failed to encrypt API keys")
            else:
                print("❌ config.json not found")
        
        elif choice == '2':
            # Decrypt keys
            api_keys = protector.decrypt_api_keys()
            if api_keys:
                print("✅ Decrypted API keys:")
                for provider, keys in api_keys.items():
                    print(f"  {provider}: {len(keys)} keys")
            else:
                print("❌ No encrypted API keys found")
        
        elif choice == '3':
            # Generate obfuscated code
            sample_key = "sk-1234567890abcdef1234567890abcdef12345678"
            obfuscated = protector.obfuscate_string(sample_key)
            deobfuscated = protector.deobfuscate_string(obfuscated)
            
            print("🔒 Obfuscation example:")
            print(f"Original: {sample_key}")
            print(f"Obfuscated: {obfuscated}")
            print(f"Deobfuscated: {deobfuscated}")
            print(f"✅ Verification: {sample_key == deobfuscated}")
        
        elif choice == '4':
            # Create secure loader
            loader_code = protector.create_secure_config_loader()
            print("🔐 Secure config loader generated:")
            print(loader_code)
        
        elif choice == '5':
            # Runtime protection
            protection_code = protector.add_runtime_protection()
            print("🛡️ Runtime protection code:")
            print(protection_code)
        
        elif choice == '6':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
