#!/usr/bin/env python3
"""
🍔 Fat Progress Bar Demo
Showcasing shorter but fatter progress bars with enhanced visual impact
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
    show_hybrid_startup
)

def demo_fat_progress_bars():
    """Demonstrate fat progress bars with different heights"""
    print("🍔 Fat Progress Bar Demo")
    print("=" * 30)
    
    heights = [1, 2, 3, 4, 5]
    
    for height in heights:
        print(f"\n📏 Bar Height: {height} lines")
        
        progress = create_hybrid_progress(
            total=20,
            description=f"🍔 {height}-line Fat Bar",
            theme=HybridProgressTheme.CYBERPUNK_FUSION,
            bar_width=60,  # Shorter but fatter
            bar_height=height,  # Variable height
            particle_effects=True,
            glow_effect=True,
            pulse_animation=True
        )
        
        progress.start()
        
        for i in range(1, 21):
            progress.set_progress(i, f"Fat step {i}/20...")
            time.sleep(0.05)
        
        progress.finish(f"✅ {height}-line fat bar complete!")
        time.sleep(0.3)

def demo_fat_vs_thin_comparison():
    """Compare fat vs thin progress bars"""
    print("\n⚖️ Fat vs Thin Progress Bar Comparison")
    print("=" * 40)
    
    print("\n📏 Thin Bar (1 line, 80 width):")
    progress_thin = create_hybrid_progress(
        total=15,
        description="📏 Thin Progress Bar",
        theme=HybridProgressTheme.NEON_MATRIX,
        bar_width=80,
        bar_height=1,
        particle_effects=True,
        glow_effect=True
    )
    
    progress_thin.start()
    
    for i in range(1, 16):
        progress_thin.set_progress(i, f"Thin step {i}/15...")
        time.sleep(0.08)
    
    progress_thin.finish("✅ Thin bar complete!")
    time.sleep(0.5)
    
    print("\n🍔 Fat Bar (3 lines, 60 width):")
    progress_fat = create_hybrid_progress(
        total=15,
        description="🍔 Fat Progress Bar",
        theme=HybridProgressTheme.FIRE_PLASMA,
        bar_width=60,
        bar_height=3,
        particle_effects=True,
        glow_effect=True
    )
    
    progress_fat.start()
    
    for i in range(1, 16):
        progress_fat.set_progress(i, f"Fat step {i}/15...")
        time.sleep(0.08)
    
    progress_fat.finish("✅ Fat bar complete!")

def demo_fat_bars_with_themes():
    """Demonstrate fat bars with different themes"""
    print("\n🎨 Fat Bars with Different Themes")
    print("=" * 35)
    
    themes = [
        (HybridProgressTheme.CYBERPUNK_FUSION, "🔮 Cyberpunk"),
        (HybridProgressTheme.NEON_MATRIX, "💚 Neon Matrix"),
        (HybridProgressTheme.FIRE_PLASMA, "🔥 Fire Plasma"),
        (HybridProgressTheme.OCEAN_WAVE, "🌊 Ocean Wave"),
        (HybridProgressTheme.GALAXY_NEBULA, "🌌 Galaxy Nebula"),
        (HybridProgressTheme.RAINBOW_PRISM, "🌈 Rainbow Prism")
    ]
    
    for theme, description in themes:
        print(f"\n{description} - Fat Bar:")
        
        progress = create_hybrid_progress(
            total=18,
            description=f"🍔 Fat {description}",
            theme=theme,
            bar_width=60,
            bar_height=3,
            particle_effects=True,
            glow_effect=True,
            pulse_animation=True,
            show_time_left=True
        )
        
        progress.start()
        
        for i in range(1, 19):
            progress.set_progress(i, f"Fat {description} {i}/18...")
            time.sleep(0.06)
        
        progress.finish(f"✨ Fat {description} complete!")
        time.sleep(0.3)

def demo_super_fat_bars():
    """Demonstrate super fat progress bars"""
    print("\n💪 Super Fat Progress Bars")
    print("=" * 30)
    
    super_fat_configs = [
        (4, "💪 Medium Fat"),
        (5, "🍔 Large Fat"),
        (6, "🦋 Extra Fat"),
        (7, "🐋 Super Fat")
    ]
    
    for height, description in super_fat_configs:
        print(f"\n{description} ({height} lines):")
        
        progress = create_hybrid_progress(
            total=12,
            description=description,
            theme=HybridProgressTheme.ELECTRIC_PURPLE,
            bar_width=50,  # Even shorter for super fat effect
            bar_height=height,
            particle_effects=True,
            glow_effect=True,
            pulse_animation=True
        )
        
        progress.start()
        
        for i in range(1, 13):
            progress.set_progress(i, f"{description} {i}/12...")
            time.sleep(0.1)
        
        progress.finish(f"💪 {description} complete!")
        time.sleep(0.4)

def demo_fat_bars_performance():
    """Demonstrate performance with fat bars"""
    print("\n⚡ Fat Bars Performance Demo")
    print("=" * 30)
    
    configs = [
        (1, 80, "Thin Bar"),
        (2, 70, "Slim Fat"),
        (3, 60, "Standard Fat"),
        (4, 50, "Medium Fat"),
        (5, 40, "Large Fat")
    ]
    
    for height, width, description in configs:
        print(f"\n{description} ({height}x{width}):")
        
        start_time = time.time()
        
        progress = create_hybrid_progress(
            total=30,
            description=f"⚡ {description} Performance",
            theme=HybridProgressTheme.GOLDEN_SUNSET,
            bar_width=width,
            bar_height=height,
            particle_effects=True,
            glow_effect=True,
            pulse_animation=True
        )
        
        progress.start()
        
        for i in range(1, 31):
            progress.set_progress(i, f"Perf {description} {i}/30...")
            time.sleep(0.02)
        
        progress.finish(f"⚡ {description} complete!")
        
        elapsed = time.time() - start_time
        print(f"  Time: {elapsed:.2f}s | Size: {height}x{width}")

def demo_fat_bars_with_particles():
    """Demonstrate fat bars with enhanced particle effects"""
    print("\n✨ Fat Bars with Enhanced Particles")
    print("=" * 40)
    
    particle_themes = [
        (HybridProgressTheme.CYBERPUNK_FUSION, "🔮 Digital Rain"),
        (HybridProgressTheme.FIRE_PLASMA, "🔥 Flame Particles"),
        (HybridProgressTheme.GALAXY_NEBULA, "🌌 Star Particles"),
        (HybridProgressTheme.RAINBOW_PRISM, "🌈 Prism Particles")
    ]
    
    for theme, description in particle_themes:
        print(f"\n{description} - Fat Bar:")
        
        progress = create_hybrid_progress(
            total=25,
            description=f"✨ Fat {description}",
            theme=theme,
            bar_width=55,
            bar_height=4,
            particle_effects=True,
            glow_effect=True,
            pulse_animation=True,
            show_time_left=True
        )
        
        progress.start()
        
        for i in range(1, 26):
            progress.set_progress(i, f"Fat {description} {i}/25...")
            time.sleep(0.07)
        
        progress.finish(f"✨ Fat {description} complete!")
        time.sleep(0.3)

def main():
    """Main fat progress bar demonstration"""
    # Show hybrid startup
    show_hybrid_startup()
    
    print("\n🍔 Welcome to the Fat Progress Bar Demo!")
    print("This showcase demonstrates shorter but fatter progress bars")
    print("with enhanced visual impact and substantial appearance!")
    
    time.sleep(2)
    
    # Run all fat bar demonstrations
    demo_fat_progress_bars()
    demo_fat_vs_thin_comparison()
    demo_fat_bars_with_themes()
    demo_super_fat_bars()
    demo_fat_bars_performance()
    demo_fat_bars_with_particles()
    
    print("\n🎉 Fat Progress Bar Demo Complete!")
    print("The fat progress bars feature:")
    print("  🍔 Shorter width (60 characters vs 80-120)")
    print("  💪 Increased height (1-7 lines tall)")
    print("  🎨 Enhanced visual impact")
    print("  ⚡ Better performance with smaller width")
    print("  ✨ All particle effects work with fat bars")
    print("  🌈 Truecolor gradients enhanced")
    print("  💫 Glow and pulse effects more visible")
    print("\nYou can now use these substantial fat progress bars!")

if __name__ == "__main__":
    main()
