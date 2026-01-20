#!/usr/bin/env python3
"""
🧠 Advanced Collaborative AI Deliberation Demo
Showcasing local model deliberation with cloud summarizer system
"""

import time
import sys
import os

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from iblu_assistant import KaliGPTMCPAssistant

def demo_advanced_deliberation():
    """Demonstrate advanced collaborative deliberation system"""
    print("🧠 Advanced Collaborative AI Deliberation Demo")
    print("=" * 50)
    
    # Initialize the assistant
    try:
        assistant = KaliGPTMCPAssistant()
        print("✅ Assistant initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize assistant: {e}")
        return
    
    # Check available models
    print("\n🔍 Checking available models...")
    
    # Check local models
    local_models = []
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models_data = response.json()
            for model in models_data.get('models', []):
                model_name = model.get('name', '').lower()
                if any(keyword in model_name for keyword in ['dolphin', 'llama', 'mistral', 'qwen', 'deepseek']):
                    local_models.append(model.get('name'))
        print(f"🦙 Found {len(local_models)} local models: {', '.join(local_models)}")
    except Exception as e:
        print(f"❌ Error checking local models: {e}")
    
    # Check cloud providers
    cloud_providers = []
    for provider in ['openai', 'gemini', 'mistral']:
        keys = assistant.get_provider_keys(provider.upper() if provider != 'mistral' else 'MISTRAL')
        if keys:
            cloud_providers.append(provider)
    print(f"☁️ Found {len(cloud_providers)} cloud providers: {', '.join(cloud_providers)}")
    
    # Test deliberation if we have enough models
    if len(local_models) >= 3 and len(cloud_providers) >= 1:
        print("\n🚀 Starting advanced deliberation test...")
        test_questions = [
            "How to perform a network security assessment",
            "What are the best practices for password security",
            "How to set up a secure web server"
        ]
        
        for i, question in enumerate(test_questions, 1):
            print(f"\n--- Test Question {i}: {question} ---")
            try:
                response = assistant.advanced_collaborative_deliberation(
                    question, 
                    local_models[:3], 
                    [(cloud_providers[0].upper(), "test_key")]
                )
                print(f"✅ Deliberation {i} completed successfully")
                print(f"Response length: {len(response)} characters")
            except Exception as e:
                print(f"❌ Deliberation {i} failed: {e}")
            
            if i < len(test_questions):
                print("⏳ Waiting 3 seconds before next test...")
                time.sleep(3)
    
    else:
        print(f"\n❌ Insufficient models for deliberation:")
        print(f"   Local models needed: 3+, available: {len(local_models)}")
        print(f"   Cloud providers needed: 1+, available: {len(cloud_providers)}")
        
        if len(local_models) > 0:
            print(f"\n🦙 Available local models:")
            for model in local_models:
                print(f"   • {model}")
        
        if len(cloud_providers) > 0:
            print(f"\n☁️ Available cloud providers:")
            for provider in cloud_providers:
                print(f"   • {provider}")
        
        print(f"\n💡 To enable advanced deliberation:")
        print(f"   1. Install at least 3 local models: /install_llama, /install_dolphin, /install_mistral")
        print(f"   2. Configure at least 1 cloud API key: /config")

def demo_response_length_limits():
    """Demonstrate response length configuration"""
    print("\n📏 Response Length Limits Demo")
    print("=" * 30)
    
    try:
        assistant = KaliGPTMCPAssistant()
        
        print("🔧 Current response configuration:")
        for category, limits in assistant.response_config.items():
            print(f"\n{category.title()}:")
            for limit_type, value in limits.items():
                print(f"  • {limit_type}: {value}")
        
        print("\n💡 Response length limits help control:")
        print("  • Maximum tokens per response type")
        print("  • Timeout duration per operation")
        print("  • Quality vs speed trade-offs")
        
    except Exception as e:
        print(f"❌ Error demonstrating response limits: {e}")

def demo_model_communication():
    """Demonstrate model communication capabilities"""
    print("\n💬 Model Communication Demo")
    print("=" * 30)
    
    try:
        assistant = KaliGPTMCPAssistant()
        
        print("🔧 Communication features:")
        print(f"  • Collaborative mode: {assistant.collaborative_mode}")
        print(f"  • Model communication: {assistant.model_communication_enabled}")
        print(f"  • Rephrasing mode: {assistant.rephrasing_mode}")
        
        print("\n💡 Model communication enables:")
        print("  • Local models to deliberate together")
        print("  • Cloud models to summarize deliberations")
        print("  • Cross-model knowledge sharing")
        print("  • Consensus building")
        
    except Exception as e:
        print(f"❌ Error demonstrating model communication: {e}")

def main():
    """Main demonstration function"""
    print("🧠 Welcome to the Advanced Collaborative AI System Demo!")
    print("This showcases the revolutionary AI deliberation system where:")
    print("  • Local uncensored models discuss topics together")
    print("  • Cloud AI models summarize the deliberation")
    print("  • Cloud models only see the discussion, not the original question")
    print("  • Response length limits control output quality")
    
    time.sleep(2)
    
    # Run demonstrations
    demo_advanced_deliberation()
    demo_response_length_limits()
    demo_model_communication()
    
    print("\n🎉 Advanced Collaborative AI Demo Complete!")
    print("Key features demonstrated:")
    print("  🧠 Multi-model deliberation system")
    print("  📝 Cloud-based summarization")
    print("  📏 Configurable response length limits")
    print("  💫 Enhanced model communication")
    print("  🔧 Quality control mechanisms")
    
    print("\n🚀 Ready to use advanced collaborative AI!")

if __name__ == "__main__":
    main()
