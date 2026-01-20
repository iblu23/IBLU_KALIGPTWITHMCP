#!/usr/bin/env python3
"""
🎨 Hybrid Rich+Textual Progress Bar System
Combining the best of both worlds for stunning visual effects
"""

import time
import threading
import asyncio
from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass
from enum import Enum

# Rich imports
try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn, TaskID
    from rich.style import Style
    from rich.panel import Panel
    from rich.table import Table
    from rich.live import Live
    from rich.align import Align
    from rich.text import Text
    from rich import box
    from rich.layout import Layout
    from rich.columns import Columns
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# Textual imports
try:
    from textual.app import App, ComposeResult
    from textual.containers import Horizontal, Vertical, Container
    from textual.widgets import ProgressBar, Static, Footer, Header, Widget
    from textual.reactive import reactive
    from textual.binding import Binding
    from textual.screen import ModalScreen
    from textual.coordinate import Coordinate
    from textual import on
    TEXTUAL_AVAILABLE = True
except ImportError:
    TEXTUAL_AVAILABLE = False
    # Create fallback classes for when Textual is not available
    class Widget:
        def __init__(self, *args, **kwargs):
            pass
    
    class App:
        def __init__(self, *args, **kwargs):
            pass
        
        def run_async(self):
            return None
        
        def exit(self):
            pass
    
    class ComposeResult:
        def __init__(self, *args, **kwargs):
            pass
    
    class Container:
        def __init__(self, *args, **kwargs):
            pass
    
    class Static:
        def __init__(self, *args, **kwargs):
            pass
        
        def update(self, *args, **kwargs):
            pass
    
    class ProgressBar:
        def __init__(self, *args, **kwargs):
            self.progress = 0
    
    class Header:
        def __init__(self, *args, **kwargs):
            pass
    
    class Footer:
        def __init__(self, *args, **kwargs):
            pass
    
    class reactive:
        def __init__(self, *args, **kwargs):
            pass

# Colorama for fallback
try:
    from colorama import Fore, Style as ColoramaStyle
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

class HybridProgressTheme(Enum):
    """Hybrid themes combining Rich and Textual visual effects with TrueColor"""
    
    CYBERPUNK_FUSION = {
        'name': 'Cyberpunk Fusion',
        'rich_bar_color': '#00FFFF',  # Cyan truecolor
        'rich_text_color': '#FFFFFF',  # White truecolor
        'rich_spinner': 'dots',
        'textual_style': 'bold cyan',
        'textual_background': 'on black',
        'description': '🔮 Cyberpunk Rich+Textual Fusion',
        'particle_effect': 'digital_rain',
        'truecolor': True,
        'gradient_colors': ['#00FFFF', '#00CCCC', '#009999', '#006666'],  # Cyan gradient
        'glow_color': '#00FFFF',
        'pulse_color': '#00FFFF'
    }
    
    NEON_MATRIX = {
        'name': 'Neon Matrix',
        'rich_bar_color': '#00FF00',  # Bright green truecolor
        'rich_text_color': '#FFFFFF',  # White truecolor
        'rich_spinner': 'dots2',
        'textual_style': 'bold green',
        'textual_background': 'on black',
        'description': '💚 Neon Matrix Rich+Textual',
        'particle_effect': 'matrix_drops',
        'truecolor': True,
        'gradient_colors': ['#00FF00', '#00DD00', '#00BB00', '#009900'],  # Green gradient
        'glow_color': '#00FF00',
        'pulse_color': '#00FF00'
    }
    
    FIRE_PLASMA = {
        'name': 'Fire Plasma',
        'rich_bar_color': '#FF4500',  # Orange red truecolor
        'rich_text_color': '#FFFFFF',  # White truecolor
        'rich_spinner': 'line',
        'textual_style': 'bold yellow',
        'textual_background': 'on black',
        'description': '🔥 Fire Plasma Rich+Textual',
        'particle_effect': 'flames',
        'truecolor': True,
        'gradient_colors': ['#FF4500', '#FF6347', '#FF7F50', '#FFA500'],  # Fire gradient
        'glow_color': '#FF4500',
        'pulse_color': '#FF6347'
    }
    
    OCEAN_WAVE = {
        'name': 'Ocean Wave',
        'rich_bar_color': '#1E90FF',  # Dodger blue truecolor
        'rich_text_color': '#FFFFFF',  # White truecolor
        'rich_spinner': 'dots8',
        'textual_style': 'bold blue',
        'textual_background': 'on black',
        'description': '🌊 Ocean Wave Rich+Textual',
        'particle_effect': 'waves',
        'truecolor': True,
        'gradient_colors': ['#1E90FF', '#4169E1', '#0000CD', '#00008B'],  # Ocean gradient
        'glow_color': '#1E90FF',
        'pulse_color': '#4169E1'
    }
    
    GALAXY_NEBULA = {
        'name': 'Galaxy Nebula',
        'rich_bar_color': '#FF00FF',  # Magenta truecolor
        'rich_text_color': '#FFFFFF',  # White truecolor
        'rich_spinner': 'moon',
        'textual_style': 'bold magenta',
        'textual_background': 'on black',
        'description': '🌌 Galaxy Nebula Rich+Textual',
        'particle_effect': 'stars',
        'truecolor': True,
        'gradient_colors': ['#FF00FF', '#DA70D6', '#BA55D3', '#9370DB'],  # Purple gradient
        'glow_color': '#FF00FF',
        'pulse_color': '#DA70D6'
    }
    
    RAINBOW_PRISM = {
        'name': 'Rainbow Prism',
        'rich_bar_color': '#FF1493',  # Deep pink truecolor
        'rich_text_color': '#FFFFFF',  # White truecolor
        'rich_spinner': 'bouncingBar',
        'textual_style': 'bold rainbow',
        'textual_background': 'on black',
        'description': '🌈 Rainbow Prism Rich+Textual',
        'particle_effect': 'prisms',
        'truecolor': True,
        'gradient_colors': ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3'],  # Full rainbow
        'glow_color': '#FF1493',
        'pulse_color': '#FF69B4'
    }
    
    # Additional truecolor themes
    ELECTRIC_PURPLE = {
        'name': 'Electric Purple',
        'rich_bar_color': '#9400D3',  # Electric purple truecolor
        'rich_text_color': '#E6E6FA',  # Lavender truecolor
        'rich_spinner': 'dots',
        'textual_style': 'bold purple',
        'textual_background': 'on black',
        'description': '⚡ Electric Purple TrueColor',
        'particle_effect': 'lightning',
        'truecolor': True,
        'gradient_colors': ['#9400D3', '#8B008B', '#800080', '#6A0DAD'],  # Purple gradient
        'glow_color': '#9400D3',
        'pulse_color': '#8B008B'
    }
    
    GOLDEN_SUNSET = {
        'name': 'Golden Sunset',
        'rich_bar_color': '#FFD700',  # Gold truecolor
        'rich_text_color': '#FFF8DC',  # Cornsilk truecolor
        'rich_spinner': 'line',
        'textual_style': 'bold yellow',
        'textual_background': 'on black',
        'description': '🌅 Golden Sunset TrueColor',
        'particle_effect': 'sunrays',
        'truecolor': True,
        'gradient_colors': ['#FFD700', '#FFA500', '#FF8C00', '#FF6347'],  # Sunset gradient
        'glow_color': '#FFD700',
        'pulse_color': '#FFA500'
    }
    
    EMERALD_FOREST = {
        'name': 'Emerald Forest',
        'rich_bar_color': '#50C878',  # Emerald truecolor
        'rich_text_color': '#F0FFF0',  # Honeydew truecolor
        'rich_spinner': 'dots2',
        'textual_style': 'bold green',
        'textual_background': 'on black',
        'description': '🌲 Emerald Forest TrueColor',
        'particle_effect': 'leaves',
        'truecolor': True,
        'gradient_colors': ['#50C878', '#3CB371', '#2E8B57', '#228B22'],  # Forest gradient
        'glow_color': '#50C878',
        'pulse_color': '#3CB371'
    }

@dataclass
class HybridProgressConfig:
    """Configuration for hybrid progress bars"""
    total: int = 100
    description: str = "Processing..."
    theme: HybridProgressTheme = HybridProgressTheme.CYBERPUNK_FUSION
    show_percentage: bool = True
    show_time: bool = True
    show_spinner: bool = True
    bar_width: int = 80  # Increased from 40 for bigger bars
    animated: bool = True
    use_textual: bool = True
    use_rich: bool = True
    particle_effects: bool = True
    show_time_left: bool = True  # New: show estimated time remaining
    interactive: bool = True  # New: interactive features
    glow_effect: bool = True  # New: glow effects
    pulse_animation: bool = True  # New: pulse animations

class HybridRichProgressBar:
    """Rich component of hybrid progress bar"""
    
    def __init__(self, config: HybridProgressConfig):
        self.config = config
        self.console = Console() if RICH_AVAILABLE else None
        self.progress = None
        self.task_id = None
        self.start_time = None
        self.particle_chars = ['✨', '⭐', '💫', '🌟', '✦', '✧', '⚡', '🔥', '💥', '🎆']
        
    def create_rich_progress(self):
        """Create enhanced Rich progress bar component with truecolor"""
        if not RICH_AVAILABLE or not self.config.use_rich:
            return None
            
        theme = self.config.theme.value
        
        # Enhanced spinner with truecolor support
        spinner = SpinnerColumn(
            spinner_name=theme['rich_spinner'],
            style=Style(color=theme['rich_text_color'], bold=True),
            speed=1.5 if self.config.animated else 1.0
        ) if self.config.show_spinner else None
        
        # Enhanced text with truecolor glow effect
        text_style = Style(color=theme['rich_text_color'], bold=True)
        if self.config.glow_effect and theme.get('truecolor', False):
            text_style = Style(color=theme['rich_text_color'], bold=True, underline=True)
        
        text = TextColumn(
            self.config.description,
            style=text_style
        )
        
        # Enhanced bar with truecolor and gradient effects
        bar_color = theme['rich_bar_color']
        if theme.get('truecolor', False) and self.config.glow_effect:
            # Create gradient effect for truecolor themes
            bar_style = Style(color=bar_color, bold=True)
            complete_style = Style(color=theme.get('glow_color', bar_color), bold=True, blink=self.config.pulse_animation)
            finished_style = Style(color=theme.get('pulse_color', bar_color), bold=True, reverse=True)
            pulse_style = Style(color=bar_color, dim=True, italic=True)
        else:
            # Fallback to standard colors
            bar_style = Style(color=bar_color, bold=True)
            complete_style = Style(color=bar_color, bold=True, blink=self.config.pulse_animation)
            finished_style = Style(color=bar_color, bold=True, reverse=True)
            pulse_style = Style(color=bar_color, dim=True, italic=True)
        
        bar = BarColumn(
            bar_width=self.config.bar_width,  # Bigger bars
            style=bar_style,
            complete_style=complete_style,
            finished_style=finished_style,
            pulse_style=pulse_style
        )
        
        # Enhanced percentage with truecolor
        percentage_style = Style(color=theme['rich_text_color'], bold=True)
        if theme.get('truecolor', False):
            percentage_style = Style(color=theme['rich_text_color'], bold=True)
        
        percentage = TextColumn(
            "[progress.percentage]{task.percentage:>6.1f}%",
            style=percentage_style
        ) if self.config.show_percentage else None
        
        # Enhanced time tracking with truecolor
        time_columns = []
        if self.config.show_time:
            time_columns.append(TimeElapsedColumn())
        
        if self.config.show_time_left:
            # Custom time remaining column with truecolor
            class TimeRemainingColumn(TextColumn):
                def __init__(self):
                    super().__init__("", style=Style(color=theme.get('glow_color', 'cyan'), bold=True))
                
                def render(self, task):
                    if task.completed > 0 and task.total > 0:
                        elapsed = task.finished_time or task.elapsed
                        if elapsed > 0:
                            rate = task.completed / elapsed
                            remaining = (task.total - task.completed) / rate if rate > 0 else 0
                            minutes, seconds = divmod(int(remaining), 60)
                            if minutes > 0:
                                eta_color = theme.get('glow_color', 'cyan')
                                return Text(f"ETA: {minutes:02d}:{seconds:02d}", style=Style(color=eta_color, bold=True))
                            else:
                                eta_color = theme.get('glow_color', 'cyan')
                                return Text(f"ETA: {seconds:02d}s", style=Style(color=eta_color, bold=True))
                    eta_color = theme.get('glow_color', 'cyan')
                    return Text("ETA: --:--", style=Style(color=eta_color, dim=True))
            
            time_columns.append(TimeRemainingColumn())
        
        # Build columns list with enhanced layout
        columns = []
        if spinner:
            columns.append(spinner)
        columns.append(text)
        columns.append(bar)
        if percentage:
            columns.append(percentage)
        columns.extend(time_columns)
        
        # Add enhanced particle effects column with truecolor
        if self.config.particle_effects:
            class ParticleColumn(TextColumn):
                def __init__(self):
                    super().__init__("", style=Style(color=theme.get('glow_color', 'bright_yellow'), bold=True))
                
                def render(self, task):
                    import random
                    # Enhanced particle set for truecolor themes
                    if theme.get('truecolor', False):
                        particles = ['✨', '⭐', '💫', '🌟', '✦', '✧', '⚡', '🔥', '💥', '🎆', '🌈', '💎', '🔮']
                    else:
                        particles = ['✨', '⭐', '💫', '🌟']
                    
                    particle = random.choice(particles)
                    progress_pct = task.completed / task.total if task.total > 0 else 0
                    
                    # Truecolor particle effects
                    if theme.get('truecolor', False):
                        gradient_colors = theme.get('gradient_colors', [theme['rich_bar_color']])
                        color_index = int(progress_pct * (len(gradient_colors) - 1))
                        particle_color = gradient_colors[min(color_index, len(gradient_colors) - 1)]
                        
                        if progress_pct > 0.8:
                            return Text(particle, style=Style(color=theme.get('glow_color', particle_color), bold=True))
                        elif progress_pct > 0.5:
                            return Text(particle, style=Style(color=particle_color, bold=True))
                        elif progress_pct > 0.2:
                            return Text(particle, style=Style(color=particle_color, bold=True))
                        else:
                            return Text(particle, style=Style(color=particle_color, dim=True))
                    else:
                        # Fallback particle effects
                        if progress_pct > 0.8:
                            return Text(particle, style="bright_yellow")
                        elif progress_pct > 0.5:
                            return Text(particle, style="bright_cyan")
                        elif progress_pct > 0.2:
                            return Text(particle, style="bright_blue")
                        else:
                            return Text(particle, style="dim white")
            
            columns.append(ParticleColumn())
        
        # Create enhanced progress object with truecolor support
        progress = Progress(
            *columns,
            console=self.console,
            transient=False,
            refresh_per_second=20 if self.config.animated else 4,  # Higher refresh rate
            expand=True  # Make it expand to full width
        )
        
        return progress
    
    def start(self) -> Optional[TaskID]:
        """Start Rich progress bar"""
        if self.config.use_rich and RICH_AVAILABLE:
            self.progress = self.create_rich_progress()
            if self.progress:
                self.task_id = self.progress.add_task(
                    self.config.description,
                    total=self.config.total
                )
                self.progress.start()
                return self.task_id
        return None
    
    def update(self, advance: int = 1, description: str = None):
        """Update Rich progress"""
        if description:
            self.config.description = description
            
        if self.progress and self.task_id:
            self.progress.update(
                self.task_id,
                advance=advance,
                description=self.config.description
            )
    
    def set_progress(self, current: int, description: str = None):
        """Set specific progress value"""
        if description:
            self.config.description = description
            
        if self.progress and self.task_id:
            completed = current - self.progress.tasks[self.task_id].completed
            self.progress.update(
                self.task_id,
                completed=current,
                description=self.config.description
            )
    
    def finish(self, message: str = "✅ Complete!"):
        """Finish Rich progress bar"""
        if self.progress:
            if self.task_id:
                self.progress.update(self.task_id, completed=self.config.total)
            
            theme = self.config.theme.value
            self.console.print(f"[bold {theme['rich_bar_color']}]{message}[/bold {theme['rich_bar_color']}]")
            self.progress.stop()

class HybridTextualProgressBar(Widget):
    """Enhanced Textual component of hybrid progress bar"""
    
    def __init__(self, config: HybridProgressConfig):
        super().__init__()
        self.config = config
        self.current_progress = 0
        self.theme = config.theme.value
        self.start_time = None
        self.particle_chars = ['✨', '⭐', '💫', '🌟', '✦', '✧', '⚡', '🔥', '💥', '🎆']
        self.current_particle = 0
        
    def compose(self) -> ComposeResult:
        """Compose enhanced Textual widget"""
        theme = self.config.theme.value
        
        # Enhanced header with glow effect
        header_style = f"{theme['textual_style']} bold"
        if self.config.glow_effect:
            header_style += " underline"
        
        yield Static(f"[{header_style}] {self.config.description} [/{header_style}]", id="description")
        
        # Enhanced progress bar with bigger size
        yield ProgressBar(
            total=self.config.total, 
            show_percentage=self.config.show_percentage,
            id="progress",
            style=f"bold {theme['textual_style']}"
        )
        
        # Enhanced time tracking section
        with Container(id="time_container"):
            if self.config.show_time:
                yield Static("00:00:00", id="timer")
            if self.config.show_time_left:
                yield Static("ETA: --:--", id="eta")
        
        # Particle effects section
        if self.config.particle_effects:
            yield Static("✨", id="particles")
        
        # Interactive controls
        if self.config.interactive:
            with Container(id="controls"):
                yield Static("[Space] Pause | [R] Resume | [Q] Quit", id="controls_text")
    
    def on_mount(self) -> None:
        """Called when widget is mounted"""
        self.progress_bar = self.query_one("#progress", ProgressBar)
        self.start_time = time.time()
        
        # Set up timer updates
        self.set_interval(0.1, self.update_timer)
        
        # Set up particle animation
        if self.config.particle_effects:
            self.set_interval(0.5, self.update_particles)
        
        # Set up interactive controls
        if self.config.interactive:
            self.set_interval(0.1, self.check_interactive_input)
    
    def update_timer(self) -> None:
        """Update timer displays with enhanced formatting"""
        elapsed = int(time.time() - self.start_time)
        hours, remainder = divmod(elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if self.config.show_time:
            try:
                timer = self.query_one("#timer", Static)
                timer.update(f"⏱️ {hours:02d}:{minutes:02d}:{seconds:02d}")
            except:
                pass
        
        if self.config.show_time_left:
            try:
                eta = self.query_one("#eta", Static)
                if self.current_progress > 0 and self.config.total > 0:
                    rate = self.current_progress / elapsed if elapsed > 0 else 0
                    remaining = (self.config.total - self.current_progress) / rate if rate > 0 else 0
                    eta_minutes, eta_seconds = divmod(int(remaining), 60)
                    if eta_minutes > 0:
                        eta.update(f"⏳ ETA: {eta_minutes:02d}:{eta_seconds:02d}")
                    else:
                        eta.update(f"⏳ ETA: {eta_seconds:02d}s")
                else:
                    eta.update("⏳ ETA: --:--")
            except:
                pass
    
    def update_particles(self) -> None:
        """Update particle effects with truecolor"""
        if self.config.particle_effects:
            try:
                particles = self.query_one("#particles", Static)
                theme = self.config.theme.value
                
                # Enhanced particle set for truecolor themes
                if theme.get('truecolor', False):
                    particle_chars = ['✨', '⭐', '💫', '🌟', '✦', '✧', '⚡', '🔥', '💥', '🎆', '🌈', '💎', '🔮']
                else:
                    particle_chars = self.particle_chars
                
                particle = particle_chars[self.current_particle % len(particle_chars)]
                
                # Truecolor particle effects with gradient
                progress_pct = self.current_progress / self.config.total if self.config.total > 0 else 0
                
                if theme.get('truecolor', False):
                    gradient_colors = theme.get('gradient_colors', [theme['rich_bar_color']])
                    color_index = int(progress_pct * (len(gradient_colors) - 1))
                    particle_color = gradient_colors[min(color_index, len(gradient_colors) - 1)]
                    
                    # Apply truecolor styling
                    if progress_pct > 0.8:
                        glow_color = theme.get('glow_color', particle_color)
                        particle_style = f"bold {glow_color}"
                    elif progress_pct > 0.5:
                        particle_style = f"bold {particle_color}"
                    elif progress_pct > 0.2:
                        particle_style = f"bold {particle_color}"
                    else:
                        particle_style = f"dim {particle_color}"
                else:
                    # Fallback particle effects
                    if progress_pct > 0.8:
                        particle_style = f"bright_yellow {particle}"
                    elif progress_pct > 0.5:
                        particle_style = f"bright_cyan {particle}"
                    elif progress_pct > 0.2:
                        particle_style = f"bright_blue {particle}"
                    else:
                        particle_style = f"dim white {particle}"
                
                particles.update(particle_style)
                self.current_particle += 1
            except:
                pass
    
    def check_interactive_input(self) -> None:
        """Check for interactive input (placeholder for future enhancement)"""
        # This would be enhanced with actual input handling
        pass
    
    def update_progress(self, current: int, description: str = None):
        """Update progress with enhanced visual feedback"""
        self.current_progress = current
        self.progress_bar.progress = current
        
        if description:
            try:
                desc = self.query_one("#description", Static)
                theme = self.config.theme.value
                header_style = f"{theme['textual_style']} bold"
                if self.config.glow_effect:
                    header_style += " underline"
                desc.update(f"[{header_style}] {description} [/{header_style}]")
            except:
                pass
    
    def finish(self, message: str = "✅ Complete!"):
        """Finish progress with celebration effects"""
        self.progress_bar.progress = self.config.total
        
        # Update description with celebration
        try:
            desc = self.query_one("#description", Static)
            theme = self.config.theme.value
            celebration_style = f"{theme['textual_style']} bold blink"
            desc.update(f"[{celebration_style}] {message} [/{celebration_style}]")
        except:
            pass
        
        # Update particles with celebration
        if self.config.particle_effects:
            try:
                particles = self.query_one("#particles", Static)
                particles.update("🎉🎊🎉🎊🎉")  # Celebration particles
            except:
                pass

class HybridProgressApp(App):
    """Hybrid Textual app for progress display"""
    
    def __init__(self, config: HybridProgressConfig):
        super().__init__()
        self.config = config
        self.textual_progress = None
        
    def compose(self) -> ComposeResult:
        """Compose the app"""
        theme = self.config.theme.value
        
        # Create header with theme styling
        yield Header(f"[{theme['textual_style']}]🎨 Hybrid Progress System[/{theme['textual_style']}]")
        
        # Main container
        with Container(id="main"):
            yield HybridTextualProgressBar(self.config)
        
        # Footer
        yield Footer()
    
    def on_mount(self) -> None:
        """Called when app is mounted"""
        self.textual_progress = self.query_one(HybridTextualProgressBar)
        self.title = f"Hybrid Progress - {self.config.theme.value['name']}"

class HybridStunningProgressBar:
    """Main hybrid progress bar combining Rich and Textual"""
    
    def __init__(self, config: Optional[HybridProgressConfig] = None):
        self.config = config or HybridProgressConfig()
        self.rich_component = HybridRichProgressBar(self.config)
        self.textual_app = None
        self.textual_thread = None
        self.is_running = False
        
        # Theme management
        self.available_themes = list(HybridProgressTheme)
        self.current_theme_index = 0
        
    def get_random_theme(self) -> HybridProgressTheme:
        """Get a random theme"""
        import random
        return random.choice(self.available_themes)
    
    def set_theme(self, theme: HybridProgressTheme):
        """Set the progress bar theme"""
        self.config.theme = theme
        self.rich_component.config.theme = theme
    
    def next_theme(self) -> HybridProgressTheme:
        """Cycle to next theme"""
        self.current_theme_index = (self.current_theme_index + 1) % len(self.available_themes)
        self.config.theme = self.available_themes[self.current_theme_index]
        return self.config.theme
    
    def start(self):
        """Start hybrid progress bar"""
        self.is_running = True
        
        # Start Rich component
        rich_task_id = self.rich_component.start()
        
        # Start Textual component if enabled
        if self.config.use_textual and TEXTUAL_AVAILABLE:
            self.textual_app = HybridProgressApp(self.config)
            self.textual_thread = threading.Thread(
                target=self._run_textual_app,
                daemon=True
            )
            self.textual_thread.start()
        
        return rich_task_id
    
    def _run_textual_app(self):
        """Run Textual app in separate thread"""
        if self.textual_app:
            asyncio.run(self.textual_app.run_async())
    
    def update(self, advance: int = 1, description: str = None):
        """Update hybrid progress"""
        # Update Rich component
        self.rich_component.update(advance, description)
        
        # Update Textual component
        if self.textual_app and self.textual_app.textual_progress:
            current = self.rich_component.progress.tasks[self.rich_component.task_id].completed if self.rich_component.task_id else 0
            self.textual_app.textual_progress.update_progress(current, description)
    
    def set_progress(self, current: int, description: str = None):
        """Set specific progress value"""
        # Update Rich component
        self.rich_component.set_progress(current, description)
        
        # Update Textual component
        if self.textual_app and self.textual_app.textual_progress:
            self.textual_app.textual_progress.update_progress(current, description)
    
    def finish(self, message: str = "✅ Complete!"):
        """Finish hybrid progress"""
        # Finish Rich component
        self.rich_component.finish(message)
        
        # Finish Textual component
        if self.textual_app and self.textual_app.textual_progress:
            self.textual_app.textual_progress.finish(message)
            # Close Textual app
            self.textual_app.exit()
        
        self.is_running = False

class HybridProgressManager:
    """Manager for multiple hybrid progress bars"""
    
    def __init__(self):
        self.progress_bars: Dict[str, HybridStunningProgressBar] = {}
        self.console = Console() if RICH_AVAILABLE else None
        
    def create_progress(self, name: str, config: HybridProgressConfig = None) -> HybridStunningProgressBar:
        """Create a new hybrid progress bar"""
        progress = HybridStunningProgressBar(config)
        self.progress_bars[name] = progress
        return progress
    
    def get_progress(self, name: str) -> Optional[HybridStunningProgressBar]:
        """Get existing progress bar"""
        return self.progress_bars.get(name)
    
    def create_multi_hybrid_progress(self, configs: List[HybridProgressConfig]):
        """Create multiple hybrid progress bars"""
        if not RICH_AVAILABLE:
            return None
            
        progress_table = Table.grid(padding=1)
        progress_table.add_column()
        
        progress_rows = []
        for config in configs:
            progress = HybridStunningProgressBar(config)
            rich_progress = progress.rich_component.create_rich_progress()
            if rich_progress:
                task_id = rich_progress.add_task(config.description, total=config.total)
                progress_rows.append(rich_progress)
                progress_table.add_row(rich_progress)
        
        live = Live(Align.center(progress_table), console=self.console, refresh_per_second=4)
        return live
    
    def show_hybrid_dashboard(self, title: str, items: List[Dict[str, Any]]):
        """Show hybrid dashboard with Rich and Textual elements"""
        if not RICH_AVAILABLE:
            print(f"\n{title}")
            for item in items:
                print(f"  {item.get('name', 'Unknown')}: {item.get('status', 'Unknown')}")
            return
            
        # Create Rich table
        table = Table(title=title, box=box.ROUNDED)
        table.add_column("Task", style="cyan", no_wrap=True)
        table.add_column("Status", style="green")
        table.add_column("Progress", style="yellow")
        table.add_column("Mode", style="magenta")
        
        for item in items:
            mode = "Hybrid" if item.get('hybrid', False) else "Rich"
            table.add_row(
                item.get('name', 'Unknown'),
                item.get('status', 'Unknown'),
                item.get('progress', '0%'),
                mode
            )
        
        # Create hybrid panel
        panel = Panel(
            table,
            title="🎨 Hybrid Rich+Textual Progress Dashboard",
            border_style="bright_cyan",
            subtitle="Combining the best of both worlds"
        )
        
        self.console.print(panel)

# Global hybrid progress manager
hybrid_progress_manager = HybridProgressManager()

# Convenience functions
def create_hybrid_progress(total: int = 100, description: str = "Processing...", 
                         theme: HybridProgressTheme = HybridProgressTheme.CYBERPUNK_FUSION,
                         use_textual: bool = True, use_rich: bool = True,
                         show_percentage: bool = True, show_time: bool = True, 
                         show_spinner: bool = True, bar_width: int = 80,
                         particle_effects: bool = True, show_time_left: bool = True,
                         interactive: bool = True, glow_effect: bool = True,
                         pulse_animation: bool = True) -> HybridStunningProgressBar:
    """Create an enhanced hybrid Rich+Textual progress bar"""
    config = HybridProgressConfig(
        total=total, 
        description=description, 
        theme=theme,
        use_textual=use_textual,
        use_rich=use_rich,
        show_percentage=show_percentage,
        show_time=show_time,
        show_spinner=show_spinner,
        bar_width=bar_width,
        particle_effects=particle_effects,
        show_time_left=show_time_left,
        interactive=interactive,
        glow_effect=glow_effect,
        pulse_animation=pulse_animation
    )
    return HybridStunningProgressBar(config)

def run_with_hybrid_progress(total: int, description: str, func, *args, 
                            theme: HybridProgressTheme = HybridProgressTheme.CYBERPUNK_FUSION,
                            use_textual: bool = True, use_rich: bool = True, **kwargs):
    """Run a function with hybrid Rich+Textual progress bar"""
    progress = create_hybrid_progress(total, description, theme, use_textual, use_rich)
    progress.start()
    
    try:
        result = func(progress, *args, **kwargs)
        progress.finish("✅ Complete!")
        return result
    except Exception as e:
        progress.finish(f"❌ Error: {e}")
        raise

def show_hybrid_startup():
    """Show stunning hybrid startup animation"""
    if not RICH_AVAILABLE:
        print("🚀 Starting IBLU KALIGPT...")
        return
        
    console = Console()
    
    # Create hybrid startup panel
    startup_text = Text.from_markup(
        "[bold bright_cyan]🔥 IBLU HYBRID RICH+TEXTUAL SYSTEM 🔥\n\n"
        "[bright_yellow]🚀 Initializing Hybrid Visual Interface... 🚀[/bright_yellow]\n\n"
        "[bright_green]✨ Combining Rich and Textual for stunning effects... ✨[/bright_green]\n"
        "[bright_magenta]🎨 Best of both worlds integration complete... 🎨[/bright_magenta]"
    )
    
    panel = Panel(
        Align.center(startup_text),
        box=box.DOUBLE_EDGE,
        border_style="bright_cyan",
        padding=(1, 2),
        title="🎨 Hybrid Progress System",
        subtitle="Rich + Textual Fusion"
    )
    
    console.print(panel)
    time.sleep(2)

# Export main classes and functions
__all__ = [
    'HybridStunningProgressBar',
    'HybridProgressManager',
    'HybridProgressConfig',
    'HybridProgressTheme',
    'hybrid_progress_manager',
    'create_hybrid_progress',
    'run_with_hybrid_progress',
    'show_hybrid_startup',
    'HybridRichProgressBar',
    'HybridTextualProgressBar',
    'HybridProgressApp'
]
