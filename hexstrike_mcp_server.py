#!/usr/bin/env python3
"""
🔥 HexStrike MCP Server Integration 🔥
🚀 Professional Security Tools MCP Server 🚀
🧠 Real-time vulnerability assessment and penetration testing 🧠
"""

import json
import asyncio
import subprocess
import sys
import os
from pathlib import Path
from typing import Dict, List, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HexStrikeMCPServer:
    """HexStrike MCP Server - Professional Security Tools Integration"""
    
    def __init__(self):
        self.server_process = None
        self.config_file = "hexstrike_mcp_config.json"
        self.tools_directory = "hexstrike_tools"
        self.installed_tools = {}
        self.load_config()
        
        # Ensure tools directory exists
        Path(self.tools_directory).mkdir(exist_ok=True)
    
    def load_config(self):
        """Load HexStrike MCP configuration"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
                logger.info("✅ HexStrike MCP configuration loaded")
            else:
                self.config = {
                    "server_name": "HexStrike MCP Server",
                    "version": "1.0.0",
                    "tools": [
                        "nmap", "metasploit", "burpsuite", "hydra", "john", "hashcat",
                        "sqlmap", "nikto", "dirb", "gobuster", "wfuzz", "skipfish",
                        "cewl", "theharvester", "sublist3r", "amass", "masscan",
                        "zmap", "nuclei", "ffuf", "wfuzz", "hping3", "netcat",
                        "tcpdump", "wireshark", "ettercap", "aircrack-ng", "bully"
                    ],
                    "mcp_port": 8080,
                    "auto_install": True
                }
                self.save_config()
                logger.info("📝 Created default HexStrike MCP configuration")
        except Exception as e:
            logger.error(f"❌ Error loading config: {e}")
            self.config = {"tools": [], "mcp_port": 8080}
    
    def save_config(self):
        """Save HexStrike MCP configuration"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            logger.info("💾 HexStrike MCP configuration saved")
        except Exception as e:
            logger.error(f"❌ Error saving config: {e}")
    
    def check_tool_installed(self, tool_name: str) -> bool:
        """Check if a security tool is installed"""
        try:
            result = subprocess.run(['which', tool_name], 
                                  capture_output=True, text=True)
            return result.returncode == 0
        except Exception:
            return False
    
    def install_tool(self, tool_name: str) -> bool:
        """Install a security tool using apt"""
        try:
            logger.info(f"📦 Installing {tool_name}...")
            
            # Update package list
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            
            # Install the tool
            result = subprocess.run(['sudo', 'apt', 'install', '-y', tool_name], 
                                      capture_output=True, text=True)
            
            if result.returncode == 0:
                logger.info(f"✅ Successfully installed {tool_name}")
                self.installed_tools[tool_name] = True
                return True
            else:
                logger.error(f"❌ Failed to install {tool_name}: {result.stderr}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error installing {tool_name}: {e}")
            return False
    
    def setup_hexstrike_tools(self) -> Dict[str, bool]:
        """Setup HexStrike security tools"""
        logger.info("🔧 Setting up HexStrike security tools...")
        
        installation_status = {}
        
        for tool in self.config.get("tools", []):
            if self.check_tool_installed(tool):
                logger.info(f"✅ {tool} is already installed")
                installation_status[tool] = True
            elif self.config.get("auto_install", True):
                logger.info(f"📦 Installing {tool}...")
                installation_status[tool] = self.install_tool(tool)
            else:
                logger.warning(f"⚠️  {tool} is not installed (auto_install disabled)")
                installation_status[tool] = False
        
        return installation_status
    
    def get_tool_info(self, tool_name: str) -> Dict[str, Any]:
        """Get detailed information about a tool"""
        tool_info = {
            "nmap": {
                "name": "Nmap",
                "description": "Network discovery and security auditing",
                "category": "reconnaissance",
                "usage": "nmap <target>",
                "examples": ["nmap -sS target.com", "nmap -p- 1-65535 target.com"],
                "install": "sudo apt install nmap"
            },
            "metasploit": {
                "name": "Metasploit Framework",
                "description": "Penetration testing framework",
                "category": "exploitation",
                "usage": "msfconsole",
                "examples": ["msfconsole", "msfven windows/meterpreter/reverse_tcp"],
                "install": "sudo apt install metasploit-framework"
            },
            "burpsuite": {
                "name": "Burp Suite",
                "description": "Web application security testing",
                "category": "web",
                "usage": "burpsuite",
                "examples": ["burpsuite", "java -jar burpsuite.jar"],
                "install": "sudo apt install burpsuite"
            },
            "hydra": {
                "name": "Hydra",
                "description": "Password cracking tool",
                "category": "authentication",
                "usage": "hydra -l users.txt target ssh",
                "examples": ["hydra -l users.txt target ssh", "hydra -P 80 target http-get /"],
                "install": "sudo apt install hydra"
            },
            "sqlmap": {
                "name": "SQLMap",
                "description": "SQL injection testing tool",
                "category": "database",
                "usage": "sqlmap -u target.com",
                "examples": ["sqlmap -u target.com", "sqlmap -u target.com --dbs"],
                "install": "sudo apt install sqlmap"
            },
            "nikto": {
                "name": "Nikto",
                "description": "Web server scanner",
                "category": "web",
                "usage": "nikto -h target.com",
                "examples": ["nikto -h target.com", "nikto -h target.com -p 8080"],
                "install": "sudo apt install nikto"
            }
        }
        
        return tool_info.get(tool_name.lower(), {
            "name": tool_name,
            "description": "Security tool",
            "category": "general",
            "usage": f"{tool_name} [options]",
            "examples": [f"{tool_name} --help"],
            "install": f"sudo apt install {tool_name}"
        })
    
    def start_mcp_server(self) -> bool:
        """Start the MCP server"""
        try:
            logger.info("🚀 Starting HexStrike MCP Server...")
            
            # Setup tools first
            tool_status = self.setup_hexstrike_tools()
            
            logger.info(f"🔗 MCP Server will start on port {self.config['mcp_port']}")
            logger.info("🛡️ Ready to serve HexStrike security tools!")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error starting MCP server: {e}")
            return False
    
    def get_available_commands(self) -> List[str]:
        """Get list of available commands with descriptions"""
        commands = []
        for tool in self.config.get("tools", []):
            tool_info = self.get_tool_info(tool)
            commands.append(f"/{tool.lower()} - {tool_info['description']}")
        
        # Add general commands
        commands.extend([
            "/help - Show this help message",
            "/tools - List all available tools",
            "/install <tool> - Install a specific tool",
            "/status - Show MCP server status",
            "/scan <target> - Quick scan with nmap",
            "/payload <type> - Generate payload",
            "/pentest <target> - Run automated pentest"
            "/mcp_status - Check MCP connection"
        ])
        
        return commands

if __name__ == "__main__":
    server = HexStrikeMCPServer()
    server.start_mcp_server()
