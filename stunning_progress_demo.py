#!/usr/bin/env python3
"""
🎨 Stunning Rich Progress Bar Demo
Showcase all beautiful themes and effects
"""

import time
import random
from stunning_progress import (
    StunningRichProgressBar, 
    ProgressConfig, 
    ProgressTheme,
    create_progress,
    progress_manager,
    show_stunning_startup
)

def demo_all_themes():
    """Demonstrate all available progress bar themes"""
    print("🎨 Stunning Rich Progress Bar Themes Demo")
    print("=" * 50)
    
    themes = [
        (ProgressTheme.CYBERPUNK, "🔮 Cyberpunk Theme"),
        (ProgressTheme.NEON_PURPLE, "💜 Neon Purple Theme"),
        (ProgressTheme.MATRIX_GREEN, "💚 Matrix Green Theme"),
        (ProgressTheme.FIRE_ORANGE, "🔥 Fire Orange Theme"),
        (ProgressTheme.OCEAN_BLUE, "🌊 Ocean Blue Theme"),
        (ProgressTheme.GALAXY_PURPLE, "🌌 Galaxy Purple Theme"),
        (ProgressTheme.RAINBOW, "🌈 Rainbow Theme"),
        (ProgressTheme.GOLD, "⭐ Gold Theme")
    ]
    
    for theme, description in themes:
        print(f"\n{description}")
        print("-" * 30)
        
        progress = create_progress(
            total=20,
            description=f"Demo {theme.value['name']}",
            theme=theme
        )
        
        progress.start()
        
        for i in range(1, 21):
            progress.set_progress(i, f"Processing step {i}/20...")
            time.sleep(0.1)  # Quick demo
        
        progress.finish(f"✅ {theme.value['name']} Complete!")
        time.sleep(0.5)

def demo_multi_progress():
    """Demonstrate multiple progress bars running simultaneously"""
    print("\n🎯 Multi-Progress Demo")
    print("=" * 30)
    
    configs = [
        ProgressConfig(
            total=15,
            description="🔧 Installing Tools",
            theme=ProgressTheme.FIRE_ORANGE
        ),
        ProgressConfig(
            total=10,
            description="📦 Downloading Models",
            theme=ProgressTheme.OCEAN_BLUE
        ),
        ProgressConfig(
            total=20,
            description="🔗 Configuring System",
            theme=ProgressTheme.MATRIX_GREEN
        )
    ]
    
    # Create progress dashboard
    items = [
        {"name": "Tool Installation", "status": "In Progress", "progress": "60%"},
        {"name": "Model Download", "status": "Downloading", "progress": "40%"},
        {"name": "System Config", "status": "Configuring", "progress": "20%"}
    ]
    
    progress_manager.show_progress_panel("🚀 System Installation", items)

def demo_random_themes():
    """Demonstrate random theme selection"""
    print("\n🎲 Random Theme Demo")
    print("=" * 25)
    
    progress = StunningRichProgressBar()
    
    for i in range(3):
        # Get random theme
        random_theme = progress.get_random_theme()
        progress.set_theme(random_theme)
        
        print(f"\nRandom Theme: {random_theme.value['name']}")
        
        progress.config.total = 10
        progress.config.description = f"Random Demo {i+1}"
        
        progress.start()
        
        for j in range(1, 11):
            progress.set_progress(j, f"Random step {j}/10...")
            time.sleep(0.2)
        
        progress.finish(f"🎲 Random Demo {i+1} Complete!")
        time.sleep(0.5)

def demo_cycling_themes():
    """Demonstrate theme cycling"""
    print("\n🔄 Theme Cycling Demo")
    print("=" * 25)
    
    progress = StunningRichProgressBar()
    
    for i in range(8):
        # Cycle to next theme
        current_theme = progress.next_theme()
        
        progress.config.total = 8
        progress.config.description = f"Cycle {i+1}: {current_theme.value['name']}"
        
        progress.start()
        
        for j in range(1, 9):
            progress.set_progress(j, f"Cycling step {j}/8...")
            time.sleep(0.1)
        
        progress.finish(f"🔄 {current_theme.value['name']} Complete!")
        time.sleep(0.3)

def demo_fallback_mode():
    """Demonstrate fallback mode when Rich is not available"""
    print("\n⚠️  Fallback Mode Demo")
    print("=" * 25)
    
    # Simulate fallback by creating a basic progress bar
    progress = StunningRichProgressBar()
    
    # Force fallback rendering
    progress.console = None
    
    progress.config.total = 10
    progress.config.description = "Fallback Mode Demo"
    
    progress.start()
    
    for i in range(1, 11):
        progress._render_fallback_progress(i)
        time.sleep(0.3)
    
    progress._render_fallback_complete("✅ Fallback Complete!")

def main():
    """Main demonstration function"""
    # Show stunning startup
    show_stunning_startup()
    
    print("\n🎨 Welcome to the Stunning Rich Progress Bar Demo!")
    print("This showcase demonstrates all the beautiful themes and effects.")
    
    time.sleep(2)
    
    # Run all demonstrations
    demo_all_themes()
    demo_multi_progress()
    demo_random_themes()
    demo_cycling_themes()
    demo_fallback_mode()
    
    print("\n🎉 Demo Complete!")
    print("All stunning Rich progress bar themes have been showcased!")
    print("You can now use these beautiful progress bars in your applications!")

if __name__ == "__main__":
    main()
