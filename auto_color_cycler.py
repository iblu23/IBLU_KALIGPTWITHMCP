#!/usr/bin/env python3
"""
🎨 Auto-Color Cycling Progress Bar System
Forces every progress bar to use the same settings but different colors
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

class AutoColorCycler:
    """Automatically cycles through colors for progress bars"""
    
    def __init__(self):
        self.color_index = 0
        self.base_config = {
            'bar_width': 60,  # Shorter but fatter
            'bar_height': 3,  # 3 lines tall for fat appearance
            'particle_effects': True,
            'show_time_left': True,
            'interactive': True,
            'glow_effect': True,
            'pulse_animation': True,
            'show_percentage': True,
            'show_time': True,
            'show_spinner': True,
            'use_textual': True,
            'use_rich': True
        }
        
        # Define color schemes to cycle through
        self.color_schemes = [
            {
                'name': 'Electric Blue',
                'bar_color': '#00BFFF',
                'text_color': '#FFFFFF',
                'glow_color': '#00FFFF',
                'pulse_color': '#87CEEB',
                'gradient_colors': ['#00BFFF', '#87CEEB', '#4682B4', '#1E90FF']
            },
            {
                'name': 'Neon Pink',
                'bar_color': '#FF1493',
                'text_color': '#FFFFFF',
                'glow_color': '#FF69B4',
                'pulse_color': '#FFB6C1',
                'gradient_colors': ['#FF1493', '#FF69B4', '#FFB6C1', '#FFC0CB']
            },
            {
                'name': 'Lime Green',
                'bar_color': '#32CD32',
                'text_color': '#FFFFFF',
                'glow_color': '#00FF00',
                'pulse_color': '#7FFF00',
                'gradient_colors': ['#32CD32', '#00FF00', '#7FFF00', '#ADFF2F']
            },
            {
                'name': 'Golden Yellow',
                'bar_color': '#FFD700',
                'text_color': '#000000',
                'glow_color': '#FFA500',
                'pulse_color': '#FFFF00',
                'gradient_colors': ['#FFD700', '#FFA500', '#FFFF00', '#F0E68C']
            },
            {
                'name': 'Royal Purple',
                'bar_color': '#7851A9',
                'text_color': '#FFFFFF',
                'glow_color': '#9400D3',
                'pulse_color': '#8A2BE2',
                'gradient_colors': ['#7851A9', '#9400D3', '#8A2BE2', '#9932CC']
            },
            {
                'name': 'Coral Orange',
                'bar_color': '#FF7F50',
                'text_color': '#FFFFFF',
                'glow_color': '#FF6347',
                'pulse_color': '#FFA07A',
                'gradient_colors': ['#FF7F50', '#FF6347', '#FFA07A', '#FA8072']
            },
            {
                'name': 'Turquoise',
                'bar_color': '#40E0D0',
                'text_color': '#000000',
                'glow_color': '#00CED1',
                'pulse_color': '#48D1CC',
                'gradient_colors': ['#40E0D0', '#00CED1', '#48D1CC', '#00FFFF']
            },
            {
                'name': 'Rose Red',
                'bar_color': '#C71585',
                'text_color': '#FFFFFF',
                'glow_color': '#FF69B4',
                'pulse_color': '#FF1493',
                'gradient_colors': ['#C71585', '#FF69B4', '#FF1493', '#DB7093']
            },
            {
                'name': 'Mint Green',
                'bar_color': '#98FF98',
                'text_color': '#000000',
                'glow_color': '#00FF7F',
                'pulse_color': '#40E0D0',
                'gradient_colors': ['#98FF98', '#00FF7F', '#40E0D0', '#7FFFD4']
            },
            {
                'name': 'Deep Blue',
                'bar_color': '#000080',
                'text_color': '#FFFFFF',
                'glow_color': '#0000CD',
                'pulse_color': '#4169E1',
                'gradient_colors': ['#000080', '#0000CD', '#4169E1', '#1E90FF']
            }
        ]
    
    def get_next_color_scheme(self):
        """Get the next color scheme in the cycle"""
        scheme = self.color_schemes[self.color_index % len(self.color_schemes)]
        self.color_index += 1
        return scheme
    
    def create_dynamic_theme(self, color_scheme, description):
        """Create a dynamic theme with the given color scheme"""
        class DynamicTheme:
            value = {
                'name': color_scheme['name'],
                'rich_bar_color': color_scheme['bar_color'],
                'rich_text_color': color_scheme['text_color'],
                'rich_spinner': 'dots',
                'textual_style': 'bold',
                'textual_background': 'on black',
                'description': description,
                'particle_effect': 'dynamic',
                'truecolor': True,
                'gradient_colors': color_scheme['gradient_colors'],
                'glow_color': color_scheme['glow_color'],
                'pulse_color': color_scheme['pulse_color']
            }
        
        return DynamicTheme()
    
    def create_progress_with_next_color(self, total, description):
        """Create a progress bar with the next color in the cycle"""
        color_scheme = self.get_next_color_scheme()
        theme = self.create_dynamic_theme(color_scheme, description)
        
        config = HybridProgressConfig(
            total=total,
            description=description,
            theme=theme,
            **self.base_config
        )
        
        return HybridStunningProgressBar(config)

def demo_auto_color_cycling():
    """Demonstrate automatic color cycling"""
    print("🎨 Auto-Color Cycling Progress Bar Demo")
    print("=" * 45)
    
    cycler = AutoColorCycler()
    
    print(f"\n🎨 Cycling through {len(cycler.color_schemes)} color schemes...")
    print("Each progress bar uses the same settings but different colors!")
    
    tasks = [
        (15, "🔧 Initializing System Components"),
        (20, "📦 Downloading Required Packages"),
        (25, "🛠️ Building Application Modules"),
        (18, "🔍 Running Security Scans"),
        (22, "🌐 Configuring Network Settings"),
        (16, "💾 Setting Up Database"),
        (19, "🔑 Generating Security Keys"),
        (21, "🧪 Running Unit Tests"),
        (17, "📊 Performance Optimization"),
        (23, "🚀 Final System Preparation")
    ]
    
    for total, description in tasks:
        # Create progress bar with next color
        progress = cycler.create_progress_with_next_color(total, description)
        progress.start()
        
        # Simulate work
        for i in range(1, total + 1):
            progress.set_progress(i, f"{description} - Step {i}/{total}")
            time.sleep(0.05)
        
        progress.finish(f"✅ {description} Complete!")
        time.sleep(0.3)

def demo_rapid_color_cycling():
    """Demonstrate rapid color cycling with quick progress bars"""
    print("\n⚡ Rapid Color Cycling Demo")
    print("=" * 30)
    
    cycler = AutoColorCycler()
    
    print("\n🏎️ Rapid color cycling - Quick progress bars!")
    
    for i in range(15):
        total = random.randint(8, 15)
        description = f"⚡ Quick Task {i+1}"
        
        progress = cycler.create_progress_with_next_color(total, description)
        progress.start()
        
        for j in range(1, total + 1):
            progress.set_progress(j, f"{description} - {j}/{total}")
            time.sleep(0.02)
        
        progress.finish(f"⚡ {description} Complete!")
        time.sleep(0.1)

def demo_consistent_settings_different_colors():
    """Demonstrate consistent settings with different colors"""
    print("\n🎯 Consistent Settings, Different Colors Demo")
    print("=" * 50)
    
    cycler = AutoColorCycler()
    
    print("\n📏 All progress bars have identical settings:")
    print("  • Bar width: 100 characters")
    print("  • Particle effects: Enabled")
    print("  • Time tracking: Enabled")
    print("  • Glow effects: Enabled")
    print("  • Pulse animations: Enabled")
    print("  • Interactive controls: Enabled")
    print("  • Only colors change!")
    
    tasks = [
        (30, "🔧 System Configuration"),
        (30, "📦 Package Installation"),
        (30, "🛠️ Module Compilation"),
        (30, "🔍 Security Analysis"),
        (30, "🌐 Network Setup")
    ]
    
    for total, description in tasks:
        progress = cycler.create_progress_with_next_color(total, description)
        progress.start()
        
        for i in range(1, total + 1):
            progress.set_progress(i, f"{description} - {i}/{total}")
            time.sleep(0.03)
        
        progress.finish(f"🎯 {description} Complete!")
        time.sleep(0.4)

def demo_color_scheme_showcase():
    """Showcase all available color schemes"""
    print("\n🌈 Color Scheme Showcase")
    print("=" * 30)
    
    cycler = AutoColorCycler()
    
    print(f"\n🎨 Showcasing all {len(cycler.color_schemes)} color schemes:")
    
    for i, scheme in enumerate(cycler.color_schemes):
        description = f"🎨 {scheme['name']} Color Scheme"
        progress = cycler.create_progress_with_next_color(25, description)
        progress.start()
        
        for j in range(1, 26):
            progress.set_progress(j, f"{scheme['name']} - {j}/25")
            time.sleep(0.04)
        
        progress.finish(f"🎨 {scheme['name']} Complete!")
        time.sleep(0.3)

def demo_custom_color_cycling():
    """Demonstrate custom color cycling patterns"""
    print("\n🎪 Custom Color Cycling Patterns")
    print("=" * 35)
    
    # Warm colors only
    print("\n🔥 Warm Color Cycle:")
    warm_cycler = AutoColorCycler()
    warm_cycler.color_schemes = [
        scheme for scheme in warm_cycler.color_schemes 
        if any(color in scheme['name'].lower() for color in ['orange', 'yellow', 'red', 'pink', 'coral'])
    ]
    
    for i in range(5):
        progress = warm_cycler.create_progress_with_next_color(20, f"🔥 Warm Task {i+1}")
        progress.start()
        
        for j in range(1, 21):
            progress.set_progress(j, f"Warm {j}/20")
            time.sleep(0.05)
        
        progress.finish(f"🔥 Warm Task {i+1} Complete!")
        time.sleep(0.3)
    
    # Cool colors only
    print("\n❄️ Cool Color Cycle:")
    cool_cycler = AutoColorCycler()
    cool_cycler.color_schemes = [
        scheme for scheme in cool_cycler.color_schemes 
        if any(color in scheme['name'].lower() for color in ['blue', 'green', 'turquoise', 'mint'])
    ]
    
    for i in range(5):
        progress = cool_cycler.create_progress_with_next_color(20, f"❄️ Cool Task {i+1}")
        progress.start()
        
        for j in range(1, 21):
            progress.set_progress(j, f"Cool {j}/20")
            time.sleep(0.05)
        
        progress.finish(f"❄️ Cool Task {i+1} Complete!")
        time.sleep(0.3)

def main():
    """Main auto-color cycling demonstration"""
    # Show hybrid startup
    show_hybrid_startup()
    
    print("\n🎨 Welcome to the Auto-Color Cycling Progress Bar System!")
    print("This system forces every progress bar to use the same settings")
    print("but automatically cycles through different beautiful colors!")
    
    time.sleep(2)
    
    # Run all demonstrations
    demo_auto_color_cycling()
    demo_rapid_color_cycling()
    demo_consistent_settings_different_colors()
    demo_color_scheme_showcase()
    demo_custom_color_cycling()
    
    print("\n🎉 Auto-Color Cycling Demo Complete!")
    print("The system features:")
    print("  🎨 10 beautiful color schemes")
    print("  🔄 Automatic color cycling")
    print("  📏 Consistent progress bar settings")
    print("  ⚡ Rapid color transitions")
    print("  🎯 Custom color patterns")
    print("  🌈 Warm and cool color cycles")
    print("  💫 Gradient effects per color")
    print("  ✨ Enhanced particle effects")
    print("\nYou can now use this auto-color cycling system in your applications!")

if __name__ == "__main__":
    main()
