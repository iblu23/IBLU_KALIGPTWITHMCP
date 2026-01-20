#!/usr/bin/env python3
"""
IBLU KALIGPT Menu Options Navigator
Quick access to all menu options and features
"""

import os
import sys
from pathlib import Path

class MenuNavigator:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.menu_options = {
            "1": {
                "name": "💬 Chat Mode",
                "description": "IBLU KALIGPT interactive chat with multiple AI providers",
                "path": "chat_mode/README.md",
                "handler": "handle_iblu_kaligpt"
            },
            "2": {
                "name": "🛠️ Tool Management",
                "description": "Install and manage security tools",
                "path": "tool_management/README.md",
                "handler": "handle_hacking_toys"
            },
            "3": {
                "name": "⚙️ Configuration",
                "description": "System configuration and API key management",
                "path": "configuration/README.md",
                "handler": "handle_configuration"
            },
            "4": {
                "name": "🤖 AI Suggestions",
                "description": "AI-powered text suggestions and autocomplete",
                "path": "ai_suggestions/README.md",
                "handler": "handle_ai_text_suggestions"
            },
            "5": {
                "name": "🎯 Model Management",
                "description": "AI model installation and deletion",
                "path": "model_management/README.md",
                "handler": "list_available_models"
            },
            "6": {
                "name": "🔗 API Management",
                "description": "API key management and testing",
                "path": "api_management/README.md",
                "handler": "reload_api_keys_menu"
            }
        }
    
    def show_main_index(self):
        """Display main menu options index"""
        print("\n" + "="*80)
        print("🧠 IBLU KALIGPT - MENU OPTIONS NAVIGATOR")
        print("="*80)
        
        for key, option in self.menu_options.items():
            print(f"\n{key}. {option['name']}")
            print(f"   📝 {option['description']}")
            print(f"   📁 {option['path']}")
        
        print("\n" + "="*80)
        print("Commands:")
        print("  1-6: View detailed documentation")
        print("  all: Show all documentation")
        print("  tree: Show directory tree")
        print("  config: Show configuration files")
        print("  back: Return to main menu")
        print("  exit: Exit navigator")
        print("="*80)
    
    def show_option_details(self, option_num):
        """Show detailed documentation for a specific option"""
        if option_num not in self.menu_options:
            print(f"❌ Invalid option: {option_num}")
            return
        
        option = self.menu_options[option_num]
        readme_path = self.base_dir / option['path']
        
        print(f"\n📖 {option['name']} - Documentation")
        print("="*60)
        
        if readme_path.exists():
            with open(readme_path, 'r') as f:
                content = f.read()
                print(content)
        else:
            print(f"❌ Documentation not found: {readme_path}")
    
    def show_all_docs(self):
        """Show all documentation files"""
        print("\n📚 ALL DOCUMENTATION")
        print("="*60)
        
        for key, option in self.menu_options.items():
            print(f"\n{'='*20} {option['name']} {'='*20}")
            readme_path = self.base_dir / option['path']
            
            if readme_path.exists():
                with open(readme_path, 'r') as f:
                    content = f.read()
                    print(content)
            else:
                print(f"❌ Documentation not found: {readme_path}")
    
    def show_directory_tree(self):
        """Display directory structure"""
        print("\n🌳 DIRECTORY STRUCTURE")
        print("="*60)
        
        for root, dirs, files in os.walk(self.base_dir):
            level = root.replace(str(self.base_dir), '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                if not file.startswith('.'):
                    print(f"{subindent}{file}")
    
    def show_config_files(self):
        """Show configuration file locations and templates"""
        print("\n⚙️ CONFIGURATION FILES")
        print("="*60)
        
        configs = {
            "Main Config": "../config.json",
            "Environment": "../.env",
            "API Keys": "../api_keys.json",
            "Settings": "../settings.json"
        }
        
        for name, path in configs.items():
            full_path = self.base_dir.parent / path
            status = "✅" if full_path.exists() else "❌"
            print(f"{status} {name}: {path}")
            
            if full_path.exists():
                try:
                    with open(full_path, 'r') as f:
                        content = f.read()[:200]  # First 200 chars
                        print(f"   Preview: {content}...")
                except:
                    print("   (Unable to read file)")
    
    def run(self):
        """Run the navigator interface"""
        print("🧠 Welcome to IBLU KALIGPT Menu Options Navigator!")
        
        while True:
            self.show_main_index()
            choice = input("\n🎯 Choose option (1-6, all, tree, config, back, exit): ").strip().lower()
            
            if choice in ['1', '2', '3', '4', '5', '6']:
                self.show_option_details(choice)
                input("\nPress Enter to continue...")
            elif choice == 'all':
                self.show_all_docs()
                input("\nPress Enter to continue...")
            elif choice == 'tree':
                self.show_directory_tree()
                input("\nPress Enter to continue...")
            elif choice == 'config':
                self.show_config_files()
                input("\nPress Enter to continue...")
            elif choice in ['back', 'menu']:
                print("🔙 Returning to main menu...")
                break
            elif choice in ['exit', 'quit']:
                print("👋 Goodbye!")
                sys.exit(0)
            else:
                print(f"❌ Invalid choice: {choice}")
                input("Press Enter to continue...")

def main():
    """Main entry point"""
    navigator = MenuNavigator()
    navigator.run()

if __name__ == "__main__":
    main()
