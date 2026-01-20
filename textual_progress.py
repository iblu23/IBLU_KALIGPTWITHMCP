#!/usr/bin/env python3
"""
🎨 Textual-based Visual Progress System for IBLU KALIGPT
Beautiful, animated progress bars with random visual effects for each session
"""

import asyncio
import random
import time
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from enum import Enum

try:
    from textual.app import App, ComposeResult
    from textual.containers import Horizontal, Vertical
    from textual.widgets import ProgressBar, Static, Footer
    from textual.reactive import reactive
    from textual.binding import Binding
    from textual.screen import ModalScreen
    from textual import on
    TEXTUAL_AVAILABLE = True
except ImportError:
    TEXTUAL_AVAILABLE = False

class ProgressEffect(Enum):
    """Visual effects for progress bars"""
    RAINBOW = "rainbow"
    PULSE = "pulse"
    WAVE = "wave"
    NEON = "neon"
    MATRIX = "matrix"
    FIRE = "fire"
    OCEAN = "ocean"
    GALAXY = "galaxy"
    CYBER = "cyber"
    AURORA = "aurora"

@dataclass
class ProgressTheme:
    """Theme configuration for progress effects"""
    name: str
    primary_color: str
    secondary_color: str
    background_color: str
    effect_type: ProgressEffect
    animation_speed: float = 1.0
    glow_intensity: float = 0.8

class VisualThemes:
    """Collection of beautiful visual themes"""
    
    THEMES = [
        ProgressTheme("Cyber Blue", "#00ffff", "#0080ff", "#001122", ProgressEffect.CYBER, 1.2, 0.9),
        ProgressTheme("Neon Purple", "#ff00ff", "#8000ff", "#220022", ProgressEffect.NEON, 1.0, 1.0),
        ProgressTheme("Matrix Green", "#00ff00", "#008800", "#001100", ProgressEffect.MATRIX, 0.8, 0.7),
        ProgressTheme("Fire Orange", "#ff6600", "#ff0000", "#220000", ProgressEffect.FIRE, 1.5, 1.0),
        ProgressTheme("Ocean Blue", "#0066ff", "#00ccff", "#002244", ProgressEffect.OCEAN, 0.6, 0.8),
        ProgressTheme("Galaxy Purple", "#9966ff", "#ff66ff", "#110022", ProgressEffect.GALAXY, 0.7, 0.9),
        ProgressTheme("Rainbow Wave", "#ff0000", "#00ff00", "#000011", ProgressEffect.RAINBOW, 1.0, 0.8),
        ProgressTheme("Aurora Green", "#00ff99", "#66ffcc", "#001133", ProgressEffect.AURORA, 0.5, 0.6),
        ProgressTheme("Terminal Pink", "#ff00ff", "#cc00cc", "#333333", ProgressEffect.PULSE, 1.0, 0.8),
    ]
    
    @classmethod
    def get_random_theme(cls) -> ProgressTheme:
        """Get a random theme for each session"""
        return random.choice(cls.THEMES)

class AnimatedProgressBar(ProgressBar):
    """Enhanced progress bar with visual effects"""
    
    current_theme: reactive[Optional[ProgressTheme]] = reactive(None)
    
    def __init__(self, theme: Optional[ProgressTheme] = None, **kwargs):
        super().__init__(**kwargs)
        self.current_theme = theme or VisualThemes.get_random_theme()
        self.animation_offset = random.random() * 2 * 3.14159  # Random phase offset
        self.pulse_phase = 0
        
    def render(self) -> str:
        """Render with visual effects"""
        if not self.current_theme:
            return super().render()
        
        # Apply visual effects based on theme
        effect = self.current_theme.effect_type
        
        if effect == ProgressEffect.PULSE:
            return self._render_pulse()
        elif effect == ProgressEffect.WAVE:
            return self._render_wave()
        elif effect == ProgressEffect.NEON:
            return self._render_neon()
        elif effect == ProgressEffect.MATRIX:
            return self._render_matrix()
        elif effect == ProgressEffect.FIRE:
            return self._render_fire()
        elif effect == ProgressEffect.OCEAN:
            return self._render_ocean()
        elif effect == ProgressEffect.GALAXY:
            return self._render_galaxy()
        elif effect == ProgressEffect.CYBER:
            return self._render_cyber()
        elif effect == ProgressEffect.AURORA:
            return self._render_aurora()
        else:  # RAINBOW
            return self._render_rainbow()
    
    def _render_pulse(self) -> str:
        """Pulsing effect"""
        self.pulse_phase += 0.1 * self.current_theme.animation_speed
        pulse_intensity = (abs(self.pulse_phase % (2 * 3.14159)) / 3.14159)
        
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Apply pulse to filled portion
        pulse_char = "█" if pulse_intensity > 0.5 else "▓"
        bar = pulse_char * filled + "░" * (bar_length - filled)
        
        return f"[{self.current_theme.primary_color}]{bar}[/{self.current_theme.primary_color}] {percentage:.1%}"
    
    def _render_wave(self) -> str:
        """Wave effect"""
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Create wave pattern
        wave_chars = ["░", "▒", "▓", "█", "▓", "▒"]
        bar = ""
        for i in range(bar_length):
            if i < filled:
                wave_idx = int((i + self.animation_offset) % len(wave_chars))
                bar += wave_chars[wave_idx]
            else:
                bar += "░"
        
        return f"[{self.current_theme.primary_color}]{bar}[/{self.current_theme.primary_color}] {percentage:.1%}"
    
    def _render_neon(self) -> str:
        """Neon glow effect"""
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Neon effect with glow
        bar = "▓" * filled + " " * (bar_length - filled)
        
        return f"[bold {self.current_theme.primary_color}]{bar}[/bold {self.current_theme.primary_color}] {percentage:.1%}"
    
    def _render_matrix(self) -> str:
        """Matrix digital rain effect"""
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Matrix characters
        matrix_chars = ["0", "1"]
        bar = ""
        for i in range(bar_length):
            if i < filled:
                bar += random.choice(matrix_chars)
            else:
                bar += " "
        
        return f"[{self.current_theme.primary_color}]{bar}[/{self.current_theme.primary_color}] {percentage:.1%}"
    
    def _render_fire(self) -> str:
        """Fire effect"""
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Fire characters
        fire_chars = ["░", "▒", "▓", "█"]
        bar = ""
        for i in range(bar_length):
            if i < filled:
                intensity = min(3, int(random.random() * 4))
                bar += fire_chars[intensity]
            else:
                bar += " "
        
        return f"[{self.current_theme.primary_color}]{bar}[/{self.current_theme.primary_color}] {percentage:.1%}"
    
    def _render_ocean(self) -> str:
        """Ocean wave effect"""
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Ocean wave characters
        ocean_chars = ["~", "≈", "≋", "≈", "~"]
        bar = ""
        for i in range(bar_length):
            if i < filled:
                wave_idx = int((i + self.animation_offset) % len(ocean_chars))
                bar += ocean_chars[wave_idx]
            else:
                bar += " "
        
        return f"[{self.current_theme.primary_color}]{bar}[/{self.current_theme.primary_color}] {percentage:.1%}"
    
    def _render_galaxy(self) -> str:
        """Galaxy star effect"""
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Galaxy characters
        galaxy_chars = ["·", "✦", "✧", "⋆", "✦", "·"]
        bar = ""
        for i in range(bar_length):
            if i < filled:
                star_idx = int((i + self.animation_offset) % len(galaxy_chars))
                bar += galaxy_chars[star_idx]
            else:
                bar += " "
        
        return f"[{self.current_theme.primary_color}]{bar}[/{self.current_theme.primary_color}] {percentage:.1%}"
    
    def _render_cyber(self) -> str:
        """Cyberpunk effect"""
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Cyber characters
        cyber_chars = ["▀", "▄", "■", "▪", "■"]
        bar = ""
        for i in range(bar_length):
            if i < filled:
                cyber_idx = int((i + self.animation_offset) % len(cyber_chars))
                bar += cyber_chars[cyber_idx]
            else:
                bar += " "
        
        return f"[bold {self.current_theme.primary_color}]{bar}[/bold {self.current_theme.primary_color}] {percentage:.1%}"
    
    def _render_aurora(self) -> str:
        """Aurora borealis effect"""
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Aurora characters with gradient
        aurora_chars = ["░", "▒", "▓", "█", "▓", "▒", "░"]
        bar = ""
        for i in range(bar_length):
            if i < filled:
                aurora_idx = int((i + self.animation_offset) % len(aurora_chars))
                bar += aurora_chars[aurora_idx]
            else:
                bar += " "
        
        return f"[{self.current_theme.primary_color}]{bar}[/{self.current_theme.primary_color}] {percentage:.1%}"
    
    def _render_rainbow(self) -> str:
        """Rainbow effect"""
        base_progress = self.progress or 0
        total = self.total or 100
        percentage = base_progress / total if total > 0 else 0
        
        bar_length = 30
        filled = int(bar_length * percentage)
        
        # Rainbow colors
        rainbow_colors = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff", "#4b0082", "#9400d3"]
        bar = ""
        for i in range(bar_length):
            if i < filled:
                color_idx = int((i + self.animation_offset) % len(rainbow_colors))
                bar += f"[{rainbow_colors[color_idx]}]█[/{rainbow_colors[color_idx]}]"
            else:
                bar += "░"
        
        return f"{bar} {percentage:.1%}"

class ProgressModal(ModalScreen):
    """Modal screen for progress display"""
    
    BINDINGS = [("escape,q", "dismiss", "Close")]
    
    def __init__(self, title: str, tasks: List[Dict[str, Any]], theme: Optional[ProgressTheme] = None):
        super().__init__()
        self.title = title
        self.tasks = tasks
        self.theme = theme or VisualThemes.get_random_theme()
        self.progress_bars = {}
        self.current_task_index = 0
        self.completed_tasks = 0
        
    def compose(self) -> ComposeResult:
        """Compose the modal layout"""
        with Vertical(id="progress-container"):
            yield Static(f"🎨 {self.title}", id="progress-title")
            yield Static(f"🎭 Theme: {self.theme.name}", id="theme-info")
            
            # Create progress bars for each task
            for i, task in enumerate(self.tasks):
                yield Static(f"📦 {task['name']}", id=f"task-label-{i}")
                yield AnimatedProgressBar(
                    theme=self.theme,
                    total=task.get('total', 100),
                    show_eta=True,
                    id=f"progress-{i}"
                )
            
            yield Static("", id="overall-status")
    
    def on_mount(self) -> None:
        """Initialize the modal"""
        self.set_interval(0.1, self.update_progress)
        self.title_update()
    
    def title_update(self) -> None:
        """Update title with animation"""
        self.query_one("#progress-title", Static).update(
            f"🎨 {self.title} 🎭 [{self.theme.name}]"
        )
    
    def update_progress(self) -> None:
        """Update progress bars"""
        if self.current_task_index < len(self.tasks):
            current_task = self.tasks[self.current_task_index]
            progress_bar = self.query_one(f"#progress-{self.current_task_index}", AnimatedProgressBar)
            
            # Simulate progress (in real usage, this would be updated from external source)
            current_progress = progress_bar.progress or 0
            if current_progress < current_task.get('total', 100):
                new_progress = min(current_progress + random.randint(1, 3), current_task.get('total', 100))
                progress_bar.advance(new_progress - current_progress)
            else:
                # Move to next task
                self.completed_tasks += 1
                self.current_task_index += 1
                
                if self.current_task_index < len(self.tasks):
                    # Update status
                    status_text = f"✅ Completed {self.completed_tasks}/{len(self.tasks)} tasks"
                    self.query_one("#overall-status", Static).update(status_text)
                else:
                    # All tasks completed
                    self.query_one("#overall-status", Static).update(
                        f"🎉 All {len(self.tasks)} tasks completed successfully!"
                    )
                    # Auto-dismiss after 2 seconds
                    self.set_timer(2.0, self.dismiss)

class TextualProgressManager:
    """Manager for Textual progress displays"""
    
    def __init__(self):
        self.current_theme = VisualThemes.get_random_theme()
        self.active_sessions = []
        
    def create_progress_session(self, title: str, tasks: List[Dict[str, Any]]) -> 'ProgressApp':
        """Create a new progress session with random visual effects"""
        # Get a new random theme for each session
        session_theme = VisualThemes.get_random_theme()
        
        app = ProgressApp(title, tasks, session_theme)
        self.active_sessions.append(app)
        return app
    
    def show_model_installation_progress(self, model_name: str, steps: List[str]) -> None:
        """Show progress for model installation"""
        tasks = [
            {"name": step, "total": 100} for step in steps
        ]
        
        app = self.create_progress_session(f"Installing {model_name}", tasks)
        
        if TEXTUAL_AVAILABLE:
            asyncio.create_task(app.run_async())
        else:
            print(f"🎨 {model_name} Installation Progress:")
            for i, step in enumerate(steps, 1):
                print(f"  {i}. {step}")
                time.sleep(0.5)  # Simulate progress

class ProgressApp(App):
    """Main progress application"""
    
    CSS = """
    #progress-container {
        width: 80%;
        height: auto;
        border: solid $primary;
        background: $background;
        padding: 1;
    }
    
    #progress-title {
        text-align: center;
        text-style: bold;
        color: $primary;
        margin: 1;
    }
    
    #theme-info {
        text-align: center;
        color: $secondary;
        margin: 0 1;
    }
    
    AnimatedProgressBar {
        width: 100%;
        margin: 0 1;
    }
    
    #overall-status {
        text-align: center;
        color: $success;
        margin: 1;
        text-style: bold;
    }
    """
    
    def __init__(self, title: str, tasks: List[Dict[str, Any]], theme: ProgressTheme):
        super().__init__()
        self.title = title
        self.tasks = tasks
        self.theme = theme
    
    def on_mount(self) -> None:
        """Initialize the app"""
        self.push_screen(ProgressModal(self.title, self.tasks, self.theme))

# Compatibility layer for non-Textual environments
class FallbackProgressManager:
    """Fallback progress manager when Textual is not available"""
    
    def __init__(self):
        self.current_effects = ["spinner", "dots", "bars", "arrows"]
        
    def show_model_installation_progress(self, model_name: str, steps: List[str]) -> None:
        """Show fallback progress"""
        effect = random.choice(self.current_effects)
        print(f"🎨 {model_name} Installation [{effect} effect]:")
        
        for i, step in enumerate(steps, 1):
            if effect == "spinner":
                spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
                for _ in range(5):
                    for char in spinner_chars:
                        print(f"\r{char} Step {i}/{len(steps)}: {step}", end="", flush=True)
                        time.sleep(0.1)
                print()
            else:
                print(f"  ✅ Step {i}/{len(steps)}: {step}")
                time.sleep(0.3)

# Main progress manager instance
if TEXTUAL_AVAILABLE:
    progress_manager = TextualProgressManager()
else:
    progress_manager = FallbackProgressManager()

# Export for use in other modules
__all__ = [
    'progress_manager',
    'TextualProgressManager', 
    'ProgressTheme',
    'VisualThemes',
    'ProgressEffect',
    'TEXTUAL_AVAILABLE'
]
