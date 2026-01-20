def show_complete_visual_menu(self):
        """Display all 34 options in visual style matching current main menu"""
        
        if COLORAMA_AVAILABLE:
            header_width = 115
            
            # Main header
            print(f"\n{Fore.LIGHTCYAN_EX}╔{'═'*header_width}╗{ColoramaStyle.RESET_ALL}")
            print(f"{Fore.LIGHTCYAN_EX}║{ColoramaStyle.RESET_ALL} {ColoramaStyle.BRIGHT}{Fore.WHITE}🧠 COMPLETE MENU OPTIONS (1-34) 🧠{ColoramaStyle.RESET_ALL}{' ' * (header_width - 35)}{Fore.LIGHTCYAN_EX}║{ColoramaStyle.RESET_ALL}")
            print(f"{Fore.LIGHTCYAN_EX}╚{'═'*header_width}╝{ColoramaStyle.RESET_ALL}\n")
            
            # All 34 options in visual style
            options = [
                # MAIN MENU (1-6)
                ("[1] 🧠 IBLU KALIGPT", "Multi-AI Assistant", Fore.GREEN, 
                 "• Auto-rephrasing on refusal", "• Multi-AI querying", "🤖"),
                ("[2] 🎮 HACKING TOYS", "Installation & Management", Fore.BLUE, 
                 "• Install, list, and delete security tools", "", "🔧"),
                ("[3] ⚙️  CONFIGURATION", "Settings", Fore.CYAN, 
                 "• API keys, rephrasing mode", "", "🔑"),
                ("[4] 🤖 AI TEXT SUGGESTIONS", "Autocomplete & Text Generation", Fore.MAGENTA,
                 "• OpenAI GPT suggestions", "• Local models & rule-based", "✨"),
                ("[5] 📋 LIST MODELS", "Show available AI models", Fore.YELLOW, "", "", "🔍"),
                ("[6] 🚪 EXIT", "Leave the program", Fore.RED, "", "", "👋"),
                
                # HACKING TOOLS SUBMENU (7-12)
                ("[7] 📦 Install ALL tools", "Batch installation of 90+ tools", Fore.LIGHTCYAN_EX,
                 "• Quick install all security tools", "• One-click setup", "⚡"),
                ("[8] 🔧 Install ONE-BY-ONE", "Choose specific tools", Fore.LIGHTCYAN_EX,
                 "• Browse numbered list with descriptions", "• Organized by category", "🎯"),
                ("[9] 📋 LIST available tools", "View all installed tools", Fore.LIGHTCYAN_EX,
                 "• Show tools organized by category", "• Display tool descriptions", "📋"),
                ("[10] 🗑️ DELETE tools", "Remove tools from database", Fore.LIGHTCYAN_EX,
                 "• Delete individual tools or all at once", "• Free up disk space", "🗑️"),
                ("[11] 🦙 DELETE local AI models", "Remove local AI models", Fore.LIGHTCYAN_EX,
                 "• Delete Llama, Mistral, or HuggingFace models", "• Free up disk space", "🦙"),
                ("[12] 🔙 Back to MAIN MENU", "Return to main interface", Fore.LIGHTCYAN_EX,
                 "• Return to top level menu", "", "🔙"),
                
                # CONFIGURATION SUBMENU (13-19)
                ("[13] 🤖 Install Local AI Models", "Download and setup local models", Fore.LIGHTGREEN_EX,
                 "• LLaMA models, Mistral, BLOOM", "• Local inference", "🤖"),
                ("[14] 🔑 Setup API Keys", "Configure API keys", Fore.LIGHTGREEN_EX,
                 "• OpenAI API, Gemini API", "• Custom providers, Key encryption", "🔑"),
                ("[15] ⚙️ Configure AI Providers", "Select and configure providers", Fore.LIGHTGREEN_EX,
                 "• Provider selection, Default settings", "• Fallback options", "⚙️"),
                ("[16] 🔍 Test API Connections", "Verify API connectivity", Fore.LIGHTGREEN_EX,
                 "• Connection testing, Latency checks", "• API validation", "🔍"),
                ("[17] 🔄 Reload API Keys", "Refresh API keys", Fore.LIGHTGREEN_EX,
                 "• Key reload, Environment sync", "• Manual entry", "🔄"),
                ("[18] 🗑️ Delete AI Models", "Remove unused AI models", Fore.LIGHTGREEN_EX,
                 "• Model cleanup, Storage management", "• Selective removal", "🗑️"),
                ("[19] 🔙 Back to MAIN MENU", "Return to main interface", Fore.LIGHTGREEN_EX,
                 "• Return to top level menu", "", "🔙"),
                
                # API RELOAD SUBMENU (20-24)
                ("[20] 📊 Check API Keys Status", "View current API configuration", Fore.LIGHTMAGENTA_EX,
                 "• Status display, Key validation", "• Provider status", "📊"),
                ("[21] 🔄 Reload from Environment", "Load API keys from environment", Fore.LIGHTMAGENTA_EX,
                 "• Environment loading", "• Automatic detection", "🔄"),
                ("[22] ✏️ Manual Key Entry", "Enter API keys manually", Fore.LIGHTMAGENTA_EX,
                 "• Manual input, Key validation", "• Secure storage", "✏️"),
                ("[23] 🔗 Test API Connections", "Test all configured endpoints", Fore.LIGHTMAGENTA_EX,
                 "• Connectivity testing", "• Response validation", "🔗"),
                ("[24] 🔙 Back to CONFIGURATION", "Return to configuration menu", Fore.LIGHTMAGENTA_EX,
                 "• Return to configuration options", "", "🔙"),
                
                # AI SUGGESTIONS SUBMENU (25-28)
                ("[25] 🧠 OpenAI GPT Suggestions", "Context-aware suggestions", Fore.LIGHTYELLOW_EX,
                 "• GPT-3.5/4, Context awareness", "• Intelligent completion", "🧠"),
                ("[26] 🏠 Local Model Suggestions", "Offline suggestions", Fore.LIGHTYELLOW_EX,
                 "• Hugging Face, Privacy-focused", "• Offline processing", "🏠"),
                ("[27] ⚡ Rule-based Suggestions", "Fast pattern-based autocomplete", Fore.LIGHTYELLOW_EX,
                 "• Pattern matching, Dictionary lookup", "• Fast response", "⚡"),
                ("[28] 🔙 Back to MAIN MENU", "Return to main interface", Fore.LIGHTYELLOW_EX,
                 "• Return to top level menu", "", "🔙"),
                
                # MODEL DELETION SUBMENU (29-30)
                ("[29] 🦙 Delete LLaMA Models", "Remove LLaMA family models", Fore.LIGHTRED_EX,
                 "• LLaMA 2/3, Storage cleanup", "• Configuration reset", "🦙"),
                ("[30] 🔙 Back to MAIN MENU", "Return to main interface", Fore.LIGHTRED_EX,
                 "• Return to top level menu", "", "🔙"),
                
                # TOOL MANAGEMENT SUBMENU (31-34)
                ("[31] 📋 LIST Tools (All Categories)", "Show all tools with categories", Fore.WHITE,
                 "• Tool catalog, Categories", "• Status checking", "📋"),
                ("[32] 🗑️ DELETE Tools from Database", "Remove tools from database", Fore.WHITE,
                 "• Database cleanup, Selective removal", "• Tool management", "🗑️"),
                ("[33] 🦙 DELETE Local LLaMA Models", "Remove local Llama models", Fore.WHITE,
                 "• Model deletion, Space cleanup", "", "🦙"),
                ("[34] 🔙 Back to MAIN MENU", "Return to main menu", Fore.WHITE,
                 "• Return to top level menu", "", "🔙")
            ]
            
            for i, (option, title, color, desc1, desc2, icon) in enumerate(options):
                # Enhanced top border
                print(f"{color}╔{'═'*header_width}╗{ColoramaStyle.RESET_ALL}")
                
                # Option title line with icon
                title_spacing = header_width - len(option) - len(title) - len(icon) - 8
                print(f"{color}║{ColoramaStyle.RESET_ALL} {ColoramaStyle.BRIGHT}{Back.BLACK}{color}{icon} {Fore.WHITE}{option}{ColoramaStyle.RESET_ALL}: {ColoramaStyle.BRIGHT}{Fore.WHITE}{title}{ColoramaStyle.RESET_ALL}{' ' * title_spacing}{color}║{ColoramaStyle.RESET_ALL}")
                
                # Description lines
                if desc1:
                    desc_spacing = header_width - len(desc1) - 6
                    print(f"{color}║{ColoramaStyle.RESET_ALL} {Fore.LIGHTWHITE_EX}▸{ColoramaStyle.RESET_ALL} {ColoramaStyle.BRIGHT}{Fore.LIGHTBLUE_EX}{desc1}{ColoramaStyle.RESET_ALL}{' ' * desc_spacing}{color}║{ColoramaStyle.RESET_ALL}")
                if desc2:
                    desc_spacing = header_width - len(desc2) - 6
                    print(f"{color}║{ColoramaStyle.RESET_ALL} {Fore.LIGHTWHITE_EX}▸{ColoramaStyle.RESET_ALL} {ColoramaStyle.BRIGHT}{Fore.LIGHTBLUE_EX}{desc2}{ColoramaStyle.RESET_ALL}{' ' * desc_spacing}{color}║{ColoramaStyle.RESET_ALL}")
                
                # Bottom border
                print(f"{color}╚{'═'*header_width}╝{ColoramaStyle.RESET_ALL}")
            
            # Footer
            footer_width = 75
            print(f"{Fore.LIGHTGREEN_EX}┌{'─'*footer_width}┐{ColoramaStyle.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}│{ColoramaStyle.RESET_ALL} {ColoramaStyle.BRIGHT}{Fore.WHITE}💡 Type a number (1-34) to navigate directly{ColoramaStyle.RESET_ALL}{' ' * (footer_width - 40)}{Fore.LIGHTGREEN_EX}│{ColoramaStyle.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}│{ColoramaStyle.RESET_ALL} {ColoramaStyle.BRIGHT}{Fore.YELLOW}🛑 Use 'menu' to return to previous menu{ColoramaStyle.RESET_ALL}{' ' * (footer_width - 38)}{Fore.LIGHTGREEN_EX}│{ColoramaStyle.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}│{ColoramaStyle.RESET_ALL} {ColoramaStyle.BRIGHT}{Fore.CYAN}🔙 Use 'exit'/'quit' to leave program{ColoramaStyle.RESET_ALL}{' ' * (footer_width - 39)}{Fore.LIGHTGREEN_EX}│{ColoramaStyle.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}└{'─'*footer_width}┘{ColoramaStyle.RESET_ALL}\n")
        
        else:
            # Fallback for systems without colorama
            print("\n🧠 COMPLETE MENU OPTIONS (1-34)")
            print("=" * 80)
            
            print("📁 MAIN MENU (1-6)")
            print("[1] 🧠 IBLU KALIGPT: Multi-AI Assistant")
            print("    • Auto-rephrasing on refusal")
            print("    • Multi-AI querying")
            print("[2] 🎮 HACKING TOOLS: Installation & Management")
            print("    • Install, list, and delete security tools")
            print("[3] ⚙️  CONFIGURATION: Settings")
            print("    • API keys, rephrasing mode")
            print("[4] 🤖 AI TEXT SUGGESTIONS: Autocomplete & Text Generation")
            print("    • OpenAI GPT suggestions")
            print("    • Local models & rule-based")
            print("[5] 📋 LIST MODELS: Show available AI models")
            print("[6] 🚪 EXIT: Leave the program")
            
            print("\n📁 HACKING TOOLS SUBMENU (7-12)")
            print("[7] 📦 Install ALL tools: Batch installation of 90+ tools")
            print("[8] 🔧 Install ONE-BY-ONE: Choose specific tools")
            print("[9] 📋 LIST available tools: View all installed tools")
            print("[10] 🗑️ DELETE tools: Remove tools from database")
            print("[11] 🦙 DELETE local AI models: Remove local AI models")
            print("[12] 🔙 Back to MAIN MENU: Return to main interface")
            
            print("\n📁 CONFIGURATION SUBMENU (13-19)")
            print("[13] 🤖 Install Local AI Models: Download and setup local models")
            print("[14] 🔑 Setup API Keys: Configure API keys")
            print("[15] ⚙️ Configure AI Providers: Select and configure providers")
            print("[16] 🔍 Test API Connections: Verify API connectivity")
            print("[17] 🔄 Reload API Keys: Refresh API keys")
            print("[18] 🗑️ Delete AI Models: Remove unused AI models")
            print("[19] 🔙 Back to MAIN MENU: Return to main interface")
            
            print("\n📁 API RELOAD SUBMENU (20-24)")
            print("[20] 📊 Check API Keys Status: View current API configuration")
            print("[21] 🔄 Reload from Environment: Load API keys from environment")
            print("[22] ✏️ Manual Key Entry: Enter API keys manually")
            print("[23] 🔗 Test API Connections: Test all configured endpoints")
            print("[24] 🔙 Back to CONFIGURATION: Return to configuration menu")
            
            print("\n📁 AI SUGGESTIONS SUBMENU (25-28)")
            print("[25] 🧠 OpenAI GPT Suggestions: Context-aware suggestions")
            print("[26] 🏠 Local Model Suggestions: Offline suggestions")
            print("[27] ⚡ Rule-based Suggestions: Fast pattern-based autocomplete")
            print("[28] 🔙 Back to MAIN MENU: Return to main interface")
            
            print("\n📁 MODEL DELETION SUBMENU (29-30)")
            print("[29] 🦙 Delete LLaMA Models: Remove LLaMA family models")
            print("[30] 🔙 Back to MAIN MENU: Return to main interface")
            
            print("\n📁 TOOL MANAGEMENT SUBMENU (31-34)")
            print("[31] 📋 LIST Tools (All Categories): Show all tools with categories")
            print("[32] 🗑️ DELETE Tools from Database: Remove tools from database")
            print("[33] 🦙 DELETE Local LLaMA Models: Remove local Llama models")
            print("[34] 🔙 Back to MAIN MENU: Return to main menu")
            
            print("\n" + "=" * 80)
            print("💡 Type a number (1-34) to navigate directly")
            print("🛑 Use 'menu' to return to previous menu")
            print("🔙 Use 'exit'/'quit' to leave program\n")
