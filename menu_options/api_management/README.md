# 🔗 API Management

## Description
Comprehensive API key management, connection testing, and service monitoring.

## Features
- **API Key Management**: Secure storage and retrieval
- **Connection Testing**: Verify API connectivity
- **Status Monitoring**: Real-time service status
- **Key Rotation**: Secure key updates
- **Environment Sync**: Sync with system environment

## Supported APIs

### OpenAI API
- **Endpoint**: https://api.openai.com/v1
- **Models**: GPT-3.5, GPT-4, DALL-E
- **Rate Limits**: 3,000 RPM, 200,000 TPM
- **Authentication**: Bearer token

### Gemini API
- **Endpoint**: https://generativelanguage.googleapis.com/v1
- **Models**: Gemini Pro, Gemini Pro Vision
- **Rate Limits**: 60 QPM
- **Authentication**: API key

### Custom APIs
- **Endpoint**: Configurable
- **Authentication**: Bearer token, API key, custom
- **Rate Limits**: Configurable
- **Headers**: Customizable

## API Key Management

### 1. Check API Keys Status
```bash
# View current API key status
python iblu_assistant.py
# Select: 3 → 5 → 1

# Status output example
✅ OpenAI: Configured (gpt-4)
✅ Gemini: Configured (gemini-pro)
❌ Custom: Not configured
```

### 2. Reload from Environment
```bash
# Reload API keys from environment variables
export OPENAI_API_KEY="your-new-key"
export GEMINI_API_KEY="your-new-key"
python iblu_assistant.py
# Select: 3 → 5 → 2
```

### 3. Manual Key Entry
```bash
# Enter API keys manually
python iblu_assistant.py
# Select: 3 → 5 → 3

# Follow prompts for each service
```

### 4. Test API Connections
```bash
# Test all configured APIs
python iblu_assistant.py
# Select: 3 → 5 → 4

# Test results
✅ OpenAI: Connected (Latency: 245ms)
✅ Gemini: Connected (Latency: 189ms)
❌ Custom: Connection failed
```

## Configuration Files

### config.json
```json
{
  "api_keys": {
    "openai": "sk-...encrypted...",
    "gemini": "AI...encrypted...",
    "custom": null
  },
  "api_endpoints": {
    "openai": "https://api.openai.com/v1",
    "gemini": "https://generativelanguage.googleapis.com/v1",
    "custom": "https://api.example.com/v1"
  },
  "api_settings": {
    "timeout": 30,
    "retries": 3,
    "rate_limit": true
  }
}
```

### .env file
```bash
# Environment variables (take precedence)
OPENAI_API_KEY=sk-your-openai-key
GEMINI_API_KEY=AIza-your-gemini-key
CUSTOM_API_KEY=your-custom-key
OPENAI_BASE_URL=https://api.openai.com/v1
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1
```

## Security Features

### Key Encryption
- API keys are encrypted at rest
- AES-256 encryption for storage
- Memory-only decryption during use
- Automatic key rotation support

### Access Control
- File permissions: 600 (user only)
- Environment variable protection
- No keys in logs or output
- Secure key transmission

## Connection Testing

### Test Parameters
```json
{
  "test_settings": {
    "timeout": 10,
    "retry_attempts": 3,
    "test_prompt": "Hello, test connection",
    "expected_response_length": 10
  }
}
```

### Health Checks
- **Endpoint Availability**: Check if API is reachable
- **Authentication**: Verify key validity
- **Rate Limits**: Check quota availability
- **Latency**: Measure response times

## Error Handling

### Common Errors
- **Invalid API Key**: Key expired or incorrect
- **Rate Limit Exceeded**: Too many requests
- **Network Error**: Connection issues
- **Service Unavailable**: API downtime

### Troubleshooting
```bash
# Check API key validity
curl -H "Authorization: Bearer $OPENAI_API_KEY" \
     https://api.openai.com/v1/models

# Test Gemini API
curl "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=$GEMINI_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"contents":[{"parts":[{"text":"Hello"}]}]}'
```

## Menu Navigation
1. Select option 3 from main menu (Configuration)
2. Select option 5 (Reload API Keys)
3. Choose action (1-5):
   - 1: Check API Keys Status
   - 2: Reload from Environment
   - 3: Manual Key Entry
   - 4: Test API Connections
   - 5: Back to Configuration Menu

## Implementation
Located in `iblu_assistant.py`:
- `reload_api_keys_menu()` - Main API management
- `test_api_connections()` - Connection testing
- `handle_configuration()` - Configuration integration
- API key encryption/decryption functions
