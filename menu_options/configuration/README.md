# ⚙️ Configuration Management

## Description
System configuration and API key management for all AI providers.

## Features
- **API Key Management**: Secure key storage and retrieval
- **Provider Configuration**: Setup OpenAI, Gemini, Local models
- **Connection Testing**: Verify API connectivity
- **Settings Management**: System-wide configuration
- **Environment Setup**: Configure development environment

## Configuration Options

### 1. Install Local Models
- Download and setup local AI models
- Configure model paths
- Optimize performance settings

### 2. Setup API Keys
- OpenAI API key configuration
- Gemini API key configuration
- Custom provider setup

### 3. Configure Providers
- Select active AI providers
- Set default models
- Configure fallback providers

### 4. Test Connections
- Verify API key validity
- Test model connectivity
- Check response times

### 5. Reload API Keys
- Refresh API keys from environment
- Update configuration
- Reset connections

### 6. Delete Models
- Remove unused AI models
- Clean up storage space
- Reset model configuration

### 7. Back to Main Menu
- Return to main interface

## Configuration Files

### config.json
```json
{
  "api_keys": {
    "openai": "your-openai-api-key",
    "gemini": "your-gemini-api-key"
  },
  "providers": {
    "openai": {
      "enabled": true,
      "model": "gpt-4",
      "temperature": 0.7
    },
    "gemini": {
      "enabled": true,
      "model": "gemini-pro",
      "temperature": 0.7
    },
    "local": {
      "enabled": false,
      "model_path": "/path/to/model"
    }
  },
  "settings": {
    "default_provider": "openai",
    "chat_history": true,
    "auto_save": true
  }
}
```

### .env file
```bash
OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key
LOCAL_MODEL_PATH=/path/to/model
```

## Security Notes
- API keys are stored in encrypted format
- Environment variables take precedence
- Keys are never logged or displayed
- Configuration files have restricted permissions

## Implementation
Located in `iblu_assistant.py`:
- `handle_configuration()` - Main configuration menu
- `reload_api_keys_menu()` - API key management
- `install_local_models_menu()` - Model installation
- `test_api_connections()` - Connection testing
