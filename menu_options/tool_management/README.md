# 🛠️ Tool Management - Hacking Toys

## Description
Comprehensive security tools installation and management system.

## Features
- **Batch Installation**: Install all tools at once
- **Individual Installation**: Install tools one-by-one
- **Status Checking**: Monitor installation status
- **Tool Deletion**: Remove unwanted tools
- **Model Management**: Delete AI models

## Available Tools
### Network Tools
- Nmap (Network scanning)
- Netexec (Network execution)
- Hydra (Password cracking)
- Dirb/Gobuster (Directory brute-force)

### Web Tools
- Burp Suite (Web security testing)
- SQLMap (SQL injection testing)
- XSStrike (XSS testing)
- FFuf (Web fuzzing)

### Exploitation
- Metasploit Framework
- Searchsploit
- Exploit Database

## Menu Options
1. **Install ALL Tools** - Recommended for quick setup
2. **Install Individual Tools** - Select specific tools
3. **Check Installation Status** - Verify installed tools
4. **List Tools** - View all available tools
5. **Delete Tools** - Remove specific tools
6. **Delete Models** - Remove AI models
7. **Back to Main Menu** - Return to main interface

## Installation Commands
```bash
# Install all tools
python iblu_assistant.py
# Select option 2, then A

# Install specific tool
python iblu_assistant.py
# Select option 2, then B, then tool number
```

## Configuration
Tools are installed in:
- `/usr/bin/` - System-wide tools
- `~/.local/bin/` - User-specific tools
- `/opt/hexstrike/` - HexStrike tools

## Implementation
Located in `iblu_assistant.py`:
- `handle_hacking_toys()` - Main tool management
- `handle_tools_installation()` - Installation logic
- `handle_delete_models()` - Model deletion
- `handle_tool_management()` - Tool operations
