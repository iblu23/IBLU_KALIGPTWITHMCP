#!/usr/bin/env python3
"""
🎨 Auto-Color Progress Integration
Easy integration for auto-color cycling in any application
"""

from auto_color_cycler import AutoColorCycler

# Global cycler instance
auto_cycler = AutoColorCycler()

def create_auto_color_progress(total, description):
    """
    Create a progress bar with automatic color cycling
    
    Args:
        total (int): Total number of steps
        description (str): Description for the progress bar
        
    Returns:
        HybridStunningProgressBar: Progress bar with next color in cycle
    """
    return auto_cycler.create_progress_with_next_color(total, description)

def reset_color_cycle():
    """Reset the color cycle to start from the beginning"""
    auto_cycler.color_index = 0

def get_current_color_scheme():
    """Get the current color scheme name"""
    if auto_cycler.color_index > 0:
        return auto_cycler.color_schemes[(auto_cycler.color_index - 1) % len(auto_cycler.color_schemes)]['name']
    return auto_cycler.color_schemes[0]['name']

def set_color_schemes(custom_schemes):
    """
    Set custom color schemes for cycling
    
    Args:
        custom_schemes (list): List of color scheme dictionaries
    """
    auto_cycler.color_schemes = custom_schemes
    auto_cycler.color_index = 0

# Example usage functions
def demo_simple_usage():
    """Simple usage example"""
    print("🎨 Simple Auto-Color Progress Usage")
    print("=" * 40)
    
    # Create multiple progress bars with automatic color cycling
    tasks = [
        (10, "🔧 Initializing"),
        (15, "📦 Installing"),
        (20, "🛠️ Building"),
        (12, "🔍 Testing"),
        (18, "🚀 Deploying")
    ]
    
    for total, description in tasks:
        progress = create_auto_color_progress(total, description)
        progress.start()
        
        for i in range(1, total + 1):
            progress.set_progress(i, f"{description} - {i}/{total}")
            import time
            time.sleep(0.1)
        
        progress.finish(f"✅ {description} Complete!")

if __name__ == "__main__":
    demo_simple_usage()
