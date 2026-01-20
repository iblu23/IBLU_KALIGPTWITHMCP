import time
import sys

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

def print_slow(text, delay=0.001):
    """Print text with a typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_enhanced_banner(animated=False, style="default"):
    """
    Display enhanced banner with multiple style options
    
    Args:
        animated: Enable typing animation effect
        style: Choose style - "default", "neon", "matrix", "fire", "cyber"
    """
    
    if COLORAMA_AVAILABLE:
        # Style configurations
        styles = {
            "default": {
                "border": Fore.RED,
                "title": Style.BRIGHT + Fore.YELLOW,
                "subtitle": Fore.CYAN,
                "tagline": Style.BRIGHT + Fore.MAGENTA,
                "shadow": Fore.BLACK
            },
            "neon": {
                "border": Fore.MAGENTA,
                "title": Style.BRIGHT + Fore.CYAN,
                "subtitle": Style.BRIGHT + Fore.MAGENTA,
                "tagline": Style.BRIGHT + Fore.YELLOW,
                "shadow": Fore.BLUE
            },
            "matrix": {
                "border": Fore.GREEN,
                "title": Style.BRIGHT + Fore.GREEN,
                "subtitle": Fore.LIGHTGREEN_EX,
                "tagline": Style.BRIGHT + Fore.WHITE,
                "shadow": Fore.BLACK
            },
            "fire": {
                "border": Fore.RED,
                "title": Style.BRIGHT + Fore.YELLOW,
                "subtitle": Fore.RED,
                "tagline": Style.BRIGHT + Fore.RED,
                "shadow": Fore.BLACK
            },
            "cyber": {
                "border": Fore.BLUE,
                "title": Style.BRIGHT + Fore.CYAN,
                "subtitle": Fore.LIGHTBLUE_EX,
                "tagline": Style.BRIGHT + Fore.MAGENTA,
                "shadow": Fore.BLUE
            }
        }
        
        colors = styles.get(style, styles["default"])
        
        # Enhanced banner with gradient effect and better spacing
        lines = [
            f"{colors['border']}╔{'═'*78}╗",
            f"{colors['border']}║{' '*78}║",
            f"{colors['border']}║ {colors['title']}██╗  ██╗ █████╗  ██████╗██╗  ██╗    ████████╗██╗  ██╗███████╗ {colors['border']}║",
            f"{colors['border']}║ {colors['title']}██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ╚══██╔══╝██║  ██║██╔════╝ {colors['border']}║",
            f"{colors['border']}║ {colors['title']}███████║███████║██║     █████╔╝        ██║   ███████║█████╗   {colors['border']}║",
            f"{colors['border']}║ {colors['title']}██╔══██║██╔══██║██║     ██╔═██╗        ██║   ██╔══██║██╔══╝   {colors['border']}║",
            f"{colors['border']}║ {colors['title']}██║  ██║██║  ██║╚██████╗██║  ██╗       ██║   ██║  ██║███████╗ {colors['border']}║",
            f"{colors['border']}║ {colors['title']}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚══════╝ {colors['border']}║",
            f"{colors['border']}║{' '*78}║",
            f"{colors['border']}║ {colors['subtitle']}{' '*20}██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗  {colors['border']}║",
            f"{colors['border']}║ {colors['subtitle']}{' '*20}██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗ {colors['border']}║",
            f"{colors['border']}║ {colors['subtitle']}{' '*20}██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║ {colors['border']}║",
            f"{colors['border']}║ {colors['subtitle']}{' '*20}██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║ {colors['border']}║",
            f"{colors['border']}║ {colors['subtitle']}{' '*20}╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝ {colors['border']}║",
            f"{colors['border']}║ {colors['subtitle']}{' '*20} ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝  {colors['border']}║",
            f"{colors['border']}║{' '*78}║",
            f"{colors['border']}║{' '*21}{colors['tagline']}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{colors['border']}{' '*22}║",
            f"{colors['border']}║{' '*21}{colors['tagline']}┃  🔥🔥🔥 HACK THE WORLD 🔥🔥🔥  ┃{colors['border']}{' '*22}║",
            f"{colors['border']}║{' '*21}{colors['tagline']}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{colors['border']}{' '*22}║",
            f"{colors['border']}║{' '*78}║",
            f"{colors['border']}╚{'═'*78}╝"
        ]
    else:
        # Fallback without colorama
        lines = [
            "╔" + "═"*78 + "╗",
            "║" + " "*78 + "║",
            "║ ██╗  ██╗ █████╗  ██████╗██╗  ██╗    ████████╗██╗  ██╗███████╗ ║",
            "║ ██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ╚══██╔══╝██║  ██║██╔════╝ ║",
            "║ ███████║███████║██║     █████╔╝        ██║   ███████║█████╗   ║",
            "║ ██╔══██║██╔══██║██║     ██╔═██╗        ██║   ██╔══██║██╔══╝   ║",
            "║ ██║  ██║██║  ██║╚██████╗██║  ██╗       ██║   ██║  ██║███████╗ ║",
            "║ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚══════╝ ║",
            "║" + " "*78 + "║",
            "║                     ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗  ║",
            "║                     ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗ ║",
            "║                     ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║ ║",
            "║                     ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║ ║",
            "║                     ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝ ║",
            "║                      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝  ║",
            "║" + " "*78 + "║",
            "║                     ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓        ║",
            "║                     ┃  🔥🔥🔥 HACK THE WORLD 🔥🔥🔥  ┃        ║",
            "║                     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛        ║",
            "║" + " "*78 + "║",
            "╚" + "═"*78 + "╝"
        ]
    
    # Display banner
    if animated:
        for line in lines:
            print_slow(line, delay=0.003)
    else:
        for line in lines:
            print(line)

# Example usage:
if __name__ == "__main__":
    print("\n" * 2)
    
    # Display with different styles
    print("=" * 80)
    print("STYLE: CYBER (ANIMATED)")
    print("=" * 80)
    display_enhanced_banner(animated=True, style="cyber")
    
    time.sleep(1)
    print("\n" * 2)
    
    print("=" * 80)
    print("STYLE: MATRIX")
    print("=" * 80)
    display_enhanced_banner(animated=False, style="matrix")
    
    time.sleep(1)
    print("\n" * 2)
    
    print("=" * 80)
    print("STYLE: NEON")
    print("=" * 80)
    display_enhanced_banner(animated=False, style="neon")
    
    time.sleep(1)
    print("\n" * 2)
    
    print("=" * 80)
    print("STYLE: FIRE")
    print("=" * 80)
    display_enhanced_banner(animated=False, style="fire")