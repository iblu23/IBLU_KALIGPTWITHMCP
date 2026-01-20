# 🎯 Model Management

## Description
AI model installation, configuration, and deletion management.

## Features
- **Model Installation**: Download and setup AI models
- **Model Deletion**: Remove unused models
- **Status Monitoring**: Track model availability
- **Storage Management**: Monitor disk usage
- **Version Control**: Manage model versions

## Supported Models

### OpenAI Models
- **GPT-3.5 Turbo**: Fast, cost-effective
- **GPT-4**: Advanced reasoning
- **GPT-4 Turbo**: Latest GPT-4 version
- **Text-Davinci-003**: Legacy model

### Gemini Models
- **Gemini Pro**: Google's advanced model
- **Gemini Pro Vision**: Multimodal capabilities
- **Gemini Ultra**: Most capable model

### Local Models
- **LLaMA 2/3**: Meta's open models
- **Mistral**: Efficient local models
- **BLOOM**: Large open model
- **GPT-2**: Classic local model

## Installation Options

### 1. Install Local Models
```bash
# Interactive installation
python iblu_assistant.py
# Select: 3 → 1 → Choose model

# Direct installation
python -c "from iblu_assistant import IBLUAssistant; IBLUAssistant().install_local_models_menu()"
```

### Available Local Models
1. **LLaMA 7B** - 4GB storage, fast inference
2. **LLaMA 13B** - 8GB storage, balanced performance
3. **LLaMA 70B** - 40GB storage, high performance
4. **Mistral 7B** - 4GB storage, efficient
5. **BLOOM 7B** - 14GB storage, multilingual

## Deletion Options

### 1. Delete Llama Models
- Remove LLaMA family models
- Free up storage space
- Clean up configuration files

### 2. Delete Gemini Models
- Remove Gemini local instances
- Clear cached data
- Reset configuration

### 3. Delete All Models
- Complete model cleanup
- Remove all AI models
- Reset to defaults

## Storage Requirements

### Model Sizes
| Model | Size | RAM Usage | Storage |
|-------|------|-----------|---------|
| GPT-2 Small | 500MB | 1GB | 500MB |
| LLaMA 7B | 13GB | 8GB | 13GB |
| LLaMA 13B | 25GB | 16GB | 25GB |
| LLaMA 70B | 140GB | 80GB | 140GB |
| Mistral 7B | 14GB | 8GB | 14GB |

### Storage Locations
- **Linux**: `~/.cache/huggingface/`
- **Models**: `/models/` or `~/.local/models/`
- **Cache**: `/tmp/model_cache/`

## Configuration

### Model Configuration File
```json
{
  "models": {
    "local": {
      "enabled": true,
      "model_path": "~/.local/models/llama-7b",
      "device": "auto",
      "dtype": "float16"
    },
    "openai": {
      "enabled": true,
      "model": "gpt-4",
      "api_key": "configured"
    },
    "gemini": {
      "enabled": true,
      "model": "gemini-pro",
      "api_key": "configured"
    }
  },
  "settings": {
    "default_model": "openai",
    "fallback_enabled": true,
    "cache_models": true
  }
}
```

## Performance Optimization

### GPU Acceleration
```bash
# Check GPU availability
python -c "import torch; print(torch.cuda.is_available())"

# Enable GPU in config
{
  "device": "cuda",
  "n_gpu_layers": 35
}
```

### Memory Optimization
- Use quantization for large models
- Enable model streaming
- Configure cache size limits

## Menu Navigation
1. Select option 3 from main menu (Configuration)
2. Choose option 1 (Install Local Models)
3. Select model type and confirm installation

For deletion:
1. Select option 3 from main menu
2. Choose option 6 (Delete Models)
3. Select models to delete

## Implementation
Located in `iblu_assistant.py`:
- `handle_delete_models()` - Model deletion menu
- `install_local_models_menu()` - Model installation
- `list_available_models()` - Model status display
- `handle_configuration()` - Configuration management
