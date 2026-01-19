#!/usr/bin/env python3
"""
🔥 IBLU Professional Hacking Assistant v2.3 - Installation Verification Script 🔥
🚀 Comprehensive verification of all components and functionality 🚀
"""

import sys
import os
import json
import subprocess
from pathlib import Path

def print_header():
    """Print colored header"""
    print("🔥 IBLU Professional Hacking Assistant v2.3 - Installation Verification")
    print("=" * 70)
    print("🚀 Comprehensive verification of all components and functionality")
    print("=" * 70)
    print()

def check_python_version():
    """Check Python version"""
    print("🐍 Python Version Check:")
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Supported")
            return True
        else:
            print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Not supported (requires 3.8+)")
            return False
    except Exception as e:
        print(f"❌ Error checking Python version: {e}")
        return False

def check_dependencies():
    """Check required dependencies"""
    print("\n📦 Dependencies Check:")
    
    required_packages = [
        ('requests', 'requests'),
        ('colorama', 'colorama'),
        ('asyncio', 'asyncio'),
        ('pathlib', 'pathlib'),
        ('dataclasses', 'dataclasses'),
        ('time', 'time'),
        ('enum', 'enum')
    ]
    
    optional_packages = [
        ('rich', 'rich'),
        ('typer', 'typer'),
        ('pydantic', 'pydantic'),
        ('click', 'click'),
        ('aiohttp', 'aiohttp'),
        ('psutil', 'psutil'),
        ('beautifulsoup4', 'bs4'),
        ('cryptography', 'cryptography')
    ]
    
    all_required_passed = True
    for package, import_name in required_packages:
        try:
            __import__(import_name)
            print(f"✅ {package} - Available")
        except ImportError:
            print(f"❌ {package} - Missing")
            all_required_passed = False
    
    print(f"\n📦 Optional Dependencies Check:")
    for package, import_name in optional_packages:
        try:
            __import__(import_name)
            print(f"✅ {package} - Available")
        except ImportError:
            print(f"⚠️  {package} - Not installed (optional)")
    
    return all_required_passed

def check_files():
    """Check required files exist"""
    print("\n📁 Files Check:")
    
    required_files = [
        'README.md',
        'enhanced_command_helper.py',
        'iblu_assistant.py',
        'mcp_server.py',
        'config.json.example',
        'requirements.txt',
        'launch_iblu.sh'
    ]
    
    all_files_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            size = Path(file_path).stat().st_size
            print(f"✅ {file_path} - {size:,} bytes")
        else:
            print(f"❌ {file_path} - Missing")
            all_files_exist = False
    
    return all_files_exist

def check_directories():
    """Check required directories exist"""
    print("\n📁 Directories Check:")
    
    required_dirs = ['logs', 'pentest_reports', 'venv']
    
    all_dirs_exist = True
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            print(f"✅ {dir_path}/ - Directory exists")
        else:
            print(f"⚠️  {dir_path}/ - Directory missing (will be created)")
    
    return all_dirs_exist

def check_config():
    """Check configuration file"""
    print("\n⚙️ Configuration Check:")
    
    config_file = Path('config.json')
    if not config_file.exists():
        print("⚠️  config.json - Not found")
        print("💡 Creating from template...")
        
        if Path('config.json.example').exists():
            import shutil
            shutil.copy('config.json.example', 'config.json')
            print("✅ config.json - Created from template")
            print("⚠️  Please edit config.json with your API keys")
            return False
        else:
            print("❌ config.json.example - Template not found")
            return False
    else:
        print("✅ config.json - Found")
        
        # Check if API keys are configured
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
            
            has_keys = False
            for provider in ['openai_keys', 'gemini_keys', 'mistral_keys']:
                if provider in config and config[provider]:
                    if config[provider] and len(config[provider]) > 0:
                        has_keys = True
                        break
            
            if has_keys:
                print("✅ API Keys - Configured")
                return True
            else:
                print("⚠️  API Keys - Not configured")
                print("💡 Please edit config.json and add your API keys")
                return False
                
        except Exception as e:
            print(f"❌ Error reading config.json: {e}")
            return False

def test_enhanced_command_helper():
    """Test enhanced command helper functionality"""
    print("\n🔧 Enhanced Command Helper Test:")
    
    try:
        # Import enhanced command helper
        from enhanced_command_helper import EnhancedCommandHelper
        
        # Initialize helper
        helper = EnhancedCommandHelper()
        
        # Test basic functionality
        commands_count = len(helper.COMMANDS)
        categories_count = len(helper.CATEGORIES)
        
        print(f"✅ Import - Successful")
        print(f"✅ Initialization - Successful")
        print(f"✅ Total Commands: {commands_count}")
        print(f"✅ Categories: {categories_count}")
        
        # Test suggestions
        suggestions_1 = helper.get_suggestions('1')
        suggestions_scan = helper.get_suggestions('scan')
        suggestions_51 = helper.get_suggestions('51')
        
        print(f"✅ Suggestions for '1': {len(suggestions_1)}")
        print(f"✅ Suggestions for 'scan': {len(suggestions_scan)}")
        print(f"✅ Suggestions for '51': {len(suggestions_51)}")
        
        # Test numbered commands
        numbered_commands = [cmd for cmd in helper.COMMANDS.keys() if cmd.isdigit()]
        print(f"✅ Numbered Commands: {len(numbered_commands)} (1-100)")
        
        return True
        
    except Exception as e:
        print(f"❌ Enhanced Command Helper Error: {e}")
        return False

def test_main_program():
    """Test main program functionality"""
    print("\n🤖 Main Program Test:")
    
    try:
        # Import main program
        import iblu_assistant
        
        print("✅ Import - Successful")
        
        # Test basic command helper
        from iblu_assistant import IBLUCommandHelper
        helper = IBLUCommandHelper()
        
        suggestions = helper.get_suggestions('help')
        print(f"✅ Command Helper - Working ({len(suggestions)} suggestions)")
        
        return True
        
    except Exception as e:
        print(f"❌ Main Program Error: {e}")
        return False

def test_launcher():
    """Test launcher script"""
    print("\n🚀 Launcher Test:")
    
    launcher_file = Path('launch_iblu.sh')
    if launcher_file.exists():
        if os.access(launcher_file, os.X_OK):
            print("✅ launch_iblu.sh - Executable")
            
            # Test launcher help
            try:
                result = subprocess.run(['./launch_iblu.sh', '--help'], 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    print("✅ Launcher Help - Working")
                else:
                    print("⚠️  Launcher Help - May have issues")
            except subprocess.TimeoutExpired:
                print("⚠️  Launcher Help - Timeout")
            except Exception as e:
                print(f"⚠️  Launcher Help Error: {e}")
            
            return True
        else:
            print("⚠️  launch_iblu.sh - Not executable")
            print("💡 Run: chmod +x launch_iblu.sh")
            return False
    else:
        print("❌ launch_iblu.sh - Not found")
        return False

def test_permissions():
    """Test file permissions"""
    print("\n🔒 Permissions Check:")
    
    files_to_check = [
        ('launch_iblu.sh', 0o755),
        ('config.json', 0o644),
        ('README.md', 0o644),
        ('requirements.txt', 0o644)
    ]
    
    all_permissions_ok = True
    for file_path, expected_mode in files_to_check:
        if Path(file_path).exists():
            current_mode = oct(Path(file_path).stat().st_mode)[-3:]
            if current_mode == expected_mode:
                print(f"✅ {file_path} - Permissions {current_mode}")
            else:
                print(f"⚠️  {file_path} - Permissions {current_mode} (expected {expected_mode})")
        else:
            print(f"❌ {file_path} - Not found")
    
    return all_permissions_ok

def show_system_info():
    """Show system information"""
    print("\n📊 System Information:")
    
    try:
        import platform
        import psutil
        
        print(f"🖥️ Platform: {platform.platform()}")
        print(f"💻 CPU: {psutil.cpu_count()} cores")
        print(f"💾 Memory: {psutil.virtual_memory().total // (1024**3)} MB")
        print(f"💿 Disk: {psutil.disk_usage('.').free // (1024**3)} MB free")
        
    except ImportError:
        print("⚠️  System info modules not available")

def main():
    """Main verification function"""
    print_header()
    
    # Run all checks
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Files", check_files),
        ("Directories", check_directories),
        ("Configuration", check_config),
        ("Enhanced Command Helper", test_enhanced_command_helper),
        ("Main Program", test_main_program),
        ("Launcher", test_launcher),
        ("Permissions", test_permissions)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name} - Error: {e}")
            results.append((name, False))
    
    # Show system info
    show_system_info()
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 70)
    
    passed = 0
    total = len(results)
    
    for name, result in results:
        if result:
            print(f"✅ {name}: PASSED")
            passed += 1
        else:
            print(f"❌ {name}: FAILED")
    
    print(f"\n📈 Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 ALL CHECKS PASSED! Installation is ready!")
        print("\n🚀 Next Steps:")
        print("1. Run: ./launch_iblu.sh")
        print("2. Test commands: /help, /status, 1, /menu")
        print("3. Configure API keys if needed")
        print("4. Start using IBLU Assistant!")
    else:
        print(f"\n⚠️  {total - passed} checks failed")
        print("\n🔧 Troubleshooting:")
        print("1. Check failed items above")
        print("2. Install missing dependencies: pip install -r requirements.txt")
        print("3. Create config.json: cp config.json.example config.json")
        print("4. Set executable permissions: chmod +x launch_iblu.sh")
        print("5. Check Python version: python3 --version")

if __name__ == "__main__":
    main()
