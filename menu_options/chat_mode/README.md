# 💬 Chat Mode - IBLU KALIGPT

## Description
Interactive chat interface with multiple AI providers support.

## Features
- **Multi-AI Support**: OpenAI, Gemini, Local Models
- **Chat History**: Persistent conversation history
- **Provider Switching**: Dynamic AI provider changes
- **Rich Interface**: Colorful and interactive terminal UI

## Configuration
```json
{
  "providers": {
    "openai": {
      "api_key": "your-openai-key",
      "model": "gpt-4"
    },
    "gemini": {
      "api_key": "your-gemini-key",
      "model": "gemini-pro"
    },
    "local": {
      "model_path": "/path/to/local/model"
    }
  }
}
```

## Usage
1. Select option 1 from main menu
2. Type your questions directly
3. Type 'menu' to return to main menu
4. Type 'exit' to quit

## Commands
- `menu` - Return to main menu
- `exit` / `quit` - Exit program
- `switch provider` - Change AI provider
- `history` - View chat history

## Implementation
Located in `iblu_assistant.py`:
- `handle_iblu_kaligpt()` - Main chat handler
- `show_main_menu()` - Menu display
- `handle_menu_choice()` - Menu navigation
