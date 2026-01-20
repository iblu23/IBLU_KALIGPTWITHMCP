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
    from textual.widgets import ProgressBar, Static, Footer, Header
    from textual.reactive import reactive
    from textual.binding import Binding
    from textual.screen import ModalScreen
    from textual.widget import Widget
    from textual.coordinate import Coordinate
    from textual import on
    TEXTUAL_AVAILABLE = True
except ImportError:
    TEXTUAL_AVAILABLE = False

# Colorama for fallback
try:
    from colorama import Fore, Style as ColoramaStyle
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

class HybridProgressTheme(Enum):
    """Hybrid themes combining Rich and Textual visual effects"""
    
    CYBERPUNK_FUSION = {
        'name': 'Cyberpunk Fusion',
        'rich_bar_color': 'bright_cyan',
        'rich_text_color': 'white',
        'rich_spinner': 'dots',
        'textual_style': 'bold cyan',
        'textual_background': 'on black',
        'description': '🔮 Cyberpunk Rich+Textual Fusion',
        'particle_effect': 'digital_rain'
    }
    
    NEON_MATRIX = {
        'name': 'Neon Matrix',
        'rich_bar_color': 'bright_green',
        'rich_text_color': 'white',
        'rich_spinner': 'dots2',
        'textual_style': 'bold green',
        'textual_background': 'on black',
        'description': '💚 Neon Matrix Rich+Textual',
        'particle_effect': 'matrix_drops'
    }
    
    FIRE_PLASMA = {
        'name': 'Fire Plasma',
        'rich_bar_color': 'bright_yellow',
        'rich_text_color': 'white',
        'rich_spinner': 'line',
        'textual_style': 'bold yellow',
        'textual_background': 'on black',
        'description': '🔥 Fire Plasma Rich+Textual',
        'particle_effect': 'flames'
    }
    
    OCEAN_WAVE = {
        'name': 'Ocean Wave',
        'rich_bar_color': 'bright_blue',
        'rich_text_color': 'white',
        'rich_spinner': 'dots8',
        'textual_style': 'bold blue',
        'textual_background': 'on black',
        'description': '🌊 Ocean Wave Rich+Textual',
        'particle_effect': 'waves'
    }
    
    GALAXY_NEBULA = {
        'name': 'Galaxy Nebula',
        'rich_bar_color': 'bright_magenta',
        'rich_text_color': 'white',
        'rich_spinner': 'moon',
        'textual_style': 'bold magenta',
        'textual_background': 'on black',
        'description': '🌌 Galaxy Nebula Rich+Textual',
        'particle_effect': 'stars'
    }
    
    RAINBOW_PRISM = {
        'name': 'Rainbow Prism',
        'rich_bar_color': 'cyan',
        'rich_text_color': 'white',
        'rich_spinner': 'bouncingBar',
        'textual_style': 'bold rainbow',
        'textual_background': 'on black',
        'description': '🌈 Rainbow Prism Rich+Textual',
        'particle_effect': 'prisms'
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
    bar_width: int = 40
    animated: bool = True
    use_textual: bool = True
    use_rich: bool = True
    particle_effects: bool = True

class HybridRichProgressBar:
    """Rich component of hybrid progress bar"""
    
    def __init__(self, config: HybridProgressConfig):
        self.config = config
        self.console = Console() if RICH_AVAILABLE else None
        self.progress = None
        self.task_id = None
        
    def create_rich_progress(self):
        """Create Rich progress bar component"""
        if not RICH_AVAILABLE or not self.config.use_rich:
            return None
            
        theme = self.config.theme.value
        
        # Custom spinner
        spinner = SpinnerColumn(
            spinner_name=theme['rich_spinner'],
            style=f"bold {theme['rich_text_color']}"
        ) if self.config.show_spinner else None
        
        # Text column
        text = TextColumn(
            f"[bold {theme['rich_text_color']}]{self.config.description}[/bold {theme['rich_text_color']}]",
            style=Style(color=theme['rich_text_color'], bold=True)
        )
        
        # Custom bar
        bar = BarColumn(
            bar_width=self.config.bar_width,
            style=Style(color=theme['rich_bar_color'], bold=True),
            complete_style=Style(color=theme['rich_bar_color'], bold=True),
            finished_style=Style(color=theme['rich_bar_color'], bold=True),
            pulse_style=Style(color=theme['rich_bar_color'], dim=True)
        )
        
        # Additional columns
        percentage = TextColumn("[progress.percentage]{task.percentage:>3.0f}%") if self.config.show_percentage else None
        time_elapsed = TimeElapsedColumn() if self.config.show_time else None
        
        # Build columns list
        columns = []
        if spinner:
            columns.append(spinner)
        columns.append(text)
        columns.append(bar)
        if percentage:
            columns.append(percentage)
        if time_elapsed:
            columns.append(time_elapsed)
        
        # Create progress object
        progress = Progress(
            *columns,
            console=self.console,
            transient=False,
            refresh_per_second=10 if self.config.animated else 1
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
    """Textual component of hybrid progress bar"""
    
    def __init__(self, config: HybridProgressConfig):
        super().__init__()
        self.config = config
        self.current_progress = 0
        self.theme = config.theme.value
        
    def compose(self) -> ComposeResult:
        """Compose Textual widget"""
        yield Static(f"[{self.theme['textual_style']}] {self.config.description} [/{self.theme['textual_style']}]", id="description")
        yield ProgressBar(total=self.config.total, show_percentage=self.config.show_percentage, id="progress")
        if self.config.show_time:
            yield Static("00:00:00", id="timer")
    
    def on_mount(self) -> None:
        """Called when widget is mounted"""
        self.progress_bar = self.query_one("#progress", ProgressBar)
        if self.config.show_time:
            self.timer = self.query_one("#timer", Static)
        self.start_time = time.time()
        self.set_interval(0.1, self.update_timer)
    
    def update_timer(self) -> None:
        """Update timer display"""
        if self.config.show_time and hasattr(self, 'timer'):
            elapsed = int(time.time() - self.start_time)
            hours, remainder = divmod(elapsed, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.timer.update(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    
    def update_progress(self, current: int, description: str = None):
        """Update progress"""
        self.current_progress = current
        self.progress_bar.progress = current
        
        if description:
            self.description = self.query_one("#description", Static)
            theme = self.config.theme.value
            self.description.update(f"[{theme['textual_style']}] {description} [/{theme['textual_style']}]")
    
    def finish(self, message: str = "✅ Complete!"):
        """Finish progress"""
        self.progress_bar.progress = self.config.total
        theme = self.config.theme.value
        self.description = self.query_one("#description", Static)
        self.description.update(f"[{theme['textual_style']}] {message} [/{theme['textual_style']}]")

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
                         show_spinner: bool = True) -> HybridStunningProgressBar:
    """Create a hybrid Rich+Textual progress bar"""
    config = HybridProgressConfig(
        total=total, 
        description=description, 
        theme=theme,
        use_textual=use_textual,
        use_rich=use_rich,
        show_percentage=show_percentage,
        show_time=show_time,
        show_spinner=show_spinner
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
