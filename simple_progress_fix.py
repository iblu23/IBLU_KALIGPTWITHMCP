#!/usr/bin/env python3
"""
Simple fix for progress bar conflicts during model installation
"""

def patch_iblu_assistant():
    """Apply simple progress fix to iblu_assistant.py"""
    
    # Read the current file
    with open('iblu_assistant.py', 'r') as f:
        content = f.read()
    
    # Simple replacement: disable complex progress during model installation
    old_monitor = '''    def monitor_ollama_progress_with_progress(self, model_name: str, progress: InstallationProgress, start_progress: int, end_progress: int) -> bool:
        """Monitor Ollama model download with colorful 3D progress bar and detailed percentage\"'''
    
    new_monitor = '''    def monitor_ollama_progress_with_progress(self, model_name: str, progress: InstallationProgress, start_progress: int, end_progress: int) -> bool:
        """Monitor Ollama model download with simple progress display\"'''
    
    if old_monitor in content:
        content = content.replace(old_monitor, new_monitor)
        
        # Also replace the complex animation with simple one
        old_animation_start = '''        # Enhanced colorful spinners with different themes
        colorful_spinners = ['''
        
        new_animation_start = '''        # Simple spinner for clean display
        spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        
        def animate_download():
            """Simple download animation that doesn't interfere with Ollama output\"''
        
        if old_animation_start in content:
            # Find the end of the old animation function and replace everything
            start_idx = content.find(old_animation_start)
            if start_idx != -1:
                # Find the next function definition
                next_func = content.find('\n    def ', start_idx + 100)
                if next_func != -1:
                    # Replace the entire problematic section
                    simple_animation = '''        # Simple spinner for clean display
        spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        
        def animate_download():
            """Simple download animation that doesn't interfere with Ollama output"""
            idx = 0
            last_status = ""
            
            while not download_complete.is_set():
                current_time = time.time()
                elapsed = int(current_time - start_time)
                
                # Simple status line that won't conflict
                status = f"\\r{spinner_chars[idx]} 📦 {model_name} | Elapsed: {elapsed}s"
                
                # Only update if status changed to reduce flicker
                if status != last_status:
                    sys.stdout.write(status)
                    sys.stdout.flush()
                    last_status = status
                
                idx = (idx + 1) % len(spinner_chars)
                time.sleep(0.2)
            
            # Clean up the line
            sys.stdout.write('\\r' + ' ' * 80 + '\\r')
            sys.stdout.flush()
        
        def check_model_availability():
            """Check if model is available"""
            try:
                url = "http://localhost:11434/api/tags"
                response = requests.get(url, timeout=5)
                
                if response.status_code == 200:
                    models_data = response.json()
                    for model in models_data.get('models', []):
                        if model_name.replace(':8b', '').replace(':latest', '') in model.get('name', '').replace(':8b', '').replace(':latest', ''):
                            download_result['found'] = True
                            download_result['success'] = True
                            download_complete.set()
                            print(f"\\n✅ {model_name} downloaded successfully!")
                            return True
                
                return False
                
            except Exception:
                return False
        
        # Start animation in background
        animation_thread = threading.Thread(target=animate_download)
        animation_thread.daemon = True
        animation_thread.start()
        
        # Monitor download progress
        while time.time() - start_time < max_wait_time:
            if check_model_availability():
                download_complete.set()
                animation_thread.join(timeout=1)
                return True
            
            time.sleep(check_interval)
        
        # Timeout reached
        download_complete.set()
        animation_thread.join(timeout=1)
        print(f"\\n❌ Download timeout for {model_name}")
        return False
'''
                    
                    content = content[start_idx:next_func] + simple_animation + content[next_func:]
        
        # Write the fixed content
        with open('iblu_assistant.py', 'w') as f:
            f.write(content)
        
        print("✅ Applied simple progress fix")
        return True
    
    return False

if __name__ == "__main__":
    patch_iblu_assistant()
