#!/usr/bin/env python3
"""
🎨 Hybrid Rich+Textual Progress Bar Demo
Showcasing the unique fusion of Rich and Textual visual effects
"""

import time
import random
from hybrid_progress import (
    HybridStunningProgressBar, 
    HybridProgressConfig, 
    HybridProgressTheme,
    hybrid_progress_manager,
    create_hybrid_progress,
    run_with_hybrid_progress,
    show_hybrid_startup,
    HybridRichProgressBar,
    HybridTextualProgressBar
)

def demo_all_hybrid_themes():
    """Demonstrate all available hybrid themes"""
    print("🎨 Hybrid Rich+Textual Progress Bar Themes Demo")
    print("=" * 50)
    
    themes = [
        (HybridProgressTheme.CYBERPUNK_FUSION, "🔮 Cyberpunk Fusion"),
        (HybridProgressTheme.NEON_MATRIX, "💚 Neon Matrix"),
        (HybridProgressTheme.FIRE_PLASMA, "🔥 Fire Plasma"),
        (HybridProgressTheme.OCEAN_WAVE, "🌊 Ocean Wave"),
        (HybridProgressTheme.GALAXY_NEBULA, "🌌 Galaxy Nebula"),
        (HybridProgressTheme.RAINBOW_PRISM, "🌈 Rainbow Prism")
    ]
    
    for theme, description in themes:
        print(f"\n{description}")
        print("-" * 30)
        
        progress = create_hybrid_progress(
            total=15,
            description=f"Hybrid Demo {theme.value['name']}",
            theme=theme,
            use_textual=True,
            use_rich=True
        )
        
        progress.start()
        
        for i in range(1, 16):
            progress.set_progress(i, f"Hybrid step {i}/15...")
            time.sleep(0.1)  # Quick demo
        
        progress.finish(f"✅ {theme.value['name']} Complete!")
        time.sleep(0.5)

def demo_hybrid_vs_individual():
    """Demonstrate hybrid vs individual Rich/Textual modes"""
    print("\n🔄 Hybrid vs Individual Modes Demo")
    print("=" * 35)
    
    # Hybrid mode (both Rich and Textual)
    print("\n🎨 HYBRID MODE (Rich + Textual):")
    hybrid_progress = create_hybrid_progress(
        total=10,
        description="Hybrid Rich+Textual Mode",
        theme=HybridProgressTheme.CYBERPUNK_FUSION,
        use_textual=True,
        use_rich=True
    )
    
    hybrid_progress.start()
    for i in range(1, 11):
        hybrid_progress.set_progress(i, f"Hybrid step {i}/10...")
        time.sleep(0.2)
    hybrid_progress.finish("✅ Hybrid Complete!")
    
    # Rich-only mode
    print("\n🎭 RICH-ONLY MODE:")
    rich_progress = create_hybrid_progress(
        total=10,
        description="Rich-Only Mode",
        theme=HybridProgressTheme.NEON_MATRIX,
        use_textual=False,
        use_rich=True
    )
    
    rich_progress.start()
    for i in range(1, 11):
        rich_progress.set_progress(i, f"Rich step {i}/10...")
        time.sleep(0.2)
    rich_progress.finish("✅ Rich Complete!")
    
    # Textual-only mode (if available)
    print("\n📱 TEXTUAL-ONLY MODE:")
    textual_progress = create_hybrid_progress(
        total=10,
        description="Textual-Only Mode",
        theme=HybridProgressTheme.FIRE_PLASMA,
        use_textual=True,
        use_rich=False
    )
    
    textual_progress.start()
    for i in range(1, 11):
        textual_progress.set_progress(i, f"Textual step {i}/10...")
        time.sleep(0.2)
    textual_progress.finish("✅ Textual Complete!")

def demo_theme_cycling():
    """Demonstrate automatic theme cycling"""
    print("\n🎭 Theme Cycling Demo")
    print("=" * 25)
    
    progress = HybridStunningProgressBar()
    
    for i in range(6):
        # Cycle to next theme
        current_theme = progress.next_theme()
        
        progress.config.total = 8
        progress.config.description = f"Cycle {i+1}: {current_theme.value['name']}"
        progress.config.use_textual = True
        progress.config.use_rich = True
        
        progress.start()
        
        for j in range(1, 9):
            progress.set_progress(j, f"Cycling step {j}/8...")
            time.sleep(0.1)
        
        progress.finish(f"🎭 {current_theme.value['name']} Complete!")
        time.sleep(0.3)

def demo_random_themes():
    """Demonstrate random theme selection"""
    print("\n🎲 Random Hybrid Theme Demo")
    print("=" * 30)
    
    progress = HybridStunningProgressBar()
    
    for i in range(3):
        # Get random theme
        random_theme = progress.get_random_theme()
        progress.set_theme(random_theme)
        
        progress.config.total = 12
        progress.config.description = f"Random Demo {i+1}: {random_theme.value['name']}"
        progress.config.use_textual = True
        progress.config.use_rich = True
        
        progress.start()
        
        for j in range(1, 13):
            progress.set_progress(j, f"Random step {j}/12...")
            time.sleep(0.15)
        
        progress.finish(f"🎲 {random_theme.value['name']} Complete!")
        time.sleep(0.4)

def demo_hybrid_dashboard():
    """Demonstrate hybrid dashboard with multiple progress bars"""
    print("\n📊 Hybrid Dashboard Demo")
    print("=" * 25)
    
    # Create multiple hybrid progress configurations
    configs = [
        HybridProgressConfig(
            total=20,
            description="🔧 Installing Tools",
            theme=HybridProgressTheme.FIRE_PLASMA,
            use_textual=True,
            use_rich=True
        ),
        HybridProgressConfig(
            total=15,
            description="📦 Downloading Models",
            theme=HybridProgressTheme.OCEAN_WAVE,
            use_textual=True,
            use_rich=True
        ),
        HybridProgressConfig(
            total=25,
            description="🔗 Configuring System",
            theme=HybridProgressTheme.GALAXY_NEBULA,
            use_textual=True,
            use_rich=True
        )
    ]
    
    # Create hybrid dashboard items
    items = [
        {"name": "Tool Installation", "status": "In Progress", "progress": "60%", "hybrid": True},
        {"name": "Model Download", "status": "Downloading", "progress": "40%", "hybrid": True},
        {"name": "System Config", "status": "Configuring", "progress": "20%", "hybrid": True}
    ]
    
    hybrid_progress_manager.show_hybrid_dashboard("🚀 Hybrid System Installation", items)

def demo_particle_effects():
    """Demonstrate particle effects (conceptual)"""
    print("\n✨ Particle Effects Demo")
    print("=" * 25)
    
    particle_themes = {
        HybridProgressTheme.CYBERPUNK_FUSION: "Digital Rain",
        HybridProgressTheme.NEON_MATRIX: "Matrix Drops",
        HybridProgressTheme.FIRE_PLASMA: "Flames",
        HybridProgressTheme.OCEAN_WAVE: "Waves",
        HybridProgressTheme.GALAXY_NEBULA: "Stars",
        HybridProgressTheme.RAINBOW_PRISM: "Prisms"
    }
    
    for theme, effect in particle_themes.items():
        print(f"\n{theme.value['name']} - {effect} Effect:")
        
        progress = create_hybrid_progress(
            total=10,
            description=f"{effect} Effect Demo",
            theme=theme,
            use_textual=True,
            use_rich=True
        )
        
        progress.start()
        
        for i in range(1, 11):
            progress.set_progress(i, f"{effect} step {i}/10...")
            time.sleep(0.2)
        
        progress.finish(f"✨ {effect} Complete!")
        time.sleep(0.3)

def demo_performance_comparison():
    """Demonstrate performance comparison between modes"""
    print("\n⚡ Performance Comparison Demo")
    print("=" * 30)
    
    modes = [
        ("Hybrid", True, True),
        ("Rich-Only", False, True),
        ("Textual-Only", True, False)
    ]
    
    for mode_name, use_textual, use_rich in modes:
        print(f"\n{mode_name} Mode:")
        
        start_time = time.time()
        
        progress = create_hybrid_progress(
            total=50,
            description=f"{mode_name} Performance Test",
            theme=HybridProgressTheme.CYBERPUNK_FUSION,
            use_textual=use_textual,
            use_rich=use_rich
        )
        
        progress.start()
        
        for i in range(1, 51):
            progress.set_progress(i, f"{mode_name} step {i}/50...")
            time.sleep(0.01)  # Fast demo
        
        progress.finish(f"⚡ {mode_name} Complete!")
        
        elapsed = time.time() - start_time
        print(f"  Time: {elapsed:.2f}s")

def main():
    """Main demonstration function"""
    # Show hybrid startup
    show_hybrid_startup()
    
    print("\n🎨 Welcome to the Hybrid Rich+Textual Progress Bar Demo!")
    print("This showcase demonstrates the unique fusion of Rich and Textual visual effects.")
    
    time.sleep(2)
    
    # Run all demonstrations
    demo_all_hybrid_themes()
    demo_hybrid_vs_individual()
    demo_theme_cycling()
    demo_random_themes()
    demo_hybrid_dashboard()
    demo_particle_effects()
    demo_performance_comparison()
    
    print("\n🎉 Hybrid Demo Complete!")
    print("The unique Rich+Textual fusion creates stunning visual effects!")
    print("You can now use these hybrid progress bars in your applications!")

if __name__ == "__main__":
    main()
