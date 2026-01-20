#!/usr/bin/env python3
"""
Simple progress fix for model installations
"""

import sys
import time
import threading
import subprocess

def simple_model_install(model_name):
    """Simple model installation with clean progress"""
    print(f"\n{'='*60}")
    print(f"📥 Installing {model_name} model...")
    print(f"{'='*60}")
    
    # Start installation in background
    install_thread = threading.Thread(
        target=lambda: subprocess.run(['ollama', 'pull', model_name], 
                                   capture_output=True, text=True, timeout=600)
    )
    install_thread.start()
    
    # Simple spinner that doesn't interfere
    spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    start_time = time.time()
    idx = 0
    
    while install_thread.is_alive():
        elapsed = int(time.time() - start_time)
        sys.stdout.write(f'\r{spinner_chars[idx]} 📦 {model_name} | Elapsed: {elapsed}s')
        sys.stdout.flush()
        idx = (idx + 1) % len(spinner_chars)
        time.sleep(0.2)
    
    install_thread.join()
    
    # Clean up
    sys.stdout.write('\r' + ' ' * 50 + '\r')
    sys.stdout.flush()
    
    # Verify installation
    try:
        verify_cmd = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if model_name in verify_cmd.stdout:
            print(f"✅ {model_name} installed successfully!")
            return True
        else:
            print(f"❌ {model_name} installation failed")
            return False
    except Exception as e:
        print(f"❌ Error verifying {model_name}: {e}")
        return False

if __name__ == "__main__":
    # Test with a small model
    simple_model_install("llama2")
