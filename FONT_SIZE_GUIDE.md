# Terminal Font Size Guide

## How to Increase Font Size by 10%

Terminal font size is controlled by your terminal emulator, not Python code. Here's how to increase it:

### For GNOME Terminal (Default on many Linux systems):
1. Open Terminal
2. Click **Edit** → **Preferences**
3. Select your profile
4. Go to **Text** tab
5. Uncheck "Use the system fixed width font"
6. Click the font button
7. Increase size by ~10% (e.g., if current is 10, change to 11)
8. Click **Close**

### For Terminator:
1. Right-click in terminal
2. Select **Preferences**
3. Go to **Profiles** tab
4. Under **General** section, find **Font**
5. Click the font button and increase size
6. Close preferences

### For Konsole (KDE):
1. Go to **Settings** → **Edit Current Profile**
2. Click **Appearance** tab
3. Click **Choose** next to Font
4. Increase font size
5. Click **OK**

### For Tilix:
1. Click hamburger menu (☰)
2. Select **Preferences**
3. Go to **Profiles**
4. Select **Default** profile
5. Click **Text** section
6. Adjust **Custom font** size
7. Close preferences

### For Alacritty (config file):
Edit `~/.config/alacritty/alacritty.yml`:
```yaml
font:
  size: 11.0  # Increase from 10.0 to 11.0 (10% increase)
```

### For Kitty (config file):
Edit `~/.config/kitty/kitty.conf`:
```
font_size 11.0
```

### Quick Terminal Commands:
Some terminals support runtime font size changes:
- **Ctrl + Shift + Plus (+)** - Increase font size
- **Ctrl + Minus (-)** - Decrease font size
- **Ctrl + 0** - Reset to default size

## Current Terminal Detection

To find out which terminal you're using:
```bash
echo $TERM
ps -o comm= -p $PPID
```

## Recommended Font Sizes

For IBLU Assistant's beautiful interface:
- **Small screens (laptop):** 10-11pt
- **Medium screens (desktop):** 11-12pt  
- **Large screens (4K):** 12-14pt

The ASCII art and box characters look best with monospace fonts like:
- **DejaVu Sans Mono**
- **Fira Code**
- **JetBrains Mono**
- **Source Code Pro**
