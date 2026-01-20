# 🤖 AI Text Suggestions & Autocomplete

## Description
Advanced AI-powered text suggestions with multiple approaches.

## Features
- **OpenAI GPT Suggestions**: Context-aware text completion
- **Local Model Suggestions**: Offline text generation
- **Rule-based Suggestions**: Pattern-based autocomplete
- **Context Learning**: Adapts to user patterns
- **Multi-language Support**: Various language models

## Suggestion Types

### 1. OpenAI GPT Suggestions
- **Provider**: OpenAI API
- **Models**: GPT-3.5, GPT-4
- **Features**: Context-aware, intelligent completion
- **Use Case**: High-quality suggestions with internet access

### 2. Local Model Suggestions
- **Provider**: Hugging Face Transformers
- **Models**: GPT-2, BLOOM, LLaMA
- **Features**: Offline processing, privacy-focused
- **Use Case**: Secure, local text generation

### 3. Rule-based Suggestions
- **Provider**: Custom patterns and dictionaries
- **Features**: Fast, deterministic results
- **Use Case**: Quick autocomplete, code completion

## Configuration

### OpenAI Configuration
```json
{
  "openai_suggestions": {
    "enabled": true,
    "model": "gpt-3.5-turbo",
    "max_tokens": 50,
    "temperature": 0.7,
    "context_window": 1000
  }
}
```

### Local Model Configuration
```json
{
  "local_suggestions": {
    "enabled": true,
    "model": "gpt2",
    "device": "cpu",
    "max_length": 50,
    "num_return_sequences": 3
  }
}
```

### Rule-based Configuration
```json
{
  "rule_based_suggestions": {
    "enabled": true,
    "patterns": [
      "common_words.txt",
      "technical_terms.txt",
      "commands.txt"
    ],
    "max_suggestions": 5
  }
}
```

## Usage Examples

### Command Line Suggestions
```bash
# Type partial command and get suggestions
nmap -sS <TAB>
# Suggestions: -p, -oN, -oX, -v, -A

# AI-powered context suggestions
curl -X POST <TAB>
# Suggestions: -H, -d, --data, --header, application/json
```

### Code Suggestions
```python
# Python code completion
import requests
r = requests.<TAB>
# Suggestions: get, post, put, delete, request
```

### Natural Language
```text
User: "The best way to secure a server is"
AI: "to implement multiple layers of security, including firewall configuration, regular updates, and access control."
```

## Menu Navigation
1. Select option 4 from main menu
2. Choose suggestion type (1-4):
   - 1: OpenAI GPT Suggestions
   - 2: Local Model Suggestions  
   - 3: Rule-based Suggestions
   - 4: Back to main menu

## Performance Tuning
- **OpenAI**: Adjust temperature for creativity vs accuracy
- **Local Models**: Use GPU for faster inference
- **Rule-based**: Optimize pattern files for speed

## Implementation
Located in `iblu_assistant.py`:
- `handle_ai_text_suggestions()` - Main suggestions menu
- `handle_openai_suggestions()` - OpenAI integration
- `handle_local_model_suggestions()` - Local model integration
- `handle_rule_based_suggestions()` - Pattern-based suggestions
