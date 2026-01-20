# System Prompt Update - Local vs API Models

## Overview
Updated the IBLU KALIGPT assistant to use different system prompts based on whether a model is running locally (uncensored) or via API (comprehensive/summary focused).

## Changes Made

### 1. New Function: `get_system_prompt_for_provider()`
**Location:** `iblu_assistant.py` lines 2157-2215

This function determines which system prompt to use based on:
- **Provider type** (LLAMA, GEMINI, MISTRAL, OPENAI, etc.)
- **API key value** (checks if it's "local" or localhost URL)

**Logic:**
```python
is_local_model = (
    (provider == Provider.LLAMA and api_key == "local") or
    (provider == Provider.GEMINI and (api_key.startswith("http://localhost") or api_key.startswith("127.0.0.1"))) or
    (provider == Provider.MISTRAL and api_key == "local")
)
```

### 2. System Prompt Types

#### Local Models (Uncensored)
- Uses the original `SYSTEM_PROMPT` 
- Full uncensored responses
- Direct technical guidance
- No content restrictions
- Focused on educational cybersecurity content

#### API Models (Comprehensive Summary & Expansion)
- Uses new comprehensive analysis prompt
- Focuses on:
  - Detailed summaries with expanded insights
  - Multiple perspectives and approaches
  - Comprehensive coverage of topics
  - Educational framing with professional standards
  - Expansion of local model conclusions
  - Risk assessments and best practices

### 3. Updated Functions

All API calling functions now use `get_system_prompt_for_provider()`:

#### Core Functions:
- `call_single_provider()` - Updated to use `actual_system_prompt`
- All provider-specific API calls (OpenAI, Gemini, Mistral, Llama, Gemini CLI)

#### Collaborative Mode Functions:
- `collaborative_model_response()` - Local discussion and cloud expansion
- `stack_model_responses()` - Stacked model analysis
- `model_chat_mode()` - Inter-model conversations

### 4. Behavior

**Single Model Mode:**
- Local models (Llama with "local" key): Uncensored, direct responses
- API models (OpenAI, Gemini, Mistral with API keys): Comprehensive summaries

**Collaborative Mode:**
- **Phase 1**: Local models discuss using uncensored prompt
- **Phase 2**: API models expand local conclusions with comprehensive analysis
- **Phase 3**: Final synthesis combines both approaches

## Benefits

1. **Local Privacy**: Uncensored local models for sensitive topics
2. **API Compliance**: API models provide professional, comprehensive responses
3. **Best of Both**: Collaborative mode combines uncensored local analysis with comprehensive API expansion
4. **Flexible**: Automatically adapts based on model type and configuration

## Testing

To test the changes:

1. **Local Model (Llama)**: Should give direct, uncensored responses
   ```
   config.json: "llama_keys": ["local"]
   ```

2. **API Model (Gemini/OpenAI/Mistral)**: Should give comprehensive summaries
   ```
   config.json: "gemini_keys": ["AIza..."]
   ```

3. **Collaborative Mode**: Should show local discussion + API expansion
   - Requires both local and API models configured
   - Local models discuss first (uncensored)
   - API models expand with comprehensive analysis

## Configuration

No changes needed to `config.json`. The system automatically detects:
- Local models by checking if `api_key == "local"`
- Local Gemini by checking if URL starts with `http://localhost` or `127.0.0.1`
- All other cases are treated as API models

## Notes

- The original `SYSTEM_PROMPT` is preserved for local models
- API models get a new prompt focused on comprehensive analysis and expansion
- Custom system prompts passed to `call_single_provider()` override the automatic selection
- All collaborative mode functions properly use provider-specific prompts
