#!/usr/bin/env python3
"""
IBLU KALIGPT - Unified Numbered Options List (1-34)
All menu options in sequential numbering format
"""

def get_unified_options_list():
    """Return all options in unified 1-34 numbering format"""
    
    unified_options = """
📁 MAIN MENU (1–6)

1. 🧠 IBLU KALIGPT: Multi-AI Assistant
   📝 Interactive chat with multiple AI providers
   🏷️  Aliases: 1, iblu, kali, kaligpt
   ⭐ Features: Auto-rephrasing on refusal, Multi-AI querying

2. 🎮 HACKING TOOLS: Installation & Management
   📝 Install, list, and delete security tools
   🏷️  Aliases: 2, toys, tools, install, hacking, manage
   ⭐ Features: 90+ security tools, Batch installation, Tool management

3. ⚙️ CONFIGURATION: Settings
   📝 API keys, rephrasing mode
   🏷️  Aliases: 3, config, settings
   ⭐ Features: API key management, Provider configuration

4. 🤖 AI TEXT SUGGESTIONS: Autocomplete & Text Generation
   📝 OpenAI GPT suggestions, Local models & rule-based
   🏷️  Aliases: 4, suggestions, autocomplete, ai, text
   ⭐ Features: OpenAI GPT, Local models, Rule-based

5. 📋 LIST MODELS: Show available AI models
   📝 Display all available AI models
   🏷️  Aliases: 5, models, list
   ⭐ Features: Model listing, Status checking

6. 🚪 EXIT: Leave the program
   📝 Exit IBLU KALIGPT
   🏷️  Aliases: 6, exit, quit
   ⭐ Features: Clean exit, Save state

📁 HACKING TOOLS SUBMENU (7–12)

7. 📦 Install ALL tools at once
   📝 Install 90+ security tools in batch
   ⭐ Features: Batch installation, All categories, One-click setup

8. 🔧 Install tools ONE-BY-ONE
   📝 Choose and install tools individually
   ⭐ Features: Selective installation, Tool descriptions, Custom setup

9. 📋 LIST available tools
   📝 View all available tools with categories
   ⭐ Features: Tool catalog, Categories, Installation status

10. 🗑️ DELETE tools
    📝 Remove tools from database
    ⭐ Features: Tool removal, Database cleanup, Selective deletion

11. 🦙 DELETE local AI models
    📝 Remove local AI models
    ⭐ Features: Model deletion, Space cleanup, Cache clearing

12. 🔙 Back to MAIN MENU
    📝 Return to main interface
    ⭐ Features: Menu navigation, Return to top

📁 CONFIGURATION SUBMENU (13–19)

13. 🤖 Install Local AI Models
    📝 Download and setup local AI models
    ⭐ Features: LLaMA models, Mistral, BLOOM, Local inference

14. 🔑 Setup API Keys
    📝 Configure OpenAI, Gemini, and custom API keys
    ⭐ Features: OpenAI API, Gemini API, Custom providers, Key encryption

15. ⚙️ Configure AI Providers
    📝 Select and configure AI providers
    ⭐ Features: Provider selection, Default settings, Fallback options

16. 🔍 Test API Connections
    📝 Verify API connectivity and response times
    ⭐ Features: Connection testing, Latency checks, API validation

17. 🔄 Reload API Keys
    📝 Refresh API keys from environment or manual entry
    ⭐ Features: Key reload, Environment sync, Manual entry

18. 🗑️ Delete AI Models
    📝 Remove unused AI models
    ⭐ Features: Model cleanup, Storage management, Selective removal

19. 🔙 Back to MAIN MENU
    📝 Return to main interface
    ⭐ Features: Menu navigation

📁 API RELOAD SUBMENU (20–24)

20. 📊 Check API Keys Status
    📝 View current API key configuration
    ⭐ Features: Status display, Key validation, Provider status

21. 🔄 Reload API Keys from Environment
    📝 Load API keys from environment variables
    ⭐ Features: Environment loading, Automatic detection, Variable parsing

22. ✏️ Manual API Key Entry
    📝 Enter API keys manually
    ⭐ Features: Manual input, Key validation, Secure storage

23. 🔗 Test API Connections
    📝 Test all configured API endpoints
    ⭐ Features: Connectivity testing, Response validation, Performance checks

24. 🔙 Back to CONFIGURATION MENU
    📝 Return to configuration options
    ⭐ Features: Menu navigation

📁 AI SUGGESTIONS SUBMENU (25–28)

25. 🧠 OpenAI GPT Suggestions
    📝 Context-aware suggestions using OpenAI models
    ⭐ Features: GPT-3.5/4, Context awareness, Intelligent completion

26. 🏠 Local Model Suggestions
    📝 Offline suggestions using local models
    ⭐ Features: Hugging Face, Privacy-focused, Offline processing

27. ⚡ Rule-based Suggestions
    📝 Fast pattern-based autocomplete
    ⭐ Features: Pattern matching, Dictionary lookup, Fast response

28. 🔙 Back to MAIN MENU
    📝 Return to main interface
    ⭐ Features: Menu navigation

📁 MODEL DELETION SUBMENU (29–30)

29. 🦙 Delete LLaMA Models
    📝 Remove LLaMA family models
    ⭐ Features: LLaMA 2/3, Storage cleanup, Configuration reset

30. 🔙 Back to MAIN MENU
    📝 Return to main interface
    ⭐ Features: Menu navigation

📁 TOOL MANAGEMENT SUBMENU (31–34)

31. 📋 LIST Tools (All Categories)
    📝 Show all available tools with categories
    ⭐ Features: Tool catalog, Categories, Status checking

32. 🗑️ DELETE Tools from Database
    📝 Remove tools from database
    ⭐ Features: Database cleanup, Selective removal, Tool management

33. 🦙 DELETE Local LLaMA Models
    📝 Remove local Llama models
    ⭐ Features: Model deletion, Space cleanup

34. 🔙 Back to MAIN MENU
    📝 Return to main menu
    ⭐ Features: Menu navigation
"""
    
    return unified_options

def show_unified_options():
    """Display the unified numbered options list"""
    print("🧠 IBLU KALIGPT - UNIFIED OPTIONS LIST (1-34)")
    print("=" * 80)
    print(get_unified_options_list())
    print("=" * 80)
    print(f"📊 Total Options: 34")
    print(f"🎯 Quick Access: Type any number 1-34 to navigate directly")
    print(f"🔙 Navigation: Use 'menu' to return to main menu")

def get_option_by_number(number):
    """Get option details by unified number"""
    options_map = {
        1: {"name": "🧠 IBLU KALIGPT", "handler": "handle_iblu_kaligpt", "menu": "MAIN"},
        2: {"name": "🎮 HACKING TOOLS", "handler": "handle_hacking_toys", "menu": "MAIN"},
        3: {"name": "⚙️ CONFIGURATION", "handler": "handle_configuration", "menu": "MAIN"},
        4: {"name": "🤖 AI TEXT SUGGESTIONS", "handler": "handle_ai_text_suggestions", "menu": "MAIN"},
        5: {"name": "📋 LIST MODELS", "handler": "list_available_models", "menu": "MAIN"},
        6: {"name": "🚪 EXIT", "handler": "exit_program", "menu": "MAIN"},
        7: {"name": "📦 Install ALL tools", "handler": "install_all_tools", "menu": "HACKING"},
        8: {"name": "🔧 Install ONE-BY-ONE", "handler": "install_tools_one_by_one", "menu": "HACKING"},
        9: {"name": "📋 LIST available tools", "handler": "show_tools_list", "menu": "HACKING"},
        10: {"name": "🗑️ DELETE tools", "handler": "delete_tools", "menu": "HACKING"},
        11: {"name": "🦙 DELETE local AI models", "handler": "delete_models", "menu": "HACKING"},
        12: {"name": "🔙 Back to MAIN MENU", "handler": "show_main_menu", "menu": "HACKING"},
        13: {"name": "🤖 Install Local AI Models", "handler": "install_local_models", "menu": "CONFIG"},
        14: {"name": "🔑 Setup API Keys", "handler": "setup_api_keys", "menu": "CONFIG"},
        15: {"name": "⚙️ Configure AI Providers", "handler": "configure_providers", "menu": "CONFIG"},
        16: {"name": "🔍 Test API Connections", "handler": "test_connections", "menu": "CONFIG"},
        17: {"name": "🔄 Reload API Keys", "handler": "reload_api_keys", "menu": "CONFIG"},
        18: {"name": "🗑️ Delete AI Models", "handler": "delete_models", "menu": "CONFIG"},
        19: {"name": "🔙 Back to MAIN MENU", "handler": "show_main_menu", "menu": "CONFIG"},
        20: {"name": "📊 Check API Keys Status", "handler": "check_api_status", "menu": "API"},
        21: {"name": "🔄 Reload API Keys from Environment", "handler": "reload_from_env", "menu": "API"},
        22: {"name": "✏️ Manual API Key Entry", "handler": "manual_key_entry", "menu": "API"},
        23: {"name": "🔗 Test API Connections", "handler": "test_api_connections", "menu": "API"},
        24: {"name": "🔙 Back to CONFIGURATION MENU", "handler": "handle_configuration", "menu": "API"},
        25: {"name": "🧠 OpenAI GPT Suggestions", "handler": "openai_suggestions", "menu": "AI"},
        26: {"name": "🏠 Local Model Suggestions", "handler": "local_suggestions", "menu": "AI"},
        27: {"name": "⚡ Rule-based Suggestions", "handler": "rule_suggestions", "menu": "AI"},
        28: {"name": "🔙 Back to MAIN MENU", "handler": "show_main_menu", "menu": "AI"},
        29: {"name": "🦙 Delete LLaMA Models", "handler": "delete_llama_models", "menu": "MODEL"},
        30: {"name": "🔙 Back to MAIN MENU", "handler": "show_main_menu", "menu": "MODEL"},
        31: {"name": "📋 LIST Tools (All Categories)", "handler": "list_tools", "menu": "TOOL"},
        32: {"name": "🗑️ DELETE Tools from Database", "handler": "delete_tools_db", "menu": "TOOL"},
        33: {"name": "🦙 DELETE Local LLaMA Models", "handler": "delete_llama_models", "menu": "TOOL"},
        34: {"name": "🔙 Back to MAIN MENU", "handler": "show_main_menu", "menu": "TOOL"}
    }
    
    return options_map.get(number, None)

def search_unified_options(query):
    """Search options by name or description"""
    results = []
    query_lower = query.lower()
    
    for num in range(1, 35):
        option = get_option_by_number(num)
        if option and query_lower in option['name'].lower():
            results.append({"number": num, "option": option})
    
    return results

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            num = int(sys.argv[1])
            option = get_option_by_number(num)
            if option:
                print(f"🎯 Option {num}: {option['name']}")
                print(f"📁 Menu: {option['menu']}")
                print(f"🔧 Handler: {option['handler']}")
            else:
                print(f"❌ Invalid option number: {num}")
        else:
            query = ' '.join(sys.argv[1:])
            results = search_unified_options(query)
            if results:
                print(f"🔍 Search Results for '{query}':")
                for result in results:
                    print(f"  {result['number']}. {result['option']['name']}")
            else:
                print(f"❌ No results found for '{query}'")
    else:
        show_unified_options()
