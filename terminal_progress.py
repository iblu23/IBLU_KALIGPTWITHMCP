#!/usr/bin/env python3
"""
Advanced 3D Terminal Progress Bar System
Modern, visually stunning progress bars with gradients, shadows, and 3D effects
"""

import time
import threading
import math
from typing import Optional, Callable, Any
from dataclasses import dataclass


@dataclass
class ProgressConfig:
    """Configuration for modern 3D progress bar styling"""
    # 3D Effect characters
    fill_char: str = "█"
    empty_char: str = "░"
    shadow_char: str = "▓"
    highlight_char: str = "▒"
    border_char: str = "═"
    
    # Modern color scheme with gradients
    fill_color: str = "\033[95m"  # Bright magenta
    fill_gradient: str = "\033[38;5;201m"  # Hot pink gradient
    shadow_color: str = "\033[38;5;52m"  # Dark shadow
    highlight_color: str = "\033[38;5;225m"  # Light pink highlight
    border_color: str = "\033[38;5;135m"  # Purple border
    empty_color: str = "\033[38;5;59m"  # Dark grey
    reset_color: str = "\033[0m"
    
    # 3D Effects
    enable_3d: bool = True
    enable_gradient: bool = True
    enable_shadow: bool = True
    enable_glow: bool = True
    enable_animation: bool = True
    
    # Layout
    bar_width: int = 30
    show_percentage: bool = True
    show_time: bool = True
    show_steps: bool = True
    show_eta: bool = True


class Modern3DProgressBar:
    """Modern 3D terminal progress bar with advanced visual effects"""
    
    def __init__(self, total: int = 100, config: Optional[ProgressConfig] = None, 
                 prefix: str = "", suffix: str = "", step_info: str = ""):
        self.total = total
        self.current = 0
        self.config = config or ProgressConfig()
        self.prefix = prefix
        self.suffix = suffix
        self.step_info = step_info
        self.start_time = time.time()
        self.last_update_time = time.time()
        self.animation_phase = 0
        self._active = False
        self._thread = None
        self._stop_event = threading.Event()
        
    def _get_gradient_color(self, position: float) -> str:
        """Get gradient color based on position (0.0 to 1.0)"""
        if not self.config.enable_gradient:
            return self.config.fill_color
        
        # Create gradient effect with multiple color steps
        gradient_steps = [
            (0.0, "\033[38;5;225m"),   # Light pink
            (0.3, "\033[38;5;201m"),   # Hot pink  
            (0.6, "\033[95m"),          # Bright magenta
            (0.8, "\033[38;5;165m"),   # Medium magenta
            (1.0, "\033[38;5;135m")    # Purple
        ]
        
        for i, (pos, color) in enumerate(gradient_steps[:-1]):
            next_pos, next_color = gradient_steps[i + 1]
            if pos <= position < next_pos:
                return color
        
        return gradient_steps[-1][1]
    
    def _create_3d_bar(self, progress: float) -> str:
        """Create a 3D-styled progress bar with shadows and highlights"""
        bar_width = self.config.bar_width
        filled_width = int(bar_width * progress)
        empty_width = bar_width - filled_width
        
        # Build the 3D bar layer by layer
        layers = []
        
        if self.config.enable_3d:
            # Shadow layer (bottom)
            if self.config.enable_shadow and filled_width > 0:
                shadow_width = max(0, filled_width - 1)
                shadow_part = f"{self.config.shadow_color}{self.config.shadow_char * shadow_width}{self.config.reset_color}"
                empty_shadow = f"{self.config.empty_color}{self.config.empty_char * (bar_width - shadow_width)}{self.config.reset_color}"
                layers.append(f"  {shadow_part}{empty_shadow}")
            
            # Main fill layer with gradient
            fill_parts = []
            for i in range(filled_width):
                position = i / max(1, filled_width - 1) if filled_width > 1 else 0
                color = self._get_gradient_color(position)
                fill_parts.append(f"{color}{self.config.fill_char}{self.config.reset_color}")
            
            fill_part = "".join(fill_parts)
            empty_part = f"{self.config.empty_color}{self.config.empty_char * empty_width}{self.config.reset_color}"
            layers.append(f"  [{fill_part}{empty_part}]")
            
            # Highlight layer (top)
            if self.config.enable_3d and filled_width > 2:
                highlight_width = min(filled_width - 2, max(1, filled_width // 3))
                highlight_pos = max(0, filled_width - highlight_width - 1)
                
                before_highlight = f"{self.config.reset_color}{' ' * highlight_pos}"
                highlight_part = f"{self.config.highlight_color}{self.config.highlight_char * highlight_width}{self.config.reset_color}"
                after_highlight = f"{self.config.reset_color}{' ' * (bar_width - highlight_pos - highlight_width)}"
                
                layers.append(f"  {before_highlight}{highlight_part}{after_highlight}")
        else:
            # Simple 2D bar
            fill_part = f"{self.config.fill_color}{self.config.fill_char * filled_width}{self.config.reset_color}"
            empty_part = f"{self.config.empty_color}{self.config.empty_char * empty_width}{self.config.reset_color}"
            layers.append(f"[{fill_part}{empty_part}]")
        
        return "\n".join(layers)
    
    def _add_glow_effect(self, text: str) -> str:
        """Add glowing effect to text"""
        if not self.config.enable_glow:
            return text
        
        # Create glow by alternating bright and normal colors
        glow_chars = "█▓▒░"
        glow_colors = ["\033[95m", "\033[38;5;225m", "\033[38;5;201m"]
        
        # Simple glow effect around the bar
        return f"{glow_colors[0]}╔{self.config.border_char * (len(text) + 4)}╗{self.config.reset_color}\n" \
               f"{glow_colors[0]}║ {self.config.fill_color}{text}{self.config.reset_color} {glow_colors[0]}║{self.config.reset_color}\n" \
               f"{glow_colors[0]}╚{self.config.border_char * (len(text) + 4)}╝{self.config.reset_color}"
    
    def _format_time(self, elapsed: float) -> str:
        """Format elapsed time as HH:MM:SS"""
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def _calculate_eta(self, elapsed: float, progress: float) -> str:
        """Calculate estimated time remaining"""
        if progress <= 0:
            return "0:00:00"
        
        rate = self.current / elapsed if elapsed > 0 else 0
        if rate <= 0:
            return "0:00:00"
            
        remaining = (self.total - self.current) / rate
        return self._format_time(remaining)
    
    def _render_progress_info(self) -> str:
        """Render progress information with modern styling"""
        progress = self.current / self.total if self.total > 0 else 0
        percentage = progress * 100
        elapsed = time.time() - self.start_time
        eta = self._calculate_eta(elapsed, progress)
        
        # Modern percentage display with animation
        if self.config.enable_animation:
            self.animation_phase += 0.1
            pulse = abs(math.sin(self.animation_phase)) * 0.3 + 0.7
            if percentage > 75:
                color = f"\033[38;5;46m"  # Bright green
            elif percentage > 50:
                color = f"\033[38;5;226m"  # Bright yellow
            elif percentage > 25:
                color = f"\033[38;5;208m"  # Orange
            else:
                color = f"\033[38;5;201m"  # Pink
            
            percentage_text = f"{color}{percentage:5.1f}%{self.config.reset_color}"
        else:
            percentage_text = f"{percentage:5.1f}%"
        
        # Time information
        time_parts = []
        if self.config.show_time:
            time_parts.append(f"⏱ {self._format_time(elapsed)}")
        if self.config.show_eta and self.current > 0 and self.current < self.total:
            time_parts.append(f"⏳ ETA: {eta}")
        
        time_info = " | ".join(time_parts) if time_parts else ""
        
        return percentage_text, time_info
    
    def _render_complete_line(self) -> str:
        """Render the complete progress display"""
        progress = self.current / self.total if self.total > 0 else 0
        
        # Create 3D bar
        bar_lines = self._create_3d_bar(progress)
        
        # Get progress information
        percentage_text, time_info = self._render_progress_info()
        
        # Build complete display
        parts = []
        
        # Header with prefix and step info
        header_parts = []
        if self.prefix:
            header_parts.append(f"{self.config.fill_color}🚀{self.config.reset_color} {self.prefix}")
        if self.step_info and self.config.show_steps:
            header_parts.append(f"{self.config.highlight_color}➤{self.config.reset_color} {self.step_info}")
        
        if header_parts:
            header = " ".join(header_parts)
            parts.append(header)
        
        # Progress bar
        parts.append(bar_lines)
        
        # Footer with percentage and time
        footer_parts = [percentage_text]
        if time_info:
            footer_parts.append(time_info)
        if self.suffix:
            footer_parts.append(f"{self.config.border_color}◆{self.config.reset_color} {self.suffix}")
        
        footer = " | ".join(footer_parts)
        parts.append(f"  {footer}")
        
        return "\n".join(parts)
    
    def update(self, current: Optional[int] = None, step_info: str = "", 
              prefix: str = "", suffix: str = ""):
        """Update the progress bar with modern visuals"""
        if current is not None:
            self.current = min(current, self.total)
        
        if step_info:
            self.step_info = step_info
        if prefix:
            self.prefix = prefix
        if suffix:
            self.suffix = suffix
        
        # For better compatibility, just print the current state without cursor movement
        display = self._render_complete_line()
        
        # Clear current line and print new display
        print(f"\r{' ' * 100}\r{display}", end="", flush=True)
        
        self.last_update_time = time.time()
    
    def step(self, amount: int = 1, step_info: str = "", 
             prefix: str = "", suffix: str = ""):
        """Advance progress by a step"""
        self.update(self.current + amount, step_info, prefix, suffix)
    
    def finish(self, message: str = "Complete!"):
        """Finish the progress bar with a celebration effect"""
        self.current = self.total
        elapsed = time.time() - self.start_time
        
        # Celebration completion display
        completion_parts = []
        
        if self.config.show_time:
            completion_parts.append(f"⏱ {self._format_time(elapsed)}")
        
        if self.prefix:
            completion_parts.append(f"{self.prefix}")
        
        completion_parts.append(f"{self.config.fill_color}🎉✅ {message}{self.config.reset_color}")
        
        completion_text = " | ".join(completion_parts)
        
        # Final 3D bar at 100%
        bar_lines = self._create_3d_bar(1.0)
        
        # Clear and show completion
        print(f"\r{' ' * 100}\r", end="", flush=True)
        print(bar_lines)
        print(f"  {self.config.fill_color}██████████████████████████████{self.config.reset_color} 100.0% | {completion_text}")
        print()  # Extra line for spacing
        
        self._active = False
    
    def __enter__(self):
        """Context manager entry"""
        self._active = True
        self.start_time = time.time()
        print()  # Initial spacing
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        if self._active:
            self.finish()


class ProgressManager:
    """Manager for multiple modern 3D progress bars"""
    
    def __init__(self):
        self.bars = []
    
    def create_bar(self, total: int = 100, prefix: str = "", 
                   step_info: str = "", config: Optional[ProgressConfig] = None) -> Modern3DProgressBar:
        """Create a new modern 3D progress bar"""
        bar = Modern3DProgressBar(total=total, prefix=prefix, step_info=step_info, config=config)
        self.bars.append(bar)
        return bar
    
    def run_with_progress(self, title: str, task_func: Callable, 
                         total_steps: int = 100, steps: list = None) -> Any:
        """Run a function with modern 3D progress tracking"""
        config = ProgressConfig(enable_3d=True, enable_gradient=True, enable_shadow=True)
        
        with Modern3DProgressBar(total=total_steps, prefix=title, config=config) as bar:
            if steps:
                # Execute with predefined steps
                for i, (step_progress, step_description) in enumerate(steps):
                    bar.update(step_progress, step_description)
                    time.sleep(0.1)  # Brief pause for visual effect
                
                # Execute the actual task
                result = task_func()
                bar.finish(f"{title} complete!")
                return result
            else:
                # Execute with dynamic progress updates
                def update_wrapper(progress_val, desc):
                    bar.update(progress_val, desc)
                
                if callable(task_func):
                    result = task_func(update_wrapper)
                    bar.finish(f"{title} complete!")
                    return result
                
                return None


# Convenience functions for common use cases
def create_modern_progress(total: int = 100, prefix: str = "", 
                          enable_3d: bool = True) -> Modern3DProgressBar:
    """Create a modern 3D progress bar"""
    config = ProgressConfig(enable_3d=enable_3d, enable_gradient=True, enable_shadow=True)
    return Modern3DProgressBar(total=total, prefix=prefix, config=config)


def run_task_with_progress(title: str, task_func: Callable, 
                           total_steps: int = 100) -> Any:
    """Run a task with modern 3D progress tracking"""
    manager = ProgressManager()
    return manager.run_with_progress(title, task_func, total_steps)


# Legacy compatibility
TerminalProgressBar = Modern3DProgressBar


# Example usage and testing
if __name__ == "__main__":
    # Test the modern 3D progress bar
    print("🎨 Testing Modern 3D Progress Bar:")
    
    config = ProgressConfig(
        enable_3d=True,
        enable_gradient=True,
        enable_shadow=True,
        enable_glow=True,
        enable_animation=True
    )
    
    with Modern3DProgressBar(total=100, prefix="Installing:", step_info="Downloading packages", config=config) as bar:
        for i in range(0, 101, 5):
            bar.update(i, f"Step {i}/100")
            time.sleep(0.05)
    
    print("\n🚀 Testing multiple bars:")
    manager = ProgressManager()
    
    def test_task(callback):
        for i in range(0, 101, 10):
            if callback:
                callback(i, f"Processing item {i}")
            time.sleep(0.02)
        return "Task completed!"
    
    result = manager.run_with_progress("Processing", test_task, 100)
    print(f"Result: {result}")
