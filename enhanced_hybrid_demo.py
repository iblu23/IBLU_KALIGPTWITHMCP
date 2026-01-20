#!/usr/bin/env python3
"""
🎨 Enhanced Hybrid Rich+Textual Progress Bar Demo
Showcasing bigger, longer, more interactive progress bars with particle effects
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

def demo_enhanced_features():
    """Demonstrate all enhanced features"""
    print("🎨 Enhanced Hybrid Progress Bar Features Demo")
    print("=" * 55)
    
    print("\n✨ Features to demonstrate:")
    print("  🔥 Bigger progress bars (80-120 characters)")
    print("  ⏱️ Enhanced time tracking (elapsed + ETA)")
    print("  🎆 Particle effects that change with progress")
    print("  💫 Glow effects and pulse animations")
    print("  🎮 Interactive controls (placeholder)")
    print("  🌈 Enhanced visual styling")
    
    time.sleep(2)

def demo_bigger_progress_bars():
    """Demonstrate bigger progress bars"""
    print("\n📏 Bigger Progress Bars Demo")
    print("=" * 30)
    
    sizes = [60, 80, 100, 120]
    
    for size in sizes:
        print(f"\nBar Width: {size} characters")
        
        progress = create_hybrid_progress(
            total=20,
            description=f"📏 {size}-character Progress Bar",
            theme=HybridProgressTheme.CYBERPUNK_FUSION,
            bar_width=size,
            particle_effects=True,
            show_time_left=True,
            glow_effect=True,
            pulse_animation=True
        )
        
        progress.start()
        
        for i in range(1, 21):
            progress.set_progress(i, f"Processing step {i}/20...")
            time.sleep(0.1)
        
        progress.finish(f"✅ {size}-char bar complete!")
        time.sleep(0.5)

def demo_enhanced_time_tracking():
    """Demonstrate enhanced time tracking"""
    print("\n⏱️ Enhanced Time Tracking Demo")
    print("=" * 35)
    
    progress = create_hybrid_progress(
        total=30,
        description="⏱️ Enhanced Time Tracking Demo",
        theme=HybridProgressTheme.NEON_MATRIX,
        show_time=True,
        show_time_left=True,
        particle_effects=True,
        glow_effect=True
    )
    
    progress.start()
    
    for i in range(1, 31):
        progress.set_progress(i, f"Time tracking step {i}/30...")
        # Variable delay to make ETA calculation interesting
        delay = random.uniform(0.05, 0.2)
        time.sleep(delay)
    
    progress.finish("⏱️ Time tracking complete!")
    time.sleep(1)

def demo_particle_effects():
    """Demonstrate particle effects"""
    print("\n🎆 Particle Effects Demo")
    print("=" * 25)
    
    themes = [
        HybridProgressTheme.FIRE_PLASMA,
        HybridProgressTheme.OCEAN_WAVE,
        HybridProgressTheme.GALAXY_NEBULA,
        HybridProgressTheme.RAINBOW_PRISM
    ]
    
    for theme in themes:
        print(f"\n{theme.value['name']} Particles:")
        
        progress = create_hybrid_progress(
            total=25,
            description=f"🎆 {theme.value['name']} Particle Effects",
            theme=theme,
            particle_effects=True,
            glow_effect=True,
            pulse_animation=True
        )
        
        progress.start()
        
        for i in range(1, 26):
            progress.set_progress(i, f"Particle step {i}/25...")
            time.sleep(0.08)
        
        progress.finish(f"🎆 {theme.value['name']} particles complete!")
        time.sleep(0.5)

def demo_glow_and_pulse_effects():
    """Demonstrate glow and pulse effects"""
    print("\n💫 Glow and Pulse Effects Demo")
    print("=" * 35)
    
    # Demo with glow effects
    print("\n✨ Glow Effects:")
    progress = create_hybrid_progress(
        total=20,
        description="✨ Glow Effects Demo",
        theme=HybridProgressTheme.CYBERPUNK_FUSION,
        glow_effect=True,
        pulse_animation=False,
        particle_effects=True
    )
    
    progress.start()
    
    for i in range(1, 21):
        progress.set_progress(i, f"Glow step {i}/20...")
        time.sleep(0.1)
    
    progress.finish("✨ Glow effects complete!")
    
    # Demo with pulse effects
    print("\n💗 Pulse Effects:")
    progress = create_hybrid_progress(
        total=20,
        description="💗 Pulse Effects Demo",
        theme=HybridProgressTheme.OCEAN_WAVE,
        glow_effect=False,
        pulse_animation=True,
        particle_effects=True
    )
    
    progress.start()
    
    for i in range(1, 21):
        progress.set_progress(i, f"Pulse step {i}/20...")
        time.sleep(0.1)
    
    progress.finish("💗 Pulse effects complete!")
    
    # Demo with both effects
    print("\n🌟 Combined Glow + Pulse Effects:")
    progress = create_hybrid_progress(
        total=20,
        description="🌟 Combined Effects Demo",
        theme=HybridProgressTheme.GALAXY_NEBULA,
        glow_effect=True,
        pulse_animation=True,
        particle_effects=True
    )
    
    progress.start()
    
    for i in range(1, 21):
        progress.set_progress(i, f"Combined step {i}/20...")
        time.sleep(0.1)
    
    progress.finish("🌟 Combined effects complete!")

def demo_interactive_features():
    """Demonstrate interactive features"""
    print("\n🎮 Interactive Features Demo")
    print("=" * 30)
    
    progress = create_hybrid_progress(
        total=15,
        description="🎮 Interactive Features Demo",
        theme=HybridProgressTheme.RAINBOW_PRISM,
        interactive=True,
        particle_effects=True,
        glow_effect=True,
        show_time_left=True
    )
    
    progress.start()
    
    print("💡 Interactive controls would be available:")
    print("  [Space] Pause/Resume")
    print("  [R] Restart")
    print("  [Q] Quit")
    print("  [Arrow Keys] Adjust speed")
    
    for i in range(1, 16):
        progress.set_progress(i, f"Interactive step {i}/15...")
        time.sleep(0.15)
    
    progress.finish("🎮 Interactive demo complete!")

def demo_all_enhanced_themes():
    """Demonstrate all themes with enhanced features"""
    print("\n🌈 All Enhanced Themes Demo")
    print("=" * 30)
    
    themes = [
        (HybridProgressTheme.CYBERPUNK_FUSION, "🔮 Cyberpunk Fusion"),
        (HybridProgressTheme.NEON_MATRIX, "💚 Neon Matrix"),
        (HybridProgressTheme.FIRE_PLASMA, "🔥 Fire Plasma"),
        (HybridProgressTheme.OCEAN_WAVE, "🌊 Ocean Wave"),
        (HybridProgressTheme.GALAXY_NEBULA, "🌌 Galaxy Nebula"),
        (HybridProgressTheme.RAINBOW_PRISM, "🌈 Rainbow Prism")
    ]
    
    for theme, description in themes:
        print(f"\n{description} - Enhanced:")
        
        progress = create_hybrid_progress(
            total=18,
            description=f"Enhanced {theme.value['name']}",
            theme=theme,
            bar_width=90,
            particle_effects=True,
            show_time_left=True,
            interactive=True,
            glow_effect=True,
            pulse_animation=True
        )
        
        progress.start()
        
        for i in range(1, 19):
            progress.set_progress(i, f"Enhanced {theme.value['name']} step {i}/18...")
            time.sleep(0.08)
        
        progress.finish(f"✨ Enhanced {theme.value['name']} complete!")
        time.sleep(0.4)

def demo_performance_comparison():
    """Demonstrate performance with enhanced features"""
    print("\n⚡ Enhanced Performance Comparison")
    print("=" * 38)
    
    configs = [
        ("Basic", False, False, False, 60),
        ("Enhanced", True, True, True, 80),
        ("Ultra Enhanced", True, True, True, 100)
    ]
    
    for name, particles, glow, pulse, bar_width in configs:
        print(f"\n{name} Configuration:")
        
        start_time = time.time()
        
        progress = create_hybrid_progress(
            total=50,
            description=f"{name} Performance Test",
            theme=HybridProgressTheme.CYBERPUNK_FUSION,
            bar_width=bar_width,
            particle_effects=particles,
            glow_effect=glow,
            pulse_animation=pulse,
            show_time_left=True
        )
        
        progress.start()
        
        for i in range(1, 51):
            progress.set_progress(i, f"{name} step {i}/50...")
            time.sleep(0.02)
        
        progress.finish(f"⚡ {name} complete!")
        
        elapsed = time.time() - start_time
        print(f"  Time: {elapsed:.2f}s | Width: {bar_width} | Effects: {particles}/{glow}/{pulse}")

def main():
    """Main enhanced demonstration function"""
    # Show hybrid startup
    show_hybrid_startup()
    
    print("\n🎨 Welcome to the Enhanced Hybrid Progress Bar Demo!")
    print("This showcase demonstrates bigger, longer, more interactive progress bars")
    print("with particle effects, enhanced time tracking, and stunning visual effects!")
    
    time.sleep(2)
    
    # Run all enhanced demonstrations
    demo_enhanced_features()
    demo_bigger_progress_bars()
    demo_enhanced_time_tracking()
    demo_particle_effects()
    demo_glow_and_pulse_effects()
    demo_interactive_features()
    demo_all_enhanced_themes()
    demo_performance_comparison()
    
    print("\n🎉 Enhanced Demo Complete!")
    print("The hybrid progress bars now feature:")
    print("  📏 Bigger bars (60-120 characters)")
    print("  ⏱️ Enhanced time tracking (elapsed + ETA)")
    print("  🎆 Dynamic particle effects")
    print("  💫 Glow and pulse animations")
    print("  🎮 Interactive controls")
    print("  🌈 Stunning visual effects")
    print("\nYou can now use these enhanced hybrid progress bars in your applications!")

if __name__ == "__main__":
    main()
