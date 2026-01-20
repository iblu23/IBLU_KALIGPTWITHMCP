#!/usr/bin/env python3
"""
IBLU KALIGPT - Complete Options List
All menu options compiled into one comprehensive list
"""

def get_all_options():
    """Return all available options from the entire menu system"""
    
    options = {
        "MAIN_MENU": {
            "1": {
                "name": "🧠 IBLU KALIGPT: Multi-AI Assistant",
                "description": "Interactive chat with multiple AI providers",
                "aliases": ["1", "iblu", "kali", "kaligpt"],
                "features": ["Auto-rephrasing on refusal", "Multi-AI querying"]
            },
            "2": {
                "name": "🎮 HACKING TOYS: Installation & Management",
                "description": "Install, list, and delete security tools",
                "aliases": ["2", "toys", "tools", "install", "hacking", "manage"],
                "features": ["90+ security tools", "Batch installation", "Tool management"]
            },
            "3": {
                "name": "⚙️ CONFIGURATION: Settings",
                "description": "API keys, rephrasing mode",
                "aliases": ["3", "config", "settings"],
                "features": ["API key management", "Provider configuration"]
            },
            "4": {
                "name": "🤖 AI TEXT SUGGESTIONS: Autocomplete & Text Generation",
                "description": "OpenAI GPT suggestions, Local models & rule-based",
                "aliases": ["4", "suggestions", "autocomplete", "ai", "text"],
                "features": ["OpenAI GPT", "Local models", "Rule-based"]
            },
            "5": {
                "name": "📋 LIST MODELS: Show available AI models",
                "description": "Display all available AI models",
                "aliases": ["5", "models", "list"],
                "features": ["Model listing", "Status checking"]
            },
            "6": {
                "name": "🚪 EXIT: Leave the program",
                "description": "Exit IBLU KALIGPT",
                "aliases": ["6", "exit", "quit"],
                "features": ["Clean exit", "Save state"]
            }
        },
        
        "HACKING_TOOLS_SUBMENU": {
            "1": {
                "name": "📦 Install ALL tools at once",
                "description": "Install 90+ security tools in batch",
                "features": ["Batch installation", "All categories", "One-click setup"]
            },
            "2": {
                "name": "🔧 Install ONE-BY-ONE",
                "description": "Choose and install tools individually",
                "features": ["Selective installation", "Tool descriptions", "Custom setup"]
            },
            "3": {
                "name": "📋 LIST TOOLS",
                "description": "View all available tools with categories",
                "features": ["Tool catalog", "Categories", "Installation status"]
            },
            "4": {
                "name": "🗑️ DELETE TOOLS",
                "description": "Remove tools from database",
                "features": ["Tool removal", "Database cleanup", "Selective deletion"]
            },
            "5": {
                "name": "🦙 DELETE MODELS",
                "description": "Remove local AI models",
                "features": ["Model deletion", "Space cleanup", "Cache clearing"]
            },
            "6": {
                "name": "🔙 Back to main menu",
                "description": "Return to main interface",
                "features": ["Menu navigation", "Return to top"]
            }
        },
        
        "CONFIGURATION_SUBMENU": {
            "1": {
                "name": "🤖 Install Local Models",
                "description": "Download and setup local AI models",
                "features": ["LLaMA models", "Mistral", "BLOOM", "Local inference"]
            },
            "2": {
                "name": "🔑 Setup API Keys",
                "description": "Configure OpenAI, Gemini, and custom API keys",
                "features": ["OpenAI API", "Gemini API", "Custom providers", "Key encryption"]
            },
            "3": {
                "name": "⚙️ Configure Providers",
                "description": "Select and configure AI providers",
                "features": ["Provider selection", "Default settings", "Fallback options"]
            },
            "4": {
                "name": "🔍 Test Connections",
                "description": "Verify API connectivity and response times",
                "features": ["Connection testing", "Latency checks", "API validation"]
            },
            "5": {
                "name": "🔄 Reload API Keys",
                "description": "Refresh API keys from environment or manual entry",
                "features": ["Key reload", "Environment sync", "Manual entry"]
            },
            "6": {
                "name": "🗑️ Delete Models",
                "description": "Remove unused AI models",
                "features": ["Model cleanup", "Storage management", "Selective removal"]
            },
            "7": {
                "name": "🔙 Back to main menu",
                "description": "Return to main interface",
                "features": ["Menu navigation"]
            }
        },
        
        "API_RELOAD_SUBMENU": {
            "1": {
                "name": "📊 Check API Keys Status",
                "description": "View current API key configuration",
                "features": ["Status display", "Key validation", "Provider status"]
            },
            "2": {
                "name": "🔄 Reload from Environment",
                "description": "Load API keys from environment variables",
                "features": ["Environment loading", "Automatic detection", "Variable parsing"]
            },
            "3": {
                "name": "✏️ Manual Key Entry",
                "description": "Enter API keys manually",
                "features": ["Manual input", "Key validation", "Secure storage"]
            },
            "4": {
                "name": "🔗 Test API Connections",
                "description": "Test all configured API endpoints",
                "features": ["Connectivity testing", "Response validation", "Performance checks"]
            },
            "5": {
                "name": "🔙 Back to Configuration Menu",
                "description": "Return to configuration options",
                "features": ["Menu navigation"]
            }
        },
        
        "AI_SUGGESTIONS_SUBMENU": {
            "1": {
                "name": "🧠 OpenAI GPT Suggestions",
                "description": "Context-aware suggestions using OpenAI models",
                "features": ["GPT-3.5/4", "Context awareness", "Intelligent completion"]
            },
            "2": {
                "name": "🏠 Local Model Suggestions",
                "description": "Offline suggestions using local models",
                "features": ["Hugging Face", "Privacy-focused", "Offline processing"]
            },
            "3": {
                "name": "⚡ Rule-based Suggestions",
                "description": "Fast pattern-based autocomplete",
                "features": ["Pattern matching", "Dictionary lookup", "Fast response"]
            },
            "4": {
                "name": "🔙 Back to main menu",
                "description": "Return to main interface",
                "features": ["Menu navigation"]
            }
        },
        
        "MODEL_DELETION_SUBMENU": {
            "1": {
                "name": "🦙 Delete Llama Models",
                "description": "Remove LLaMA family models",
                "features": ["LLaMA 2/3", "Storage cleanup", "Configuration reset"]
            },
            "2": {
                "name": "🔙 Back to main menu",
                "description": "Return to main interface",
                "features": ["Menu navigation"]
            }
        },
        
        "TOOL_MANAGEMENT_SUBMENU": {
            "1": {
                "name": "📋 LIST TOOLS",
                "description": "Show all available tools with categories",
                "features": ["Tool catalog", "Categories", "Status checking"]
            },
            "2": {
                "name": "🗑️ DELETE TOOLS",
                "description": "Remove tools from database",
                "features": ["Database cleanup", "Selective removal", "Tool management"]
            },
            "3": {
                "name": "🦙 DELETE MODELS",
                "description": "Remove local Llama models",
                "features": ["Model deletion", "Space cleanup"]
            },
            "4": {
                "name": "🔙 BACK TO MENU",
                "description": "Return to main menu",
                "features": ["Menu navigation"]
            }
        }
    }
    
    return options

def display_all_options():
    """Display all options in a comprehensive list"""
    options = get_all_options()
    
    print("🧠 IBLU KALIGPT - COMPLETE OPTIONS LIST")
    print("=" * 80)
    
    for menu_name, menu_options in options.items():
        print(f"\n📁 {menu_name.replace('_', ' ').title()}")
        print("-" * 60)
        
        for key, option in menu_options.items():
            print(f"  {key}. {option['name']}")
            print(f"     📝 {option['description']}")
            if 'aliases' in option:
                print(f"     🏷️  Aliases: {', '.join(option['aliases'])}")
            if 'features' in option:
                print(f"     ⭐ Features: {', '.join(option['features'])}")
            print()

def search_options(query):
    """Search options by name or description"""
    options = get_all_options()
    results = []
    query_lower = query.lower()
    
    for menu_name, menu_options in options.items():
        for key, option in menu_options.items():
            if (query_lower in option['name'].lower() or 
                query_lower in option['description'].lower() or
                any(query_lower in feature.lower() for feature in option.get('features', []))):
                results.append({
                    'menu': menu_name,
                    'key': key,
                    'option': option
                })
    
    return results

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        results = search_options(query)
        
        if results:
            print(f"🔍 Search Results for '{query}':")
            print("=" * 60)
            for result in results:
                print(f"📁 {result['menu']} -> {result['key']}. {result['option']['name']}")
                print(f"   📝 {result['option']['description']}")
                print()
        else:
            print(f"❌ No results found for '{query}'")
    else:
        display_all_options()
