#!/usr/bin/env python3
"""
🎨 Stunning Rich Progress Bar System for IBLU KALIGPT
Beautiful, animated progress bars with multiple themes and effects
"""

import time
import threading
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
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# Colorama for fallback
try:
    from colorama import Fore, Style as ColoramaStyle
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

class ProgressTheme(Enum):
    """Beautiful progress bar themes"""
    
    CYBERPUNK = {
        'name': 'Cyberpunk',
        'bar_color': 'bright_cyan',
        'text_color': 'white',
        'spinner': 'dots',
        'style': 'bold',
        'description': '🔮 Cyberpunk Theme'
    }
    
    NEON_PURPLE = {
        'name': 'Neon Purple',
        'bar_color': 'bright_magenta',
        'text_color': 'white',
        'spinner': 'pipe',
        'style': 'bold',
        'description': '💜 Neon Purple Theme'
    }
    
    MATRIX_GREEN = {
        'name': 'Matrix Green',
        'bar_color': 'bright_green',
        'text_color': 'white',
        'spinner': 'dots2',
        'style': 'bold',
        'description': '💚 Matrix Green Theme'
    }
    
    FIRE_ORANGE = {
        'name': 'Fire Orange',
        'bar_color': 'bright_yellow',
        'text_color': 'white',
        'spinner': 'line',
        'style': 'bold',
        'description': '🔥 Fire Orange Theme'
    }
    
    OCEAN_BLUE = {
        'name': 'Ocean Blue',
        'bar_color': 'bright_blue',
        'text_color': 'white',
        'spinner': 'dots8',
        'style': 'bold',
        'description': '🌊 Ocean Blue Theme'
    }
    
    GALAXY_PURPLE = {
        'name': 'Galaxy Purple',
        'bar_color': 'purple',
        'text_color': 'white',
        'spinner': 'moon',
        'style': 'bold',
        'description': '🌌 Galaxy Purple Theme'
    }
    
    RAINBOW = {
        'name': 'Rainbow',
        'bar_color': 'cyan',
        'text_color': 'white',
        'spinner': 'bouncingBar',
        'style': 'bold',
        'description': '🌈 Rainbow Theme'
    }
    
    GOLD = {
        'name': 'Gold',
        'bar_color': 'yellow',
        'text_color': 'white',
        'spinner': 'star',
        'style': 'bold',
        'description': '⭐ Gold Theme'
    }

@dataclass
class ProgressConfig:
    """Configuration for progress bars"""
    total: int = 100
    description: str = "Processing..."
    theme: ProgressTheme = ProgressTheme.CYBERPUNK
    show_percentage: bool = True
    show_time: bool = True
    show_spinner: bool = True
    bar_width: int = 40
    animated: bool = True

class StunningRichProgressBar:
    """Stunning Rich Progress Bar with multiple themes and effects"""
    
    def __init__(self, config: Optional[ProgressConfig] = None):
        self.config = config or ProgressConfig()
        self.console = Console() if RICH_AVAILABLE else None
        self.progress = None
        self.task_id = None
        self.live = None
        self.is_running = False
        
        # Progress characters for fallback
        self.progress_chars = {
            'complete': '█',
            'partial': '▓',
            'light': '▒',
            'empty': '░'
        }
        
        # Theme management
        self.available_themes = list(ProgressTheme)
        self.current_theme_index = 0
        
    def get_random_theme(self) -> ProgressTheme:
        """Get a random theme"""
        import random
        return random.choice(self.available_themes)
    
    def set_theme(self, theme: ProgressTheme):
        """Set the progress bar theme"""
        self.config.theme = theme
    
    def next_theme(self) -> ProgressTheme:
        """Cycle to next theme"""
        self.current_theme_index = (self.current_theme_index + 1) % len(self.available_themes)
        self.config.theme = self.available_themes[self.current_theme_index]
        return self.config.theme
    
    def create_progress_bar(self) -> Optional[Progress]:
        """Create a Rich progress bar with custom styling"""
        if not RICH_AVAILABLE:
            return None
            
        theme = self.config.theme.value
        
        # Create custom spinner
        spinner = SpinnerColumn(
            spinner_name=theme['spinner'],
            style=f"{theme['style']} {theme['text_color']}"
        ) if self.config.show_spinner else None
        
        # Create text column
        text = TextColumn(
            f"[{theme['style']} {theme['text_color']}]{self.config.description}[/{theme['style']} {theme['text_color']}]",
            style=Style(color=theme['text_color'], bold=True)
        )
        
        # Create custom bar with enhanced styling
        bar = BarColumn(
            bar_width=self.config.bar_width,
            style=Style(color=theme['bar_color'], bold=True),
            complete_style=Style(color=theme['bar_color'], bold=True),
            finished_style=Style(color=theme['bar_color'], bold=True),
            pulse_style=Style(color=theme['bar_color'], dim=True)
        )
        
        # Create percentage column
        percentage = TextColumn("[progress.percentage]{task.percentage:>3.0f}%") if self.config.show_percentage else None
        
        # Create time column
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
    
    def start(self, description: str = None) -> TaskID:
        """Start the progress bar"""
        if description:
            self.config.description = description
            
        if RICH_AVAILABLE and self.console:
            self.progress = self.create_progress_bar()
            if self.progress:
                self.task_id = self.progress.add_task(
                    self.config.description,
                    total=self.config.total
                )
                self.progress.start()
                self.is_running = True
                return self.task_id
        
        # Fallback mode
        self.is_running = True
        return None
    
    def update(self, advance: int = 1, description: str = None):
        """Update progress"""
        if description:
            self.config.description = description
            
        if RICH_AVAILABLE and self.progress and self.task_id:
            self.progress.update(
                self.task_id,
                advance=advance,
                description=self.config.description
            )
        else:
            # Fallback rendering
            self._render_fallback()
    
    def set_progress(self, current: int, description: str = None):
        """Set specific progress value"""
        if description:
            self.config.description = description
            
        if RICH_AVAILABLE and self.progress and self.task_id:
            completed = current - self.progress.tasks[self.task_id].completed
            self.progress.update(
                self.task_id,
                completed=current,
                description=self.config.description
            )
        else:
            # Fallback rendering
            self._render_fallback_progress(current)
    
    def finish(self, message: str = "✅ Complete!"):
        """Finish the progress bar"""
        if RICH_AVAILABLE and self.progress:
            # Update to 100%
            if self.task_id:
                self.progress.update(self.task_id, completed=self.config.total)
            
            # Show completion message
            theme = self.config.theme.value
            self.console.print(f"[{theme['style']} {theme['bar_color']}]{message}[/{theme['style']} {theme['bar_color']}]")
            
            self.progress.stop()
        else:
            # Fallback completion
            self._render_fallback_complete(message)
        
        self.is_running = False
    
    def _render_fallback(self):
        """Fallback progress rendering for terminals without Rich"""
        if not COLORAMA_AVAILABLE:
            print(f"\r{self.config.description}...", end="", flush=True)
            return
            
        # Simple fallback
        print(f"\r{Fore.LIGHTCYAN_EX}⏳ {self.config.description}...{ColoramaStyle.RESET_ALL}", end="", flush=True)
    
    def _render_fallback_progress(self, current: int):
        """Render fallback progress bar"""
        if not COLORAMA_AVAILABLE:
            print(f"\r[{current}/{self.config.total}] {self.config.description}", end="", flush=True)
            return
            
        percentage = (current / self.config.total) * 100 if self.config.total > 0 else 0
        bar_width = 30
        filled_length = int(bar_width * percentage / 100)
        
        theme = self.config.theme.value
        color_map = {
            'bright_cyan': Fore.LIGHTCYAN_EX,
            'bright_magenta': Fore.LIGHTMAGENTA_EX,
            'bright_green': Fore.LIGHTGREEN_EX,
            'bright_yellow': Fore.LIGHTYELLOW_EX,
            'bright_blue': Fore.LIGHTBLUE_EX,
            'purple': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'yellow': Fore.LIGHTYELLOW_EX
        }
        
        color = color_map.get(theme['bar_color'], Fore.LIGHTCYAN_EX)
        chars = self.progress_chars
        
        # Build bar
        bar = ""
        for i in range(bar_width):
            if i < filled_length:
                if i == filled_length - 1:
                    bar += chars['partial']
                elif i >= filled_length - 3:
                    bar += chars['light']
                else:
                    bar += chars['complete']
            else:
                bar += chars['empty']
        
        print(f"\r{color}█{ColoramaStyle.RESET_ALL} {self.config.description} [{color}{bar}{ColoramaStyle.RESET_ALL}] {percentage:.1f}%", end="", flush=True)
    
    def _render_fallback_complete(self, message: str):
        """Render fallback completion"""
        if COLORAMA_AVAILABLE:
            print(f"\r{Fore.LIGHTGREEN_EX}{message}{ColoramaStyle.RESET_ALL}")
        else:
            print(f"\r{message}")

class ProgressManager:
    """Manager for multiple progress bars"""
    
    def __init__(self):
        self.progress_bars: Dict[str, StunningRichProgressBar] = {}
        self.console = Console() if RICH_AVAILABLE else None
        
    def create_progress(self, name: str, config: ProgressConfig = None) -> StunningRichProgressBar:
        """Create a new progress bar"""
        progress = StunningRichProgressBar(config)
        self.progress_bars[name] = progress
        return progress
    
    def get_progress(self, name: str) -> Optional[StunningRichProgressBar]:
        """Get existing progress bar"""
        return self.progress_bars.get(name)
    
    def create_multi_progress(self, configs: List[ProgressConfig]) -> Live:
        """Create multiple progress bars in a live display"""
        if not RICH_AVAILABLE:
            return None
            
        progress_table = Table.grid(padding=1)
        progress_table.add_column()
        
        progress_rows = []
        for config in configs:
            progress = StunningRichProgressBar(config)
            progress_bar = progress.create_progress_bar()
            if progress_bar:
                task_id = progress_bar.add_task(config.description, total=config.total)
                progress_rows.append(progress_bar)
                progress_table.add_row(progress_bar)
        
        live = Live(Align.center(progress_table), console=self.console, refresh_per_second=4)
        return live
    
    def show_progress_panel(self, title: str, items: List[Dict[str, Any]]):
        """Show a panel with progress information"""
        if not RICH_AVAILABLE:
            print(f"\n{title}")
            for item in items:
                print(f"  {item.get('name', 'Unknown')}: {item.get('status', 'Unknown')}")
            return
            
        table = Table(title=title, box=box.ROUNDED)
        table.add_column("Task", style="cyan", no_wrap=True)
        table.add_column("Status", style="green")
        table.add_column("Progress", style="yellow")
        
        for item in items:
            table.add_row(
                item.get('name', 'Unknown'),
                item.get('status', 'Unknown'),
                item.get('progress', '0%')
            )
        
        panel = Panel(table, title="🎯 Progress Dashboard", border_style="bright_blue")
        self.console.print(panel)

# Global progress manager
progress_manager = ProgressManager()

# Convenience functions for easy usage
def create_progress(total: int = 100, description: str = "Processing...", theme: ProgressTheme = ProgressTheme.CYBERPUNK) -> StunningRichProgressBar:
    """Create a stunning progress bar"""
    config = ProgressConfig(total=total, description=description, theme=theme)
    return StunningRichProgressBar(config)

def run_with_progress(total: int, description: str, func, *args, theme: ProgressTheme = ProgressTheme.CYBERPUNK, **kwargs):
    """Run a function with progress bar"""
    progress = create_progress(total, description, theme)
    progress.start()
    
    try:
        result = func(progress, *args, **kwargs)
        progress.finish("✅ Complete!")
        return result
    except Exception as e:
        progress.finish(f"❌ Error: {e}")
        raise

def show_stunning_startup():
    """Show stunning startup animation"""
    if not RICH_AVAILABLE:
        print("🚀 Starting IBLU KALIGPT...")
        return
        
    console = Console()
    
    # Create startup panel
    startup_text = Text.from_markup(
        "[bold bright_cyan]🔥 IBLU PROFESSIONAL HACKING ASSISTANT 🔥\n\n"
        "[bright_yellow]🚀 Initializing Advanced Security Platform... 🚀[/bright_yellow]\n\n"
        "[bright_green]✨ Loading stunning visual effects... ✨[/bright_green]"
    )
    
    panel = Panel(
        Align.center(startup_text),
        box=box.DOUBLE_EDGE,
        border_style="bright_cyan",
        padding=(1, 2)
    )
    
    console.print(panel)
    time.sleep(1)

# Export main classes and functions
__all__ = [
    'StunningRichProgressBar',
    'ProgressManager', 
    'ProgressConfig',
    'ProgressTheme',
    'progress_manager',
    'create_progress',
    'run_with_progress',
    'show_stunning_startup'
]
