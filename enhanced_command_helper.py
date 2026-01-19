#!/usr/bin/env python3
"""
🔥 Enhanced IBLU Command Helper v2.2 🔥
🚀 Consolidated command completion and suggestion system 🚀
📋 Advanced command helper with autocomplete and typing assistant 📋
🎨 Modern UI with dropdown menus and chat history 🎨
🧠 Intelligent typing assistant with real-time suggestions 🧠
"""

import os
import sys
import json
import time
import readline
import atexit
import subprocess
import threading
from typing import List, Dict, Optional, Tuple, Any
from pathlib import Path
from datetime import datetime
from collections import defaultdict

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

class EnhancedCommandHelper:
    """
    🔥 Enhanced IBLU Command Helper v2.2 🔥
    🚀 Consolidated command completion and suggestion system 🚀
    📋 Advanced command helper with autocomplete and typing assistant 📋
    🎨 Modern UI with dropdown menus and chat history 🎨
    🧠 Intelligent typing assistant with real-time suggestions 🧠
    """
    
    # Enhanced command definitions with numbered commands
    COMMANDS = {
        # Basic Commands (1-10)
        "1": {
            "category": "basic",
            "description": "Show complete command help",
            "usage": "1 or /1",
            "examples": ["1", "/1"],
            "icon": "📚",
            "number": 1
        },
        "2": {
            "category": "basic", 
            "description": "Display system information",
            "usage": "2 or /2",
            "examples": ["2", "/2"],
            "icon": "💻",
            "number": 2
        },
        "3": {
            "category": "basic",
            "description": "Check network connectivity",
            "usage": "3 or /3",
            "examples": ["3", "/3"],
            "icon": "🌐",
            "number": 3
        },
        "4": {
            "category": "basic",
            "description": "List available tools",
            "usage": "4 or /4",
            "examples": ["4", "/4"],
            "icon": "🛠️",
            "number": 4
        },
        "5": {
            "category": "basic",
            "description": "Show configuration",
            "usage": "5 or /5",
            "examples": ["5", "/5"],
            "icon": "⚙️",
            "number": 5
        },
        "6": {
            "category": "basic",
            "description": "MCP server status",
            "usage": "6 or /6",
            "examples": ["6", "/6"],
            "icon": "🔗",
            "number": 6
        },
        "7": {
            "category": "basic",
            "description": "Test API connections",
            "usage": "7 or /7",
            "examples": ["7", "/7"],
            "icon": "🔌",
            "number": 7
        },
        "8": {
            "category": "basic",
            "description": "Show conversation history",
            "usage": "8 or /8",
            "examples": ["8", "/8"],
            "icon": "📜",
            "number": 8
        },
        "9": {
            "category": "basic",
            "description": "Clear history",
            "usage": "9 or /9",
            "examples": ["9", "/9"],
            "icon": "🧹",
            "number": 9
        },
        "10": {
            "category": "basic",
            "description": "Save conversation",
            "usage": "10 or /10",
            "examples": ["10", "/10"],
            "icon": "💾",
            "number": 10
        },
        
        # RECONNAISSANCE (11-30)
        "11": {
            "category": "reconnaissance",
            "description": "Quick port scan (top 1000 ports)",
            "usage": "11 or /11 <target>",
            "examples": ["11 example.com", "/11 192.168.1.1"],
            "icon": "🔍",
            "number": 11
        },
        "12": {
            "category": "reconnaissance",
            "description": "Full port scan (all 65535 ports)",
            "usage": "12 or /12 <target>",
            "examples": ["12 example.com", "/12 192.168.1.1"],
            "icon": "🗺️",
            "number": 12
        },
        "13": {
            "category": "reconnaissance",
            "description": "Service version detection scan",
            "usage": "13 or /13 <target>",
            "examples": ["13 example.com", "/13 192.168.1.1"],
            "icon": "🔧",
            "number": 13
        },
        "14": {
            "category": "reconnaissance",
            "description": "OS detection and fingerprinting",
            "usage": "14 or /14 <target>",
            "examples": ["14 example.com", "/14 192.168.1.1"],
            "icon": "💻",
            "number": 14
        },
        "15": {
            "category": "reconnaissance",
            "description": "UDP port scan (common ports)",
            "usage": "15 or /15 <target>",
            "examples": ["15 example.com", "/15 192.168.1.1"],
            "icon": "🌐",
            "number": 15
        },
        "16": {
            "category": "reconnaissance",
            "description": "Subdomain enumeration with DNS",
            "usage": "16 or /16 <target>",
            "examples": ["16 example.com", "/16 192.168.1.1"],
            "icon": "🔍",
            "number": 16
        },
        "17": {
            "category": "reconnaissance",
            "description": "DNS zone transfer attempt",
            "usage": "17 or /17 <target>",
            "examples": ["17 example.com", "/17 192.168.1.1"],
            "icon": "📋",
            "number": 17
        },
        "18": {
            "category": "reconnaissance",
            "description": "WHOIS information gathering",
            "usage": "18 or /18 <target>",
            "examples": ["18 example.com", "/18 192.168.1.1"],
            "icon": "📊",
            "number": 18
        },
        "19": {
            "category": "reconnaissance",
            "description": "HTTP header analysis",
            "usage": "19 or /19 <target>",
            "examples": ["19 example.com", "/19 192.168.1.1"],
            "icon": "🌐",
            "number": 19
        },
        "20": {
            "category": "reconnaissance",
            "description": "SSL/TLS certificate analysis",
            "usage": "20 or /20 <target>",
            "examples": ["20 example.com", "/20 192.168.1.1"],
            "icon": "🔒",
            "number": 20
        },
        "21": {
            "category": "reconnaissance",
            "description": "Web technology fingerprinting",
            "usage": "21 or /21 <target>",
            "examples": ["21 example.com", "/21 192.168.1.1"],
            "icon": "🎨",
            "number": 21
        },
        "22": {
            "category": "reconnaissance",
            "description": "WAF detection and identification",
            "usage": "22 or /22 <target>",
            "examples": ["22 example.com", "/22 192.168.1.1"],
            "icon": "🛡️",
            "number": 22
        },
        "23": {
            "category": "reconnaissance",
            "description": "DNS record enumeration (A, MX, NS, TXT)",
            "usage": "23 or /23 <target>",
            "examples": ["23 example.com", "/23 192.168.1.1"],
            "icon": "📋",
            "number": 23
        },
        "24": {
            "category": "reconnaissance",
            "description": "Reverse DNS lookup",
            "usage": "24 or /24 <target>",
            "examples": ["24 example.com", "/24 192.168.1.1"],
            "icon": "🔄",
            "number": 24
        },
        "25": {
            "category": "reconnaissance",
            "description": "Email server enumeration",
            "usage": "25 or /25 <target>",
            "examples": ["25 example.com", "/25 192.168.1.1"],
            "icon": "📧",
            "number": 25
        },
        "26": {
            "category": "reconnaissance",
            "description": "FTP anonymous login check",
            "usage": "26 or /26 <target>",
            "examples": ["26 example.com", "/26 192.168.1.1"],
            "icon": "📁",
            "number": 26
        },
        "27": {
            "category": "reconnaissance",
            "description": "SNMP community string enumeration",
            "usage": "27 or /27 <target>",
            "examples": ["27 example.com", "/27 192.168.1.1"],
            "icon": "🔐",
            "number": 27
        },
        "28": {
            "category": "reconnaissance",
            "description": "LDAP directory enumeration",
            "usage": "28 or /28 <target>",
            "examples": ["28 example.com", "/28 192.168.1.1"],
            "icon": "📋",
            "number": 28
        },
        "29": {
            "category": "reconnaissance",
            "description": "SMB share enumeration",
            "usage": "29 or /29 <target>",
            "examples": ["29 example.com", "/29 192.168.1.1"],
            "icon": "📂",
            "number": 29
        },
        "30": {
            "category": "reconnaissance",
            "description": "RDP service detection",
            "usage": "30 or /30 <target>",
            "examples": ["30 example.com", "/30 192.168.1.1"],
            "icon": "🖥️",
            "number": 30
        },
        
        # VULNERABILITY SCANNING (31-50)
        "31": {
            "category": "vulnerability",
            "description": "SQL injection vulnerability scan",
            "usage": "31 or /31 <target>",
            "examples": ["31 example.com", "/31 192.168.1.1"],
            "icon": "💉",
            "number": 31
        },
        "32": {
            "category": "vulnerability",
            "description": "XSS vulnerability detection",
            "usage": "32 or /32 <target>",
            "examples": ["32 example.com", "/32 192.168.1.1"],
            "icon": "🎯",
            "number": 32
        },
        "33": {
            "category": "vulnerability",
            "description": "Directory traversal testing",
            "usage": "33 or /33 <target>",
            "examples": ["33 example.com", "/33 192.168.1.1"],
            "icon": "📁",
            "number": 33
        },
        "34": {
            "category": "vulnerability",
            "description": "File inclusion vulnerability check",
            "usage": "34 or /34 <target>",
            "examples": ["34 example.com", "/34 192.168.1.1"],
            "icon": "📄",
            "number": 34
        },
        "35": {
            "category": "vulnerability",
            "description": "Authentication bypass testing",
            "usage": "35 or /35 <target>",
            "examples": ["35 example.com", "/35 192.168.1.1"],
            "icon": "🔓",
            "number": 35
        },
        "36": {
            "category": "vulnerability",
            "description": "CSRF vulnerability detection",
            "usage": "36 or /36 <target>",
            "examples": ["36 example.com", "/36 192.168.1.1"],
            "icon": "🔄",
            "number": 36
        },
        "37": {
            "category": "vulnerability",
            "description": "Command injection testing",
            "usage": "37 or /37 <target>",
            "examples": ["37 example.com", "/37 192.168.1.1"],
            "icon": "⚡",
            "number": 37
        },
        "38": {
            "category": "vulnerability",
            "description": "XXE vulnerability scan",
            "usage": "38 or /38 <target>",
            "examples": ["38 example.com", "/38 192.168.1.1"],
            "icon": "📄",
            "number": 38
        },
        "39": {
            "category": "vulnerability",
            "description": "SSRF vulnerability detection",
            "usage": "39 or /39 <target>",
            "examples": ["39 example.com", "/39 192.168.1.1"],
            "icon": "🌐",
            "number": 39
        },
        "40": {
            "category": "vulnerability",
            "description": "Buffer overflow testing",
            "usage": "40 or /40 <target>",
            "examples": ["40 example.com", "/40 192.168.1.1"],
            "icon": "💥",
            "number": 40
        },
        "41": {
            "category": "vulnerability",
            "description": "Race condition testing",
            "usage": "41 or /41 <target>",
            "examples": ["41 example.com", "/41 192.168.1.1"],
            "icon": "⚡",
            "number": 41
        },
        "42": {
            "category": "vulnerability",
            "description": "Insecure deserialization scan",
            "usage": "42 or /42 <target>",
            "examples": ["42 example.com", "/42 192.168.1.1"],
            "icon": "📦",
            "number": 42
        },
        "43": {
            "category": "vulnerability",
            "description": "Cryptographic weakness check",
            "usage": "43 or /43 <target>",
            "examples": ["43 example.com", "/43 192.168.1.1"],
            "icon": "🔐",
            "number": 43
        },
        "44": {
            "category": "vulnerability",
            "description": "Session management flaws",
            "usage": "44 or /44 <target>",
            "examples": ["44 example.com", "/44 192.168.1.1"],
            "icon": "🎫",
            "number": 44
        },
        "45": {
            "category": "vulnerability",
            "description": "Access control bypass testing",
            "usage": "45 or /45 <target>",
            "examples": ["45 example.com", "/45 192.168.1.1"],
            "icon": "🚪",
            "number": 45
        },
        "46": {
            "category": "vulnerability",
            "description": "Information disclosure check",
            "usage": "46 or /46 <target>",
            "examples": ["46 example.com", "/46 192.168.1.1"],
            "icon": "📢",
            "number": 46
        },
        "47": {
            "category": "vulnerability",
            "description": "Business logic flaw testing",
            "usage": "47 or /47 <target>",
            "examples": ["47 example.com", "/47 192.168.1.1"],
            "icon": "🧠",
            "number": 47
        },
        "48": {
            "category": "vulnerability",
            "description": "API security testing",
            "usage": "48 or /48 <target>",
            "examples": ["48 example.com", "/48 192.168.1.1"],
            "icon": "🔌",
            "number": 48
        },
        "49": {
            "category": "vulnerability",
            "description": "Mobile app security scan",
            "usage": "49 or /49 <target>",
            "examples": ["49 example.com", "/49 192.168.1.1"],
            "icon": "📱",
            "number": 49
        },
        "50": {
            "category": "vulnerability",
            "description": "IoT device vulnerability scan",
            "usage": "50 or /50 <target>",
            "examples": ["50 example.com", "/50 192.168.1.1"],
            "icon": "🌐",
            "number": 50
        },
        
        # EXPLOITATION & PAYLOADS (51-70)
        "51": {
            "category": "exploitation",
            "description": "Generate reverse shell payload",
            "usage": "51 or /51 [ip] [port]",
            "examples": ["51", "/51 192.168.1.100 4444"],
            "icon": "💣",
            "number": 51
        },
        "52": {
            "category": "exploitation",
            "description": "Generate bind shell payload",
            "usage": "52 or /52 [port]",
            "examples": ["52", "/52 4444"],
            "icon": "🔗",
            "number": 52
        },
        "53": {
            "category": "exploitation",
            "description": "Generate meterpreter payload",
            "usage": "53 or /53 [ip] [port]",
            "examples": ["53", "/53 192.168.1.100 4444"],
            "icon": "🎯",
            "number": 53
        },
        "54": {
            "category": "exploitation",
            "description": "Generate custom payload",
            "usage": "54 or /54 <type>",
            "examples": ["54 python", "/54 bash"],
            "icon": "🔧",
            "number": 54
        },
        "55": {
            "category": "exploitation",
            "description": "Create web shell payload",
            "usage": "55 or /55 <type>",
            "examples": ["55 php", "/55 asp"],
            "icon": "🌐",
            "number": 55
        },
        "56": {
            "category": "exploitation",
            "description": "Generate SQL injection payload",
            "usage": "56 or /56 <target>",
            "examples": ["56 login", "/56 search"],
            "icon": "💉",
            "number": 56
        },
        "57": {
            "category": "exploitation",
            "description": "Create XSS payload",
            "usage": "57 or /57 <type>",
            "examples": ["57 reflected", "/57 stored"],
            "icon": "🎯",
            "number": 57
        },
        "58": {
            "category": "exploitation",
            "description": "Generate buffer overflow exploit",
            "usage": "58 or /58 <target>",
            "examples": ["58 service", "/58 application"],
            "icon": "💥",
            "number": 58
        },
        "59": {
            "category": "exploitation",
            "description": "Create privilege escalation exploit",
            "usage": "59 or /59 <target>",
            "examples": ["59 linux", "/59 windows"],
            "icon": "⬆️",
            "number": 59
        },
        "60": {
            "category": "exploitation",
            "description": "Generate LFI/RFI payload",
            "usage": "60 or /60 <type>",
            "examples": ["60 lfi", "/60 rfi"],
            "icon": "📁",
            "number": 60
        },
        "61": {
            "category": "exploitation",
            "description": "Create authentication bypass payload",
            "usage": "61 or /61 <target>",
            "examples": ["61 admin", "/61 login"],
            "icon": "🔓",
            "number": 61
        },
        "62": {
            "category": "exploitation",
            "description": "Generate CSRF exploit",
            "usage": "62 or /62 <target>",
            "examples": ["62 form", "/62 api"],
            "icon": "🔄",
            "number": 62
        },
        "63": {
            "category": "exploitation",
            "description": "Create command injection payload",
            "usage": "63 or /63 <target>",
            "examples": ["63 system", "/63 exec"],
            "icon": "⚡",
            "number": 63
        },
        "64": {
            "category": "exploitation",
            "description": "Generate XXE exploit",
            "usage": "64 or /64 <target>",
            "examples": ["64 xml", "/64 soap"],
            "icon": "📄",
            "number": 64
        },
        "65": {
            "category": "exploitation",
            "description": "Create SSRF payload",
            "usage": "65 or /65 <target>",
            "examples": ["65 internal", "/65 metadata"],
            "icon": "🌐",
            "number": 65
        },
        "66": {
            "category": "exploitation",
            "description": "Generate deserialization exploit",
            "usage": "66 or /66 <format>",
            "examples": ["66 java", "/66 python"],
            "icon": "📦",
            "number": 66
        },
        "67": {
            "category": "exploitation",
            "description": "Generate ransomware simulation payload",
            "usage": "67 or /67 <target>",
            "examples": ["67 files", "/67 system"],
            "icon": "🔒",
            "number": 67
        },
        "68": {
            "category": "exploitation",
            "description": "Generate keylogger payload",
            "usage": "68 or /68 <type>",
            "examples": ["68 hardware", "/68 software"],
            "icon": "⌨️",
            "number": 68
        },
        "69": {
            "category": "exploitation",
            "description": "Generate botnet client payload",
            "usage": "69 or /69 <c2>",
            "examples": ["69 irc", "/69 http"],
            "icon": "🤖",
            "number": 69
        },
        "70": {
            "category": "exploitation",
            "description": "Generate custom backdoor",
            "usage": "70 or /70 <type>",
            "examples": ["70 persistent", "/70 stealth"],
            "icon": "🚪",
            "number": 70
        },
        
        # POST-EXPLOITATION (71-85)
        "71": {
            "category": "post_exploitation",
            "description": "System enumeration post-compromise",
            "usage": "71 or /71",
            "examples": ["71", "/71"],
            "icon": "🔍",
            "number": 71
        },
        "72": {
            "category": "post_exploitation",
            "description": "User and group enumeration",
            "usage": "72 or /72",
            "examples": ["72", "/72"],
            "icon": "👥",
            "number": 72
        },
        "73": {
            "category": "post_exploitation",
            "description": "Process enumeration and analysis",
            "usage": "73 or /73",
            "examples": ["73", "/73"],
            "icon": "⚙️",
            "number": 73
        },
        "74": {
            "category": "post_exploitation",
            "description": "Network configuration discovery",
            "usage": "74 or /74",
            "examples": ["74", "/74"],
            "icon": "🌐",
            "number": 74
        },
        "75": {
            "category": "post_exploitation",
            "description": "Registry key enumeration (Windows)",
            "usage": "75 or /75",
            "examples": ["75", "/75"],
            "icon": "📋",
            "number": 75
        },
        "76": {
            "category": "post_exploitation",
            "description": "File system search for sensitive data",
            "usage": "76 or /76 <pattern>",
            "examples": ["76 passwords", "/76 keys"],
            "icon": "📁",
            "number": 76
        },
        "77": {
            "category": "post_exploitation",
            "description": "Password hash extraction",
            "usage": "77 or /77",
            "examples": ["77", "/77"],
            "icon": "🔐",
            "number": 77
        },
        "78": {
            "category": "post_exploitation",
            "description": "Service configuration analysis",
            "usage": "78 or /78",
            "examples": ["78", "/78"],
            "icon": "⚙️",
            "number": 78
        },
        "79": {
            "category": "post_exploitation",
            "description": "Scheduled task enumeration",
            "usage": "79 or /79",
            "examples": ["79", "/79"],
            "icon": "📅",
            "number": 79
        },
        "80": {
            "category": "post_exploitation",
            "description": "Log file analysis",
            "usage": "80 or /80",
            "examples": ["80", "/80"],
            "icon": "📜",
            "number": 80
        },
        "81": {
            "category": "post_exploitation",
            "description": "Memory dump analysis",
            "usage": "81 or /81",
            "examples": ["81", "/81"],
            "icon": "💾",
            "number": 81
        },
        "82": {
            "category": "post_exploitation",
            "description": "Network traffic capture",
            "usage": "82 or /82",
            "examples": ["82", "/82"],
            "icon": "📡",
            "number": 82
        },
        "83": {
            "category": "post_exploitation",
            "description": "Persistence mechanism setup",
            "usage": "83 or /83 <type>",
            "examples": ["83 registry", "/83 cron"],
            "icon": "🔄",
            "number": 83
        },
        "84": {
            "category": "post_exploitation",
            "description": "Privilege escalation attempt",
            "usage": "84 or /84",
            "examples": ["84", "/84"],
            "icon": "⬆️",
            "number": 84
        },
        "85": {
            "category": "post_exploitation",
            "description": "Lateral movement preparation",
            "usage": "85 or /85",
            "examples": ["85", "/85"],
            "icon": "➡️",
            "number": 85
        },
        
        # DEFENSE & EVASION (86-100)
        "86": {
            "category": "defense_evasion",
            "description": "Cover tracks and clear logs",
            "usage": "86 or /86",
            "examples": ["86", "/86"],
            "icon": "🧹",
            "number": 86
        },
        "87": {
            "category": "defense_evasion",
            "description": "Create stealth backdoor",
            "usage": "87 or /87 <type>",
            "examples": ["87 persistent", "/87 hidden"],
            "icon": "🚪",
            "number": 87
        },
        "88": {
            "category": "defense_evasion",
            "description": "Implement anti-forensics",
            "usage": "88 or /88",
            "examples": ["88", "/88"],
            "icon": "🔍",
            "number": 88
        },
        "89": {
            "category": "defense_evasion",
            "description": "Encryption setup for data",
            "usage": "89 or /89 <algorithm>",
            "examples": ["89 aes", "/89 rsa"],
            "icon": "🔐",
            "number": 89
        },
        "90": {
            "category": "defense_evasion",
            "description": "Create covert channel",
            "usage": "90 or /90 <protocol>",
            "examples": ["90 dns", "/90 icmp"],
            "icon": "📡",
            "number": 90
        },
        "91": {
            "category": "defense_evasion",
            "description": "Generate fake traffic for noise",
            "usage": "91 or /91 <type>",
            "examples": ["91 web", "/91 dns"],
            "icon": "🌐",
            "number": 91
        },
        "92": {
            "category": "defense_evasion",
            "description": "Implement process hiding",
            "usage": "92 or /92",
            "examples": ["92", "/92"],
            "icon": "👻",
            "number": 92
        },
        "93": {
            "category": "defense_evasion",
            "description": "Create rootkit components",
            "usage": "93 or /93 <type>",
            "examples": ["93 kernel", "/93 userland"],
            "icon": "🎭",
            "number": 93
        },
        "94": {
            "category": "defense_evasion",
            "description": "Setup encrypted communication",
            "usage": "94 or /94 <protocol>",
            "examples": ["94 tls", "/94 ssh"],
            "icon": "🔒",
            "number": 94
        },
        "95": {
            "category": "defense_evasion",
            "description": "Generate diversion tactics",
            "usage": "95 or /95 <type>",
            "examples": ["95 decoy", "/95 misdirection"],
            "icon": "🎭",
            "number": 95
        },
        "96": {
            "category": "defense_evasion",
            "description": "Implement timestamp manipulation",
            "usage": "96 or /96",
            "examples": ["96", "/96"],
            "icon": "⏰",
            "number": 96
        },
        "97": {
            "category": "defense_evasion",
            "description": "Create fileless malware",
            "usage": "97 or /97 <type>",
            "examples": ["97 powershell", "/97 wmi"],
            "icon": "👻",
            "number": 97
        },
        "98": {
            "category": "defense_evasion",
            "description": "Setup living-off-the-land techniques",
            "usage": "98 or /98",
            "examples": ["98", "/98"],
            "icon": "🌍",
            "number": 98
        },
        "99": {
            "category": "defense_evasion",
            "description": "Generate anti-analysis code",
            "usage": "99 or /99 <technique>",
            "examples": ["99 sandbox", "/99 debugger"],
            "icon": "🛡️",
            "number": 99
        },
        "100": {
            "category": "defense_evasion",
            "description": "Complete system cleanup",
            "usage": "100 or /100",
            "examples": ["100", "/100"],
            "icon": "🧹",
            "number": 100
        },
        
        # Traditional Commands
        "help": {
            "category": "basic",
            "description": "Show help for commands",
            "usage": "help [command]",
            "examples": ["help", "help scan"],
            "icon": "📚"
        },
        "clear": {
            "category": "basic", 
            "description": "Clear terminal screen",
            "usage": "clear",
            "examples": ["clear"],
            "icon": "🧹"
        },
        "exit": {
            "category": "basic",
            "description": "Exit IBLU assistant",
            "usage": "exit",
            "examples": ["exit"],
            "icon": "🚪"
        },
        "history": {
            "category": "basic",
            "description": "Show command history",
            "usage": "history [count]",
            "examples": ["history", "history 10"],
            "icon": "📜"
        },
        "save": {
            "category": "basic",
            "description": "Save conversation to file",
            "usage": "save <filename>",
            "examples": ["save session.txt"],
            "icon": "💾"
        },
        "load": {
            "category": "basic",
            "description": "Load conversation from file",
            "usage": "load <filename>",
            "examples": ["load session.txt"],
            "icon": "📂"
        },
        "providers": {
            "category": "basic",
            "description": "List available AI providers",
            "usage": "providers",
            "examples": ["providers"],
            "icon": "🤖"
        },
        "status": {
            "category": "basic",
            "description": "Show system status",
            "usage": "status",
            "examples": ["status"],
            "icon": "📊"
        },
        
        # Provider Switching Commands
        "perplexity": {
            "category": "provider",
            "description": "Switch to Perplexity AI",
            "usage": "perplexity",
            "examples": ["perplexity"],
            "icon": "🧠"
        },
        "openai": {
            "category": "provider",
            "description": "Switch to OpenAI",
            "usage": "openai",
            "examples": ["openai"],
            "icon": "🤖"
        },
        "gemini": {
            "category": "provider",
            "description": "Switch to Gemini",
            "usage": "gemini",
            "examples": ["gemini"],
            "icon": "💎"
        },
        "mistral": {
            "category": "provider",
            "description": "Switch to Mistral",
            "usage": "mistral",
            "examples": ["mistral"],
            "icon": "🌊"
        },
        
        # MCP Server Management
        "mcp_connect": {
            "category": "mcp",
            "description": "Connect to Hexstrike MCP server",
            "usage": "mcp_connect",
            "examples": ["mcp_connect"],
            "icon": "🔗"
        },
        "mcp_disconnect": {
            "category": "mcp",
            "description": "Disconnect from MCP server",
            "usage": "mcp_disconnect",
            "examples": ["mcp_disconnect"],
            "icon": "🔌"
        },
        "mcp_status": {
            "category": "mcp",
            "description": "Check MCP connection status",
            "usage": "mcp_status",
            "examples": ["mcp_status"],
            "icon": "📊"
        },
        
        # Scanning Commands
        "scan": {
            "category": "scanning",
            "description": "Perform security scan on target",
            "usage": "scan <target> <scan_type>",
            "examples": [
                "scan example.com port",
                "scan 192.168.1.1 subdomain",
                "scan target.com directory",
                "scan example.com nmap",
                "scan target.com dns",
                "scan example.com web"
            ],
            "icon": "🔍"
        },
        "nmap": {
            "category": "scanning",
            "description": "Perform Nmap scan on target",
            "usage": "nmap <target> [options]",
            "examples": [
                "nmap example.com",
                "nmap 192.168.1.1 -p 80,443"
            ],
            "icon": "🗺️"
        },
        
        # Payload Commands
        "payload": {
            "category": "payload",
            "description": "Generate security payload",
            "usage": "payload <type> [options]",
            "examples": [
                "payload reverse_shell 192.168.1.100 4444",
                "payload bind_shell",
                "payload meterpreter 192.168.1.100 4444",
                "payload custom"
            ],
            "icon": "💣"
        },
        
        # Automated Testing
        "autopentest": {
            "category": "automated",
            "description": "Run complete automated penetration test",
            "usage": "autopentest <target>",
            "examples": ["autopentest example.com"],
            "icon": "🤖"
        },
        "menu": {
            "category": "ui",
            "description": "Show interactive command menu",
            "usage": "menu",
            "examples": ["menu"],
            "icon": "📋"
        },
        "commands": {
            "category": "ui",
            "description": "Show all commands in menu format",
            "usage": "commands",
            "examples": ["commands"],
            "icon": "📝"
        },
        "chat": {
            "category": "ui",
            "description": "Show chat history",
            "usage": "chat [count]",
            "examples": ["chat", "chat 5"],
            "icon": "💬"
        }
    }
    
    CATEGORIES = {
        "basic": {"name": "Basic Commands", "icon": "🔧", "color": Fore.BLUE},
        "reconnaissance": {"name": "Reconnaissance", "icon": "🔍", "color": Fore.GREEN},
        "vulnerability": {"name": "Vulnerability Scanning", "icon": "🛡️", "color": Fore.RED},
        "exploitation": {"name": "Exploitation", "icon": "�", "color": Fore.RED},
        "post_exploitation": {"name": "Post-Exploitation", "icon": "🎯", "color": Fore.MAGENTA},
        "defense_evasion": {"name": "Defense & Evasion", "icon": "🛡️", "color": Fore.YELLOW},
        "scanning": {"name": "Scanning Tools", "icon": "�", "color": Fore.GREEN},
        "payload": {"name": "Payload Generation", "icon": "💣", "color": Fore.RED},
        "mcp": {"name": "MCP Integration", "icon": "🔗", "color": Fore.MAGENTA},
        "provider": {"name": "AI Providers", "icon": "🤖", "color": Fore.CYAN},
        "automated": {"name": "Automated Testing", "icon": "🤖", "color": Fore.BLUE},
        "ui": {"name": "Interface", "icon": "🎨", "color": Fore.YELLOW}
    }
    
    def __init__(self):
        """Initialize the enhanced command helper"""
        self.history_file = Path.home() / ".iblu_command_history"
        self.chat_history_file = Path.home() / ".iblu_chat_history"
        self.command_history: List[str] = []
        self.chat_history: List[Dict[str, str]] = []
        self.command_stats: Dict[str, int] = defaultdict(int)
        self.max_history = 1000
        self.typing_suggestions = []
        self.last_input = ""
        
        # Load histories
        self._load_history()
        self._load_chat_history()
        
        # Setup readline for autocomplete
        self._setup_readline()
    
    def _setup_readline(self):
        """Setup readline for command completion"""
        try:
            # Set up tab completion
            readline.set_completer(self._completer)
            readline.parse_and_bind("tab: complete")
            
            # Set up history
            readline.set_history_length(self.max_history)
            
            # Load history from file
            if self.history_file.exists():
                readline.read_history_file(str(self.history_file))
            
            # Save history on exit
            atexit.register(self._save_history)
            
        except ImportError:
            # Readline not available on this platform
            pass
    
    def _completer(self, text: str, state: int) -> Optional[str]:
        """Enhanced tab completion function"""
        options = []
        
        # Complete command names (including numbered commands)
        for cmd in self.COMMANDS.keys():
            if cmd.startswith(text.lower()):
                options.append(cmd)
        
        # Complete with slash prefix for numbered commands
        if text.startswith("/"):
            for cmd in self.COMMANDS.keys():
                if cmd.isdigit() and cmd.startswith(text[1:]):
                    options.append("/" + cmd)
        
        # Complete subcommands
        if text in self.COMMANDS:
            cmd_info = self.COMMANDS[text]
            if "subcommands" in cmd_info:
                options.extend(cmd_info["subcommands"])
        
        # Return the appropriate option
        if state < len(options):
            return options[state]
        return None
    
    def _load_history(self):
        """Load command history from file"""
        try:
            if self.history_file.exists():
                with open(self.history_file, 'r') as f:
                    self.command_history = [line.strip() for line in f.readlines() if line.strip()]
        except Exception:
            self.command_history = []
    
    def _load_chat_history(self):
        """Load chat history from file"""
        try:
            if self.chat_history_file.exists():
                with open(self.chat_history_file, 'r') as f:
                    self.chat_history = json.load(f)
        except Exception:
            self.chat_history = []
    
    def _save_history(self):
        """Save command history to file"""
        try:
            with open(self.history_file, 'w') as f:
                for cmd in self.command_history[-self.max_history:]:
                    f.write(f"{cmd}\n")
        except Exception:
            pass
    
    def _save_chat_history(self):
        """Save chat history to file"""
        try:
            with open(self.chat_history_file, 'w') as f:
                json.dump(self.chat_history[-self.max_history:], f, indent=2)
        except Exception:
            pass
    
    def _colorize(self, text: str, color: str = "") -> str:
        """Apply color to text if colorama is available"""
        if COLORAMA_AVAILABLE and color:
            return f"{color}{text}{Style.RESET_ALL}"
        return text
    
    def add_to_history(self, command: str):
        """Add command to history"""
        if command and command.strip():
            self.command_history.append(command.strip())
            
            # Update command statistics
            base_cmd = command.strip().split()[0].lstrip('/')
            self.command_stats[base_cmd] += 1
            
            # Keep history size manageable
            if len(self.command_history) > self.max_history:
                self.command_history = self.command_history[-self.max_history:]
    
    def add_to_chat_history(self, role: str, content: str, provider: str = "unknown"):
        """Add message to chat history"""
        message = {
            "role": role,
            "content": content,
            "provider": provider,
            "timestamp": datetime.now().isoformat()
        }
        self.chat_history.append(message)
        
        # Keep chat history size manageable
        if len(self.chat_history) > self.max_history:
            self.chat_history = self.chat_history[-self.max_history:]
        
        # Save chat history
        self._save_chat_history()
    
    def get_typing_suggestions(self, current_input: str, max_suggestions: int = 3) -> List[str]:
        """Get intelligent typing suggestions"""
        suggestions = []
        current_lower = current_input.lower()
        
        # Handle numbered commands with slash
        if current_lower.startswith("/") and current_lower[1:].isdigit():
            return [current_lower]
        
        # Partial command matching
        for cmd in self.COMMANDS.keys():
            if cmd.startswith(current_lower):
                suggestions.append(cmd)
        
        # Handle slash prefix for numbered commands
        if current_lower.startswith("/") and len(current_lower) > 1:
            cmd_part = current_lower[1:]
            for cmd in self.COMMANDS.keys():
                if cmd.isdigit() and cmd.startswith(cmd_part):
                    suggestions.append("/" + cmd)
        
        # Prioritize recently used commands
        recent_commands = [cmd.split()[0].lstrip('/') for cmd in self.command_history[-20:]]
        for recent_cmd in recent_commands:
            if recent_cmd in self.COMMANDS and recent_cmd.startswith(current_lower) and recent_cmd not in suggestions:
                suggestions.insert(0, recent_cmd)
        
        return suggestions[:max_suggestions]
    
    def show_typing_assistant(self, current_input: str):
        """Show typing assistant suggestions"""
        suggestions = self.get_typing_suggestions(current_input)
        
        if suggestions and current_input:
            print(f"\n💡 {self._colorize('Typing Assistant Suggestions:', Fore.CYAN)}")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"  {self._colorize(str(i), Fore.YELLOW)}. {self._colorize(suggestion, Fore.GREEN)}")
            print()
    
    def get_suggestions(self, query: str, max_results: int = 5, context: str = "") -> List[str]:
        """Get command suggestions based on query"""
        suggestions = []
        query_lower = query.lower()
        
        # Handle numbered commands
        if query_lower.isdigit():
            if query_lower in self.COMMANDS:
                suggestions.append(query_lower)
            suggestions.append("/" + query_lower)
        
        # Handle slash prefix for numbered commands
        if query_lower.startswith("/") and query_lower[1:].isdigit():
            cmd_num = query_lower[1:]
            if cmd_num in self.COMMANDS:
                suggestions.append(query_lower)
        
        # Exact matches first
        for cmd in self.COMMANDS.keys():
            if cmd.startswith(query_lower):
                suggestions.append(cmd)
        
        # Partial matches
        for cmd, info in self.COMMANDS.items():
            if query_lower in cmd.lower() and cmd not in suggestions:
                suggestions.append(cmd)
        
        # Category matches
        for cmd, info in self.COMMANDS.items():
            if query_lower in info.get("category", "").lower() and cmd not in suggestions:
                suggestions.append(cmd)
        
        return suggestions[:max_results]
    
    def show_command_help(self, command: str = None):
        """Show help for commands"""
        if command:
            # Handle numbered commands with slash
            if command.startswith("/") and command[1:].isdigit():
                command = command[1:]
            
            # Show help for specific command
            if command in self.COMMANDS:
                cmd_info = self.COMMANDS[command]
                category_info = self.CATEGORIES.get(cmd_info["category"], {})
                
                print(f"\n{self._colorize(cmd_info['icon'] + ' ' + command.upper(), Fore.YELLOW)}")
                print(f"{self._colorize('Category:', Fore.CYAN)} {category_info.get('name', cmd_info['category'])}")
                print(f"{self._colorize('Description:', Fore.CYAN)} {cmd_info['description']}")
                print(f"{self._colorize('Usage:', Fore.CYAN)} {cmd_info['usage']}")
                print(f"{self._colorize('Examples:', Fore.CYAN)}")
                for example in cmd_info.get("examples", []):
                    print(f"  • {self._colorize(example, Fore.GREEN)}")
                
                if "subcommands" in cmd_info:
                    print(f"{self._colorize('Subcommands:', Fore.CYAN)}")
                    for subcmd in cmd_info["subcommands"]:
                        print(f"  • {self._colorize(subcmd, Fore.GREEN)}")
                print()
            else:
                print(f"{self._colorize('❌ Command not found:', Fore.RED)} {command}")
                print(f"{self._colorize('Available commands:', Fore.CYAN)} {', '.join(list(self.COMMANDS.keys())[:10])}...")
        else:
            # Show help for all commands
            self._show_all_commands_help()
    
    def _show_all_commands_help(self):
        """Show help for all commands organized by category"""
        print(f"\n{self._colorize('🔥 ENHANCED IBLU COMMAND HELPER v2.2 🔥', Fore.YELLOW)}")
        print(f"{self._colorize('=' * 70, Fore.BLUE)}\n")
        
        for category_id, category_info in self.CATEGORIES.items():
            category_commands = []
            
            # Find commands in this category
            for cmd, cmd_info in self.COMMANDS.items():
                if cmd_info.get("category") == category_id:
                    category_commands.append((cmd, cmd_info))
            
            if category_commands:
                print(f"{self._colorize(category_info['icon'] + ' ' + category_info['name'] + ':', category_info.get('color', Fore.WHITE))}")
                
                for cmd, cmd_info in sorted(category_commands, key=lambda x: x[0]):
                    display_cmd = cmd
                    if cmd.isdigit():
                        display_cmd = f"{cmd} (or /{cmd})"
                    print(f"  {self._colorize(cmd_info['icon'], Fore.WHITE)} {self._colorize(display_cmd.ljust(20), Fore.GREEN)} - {cmd_info['description']}")
                print()
        
        print(f"{self._colorize('💡 Enhanced Features:', Fore.CYAN)}")
        print(f"  • Type {self._colorize('help <command>', Fore.GREEN)} for detailed command help")
        print(f"  • Use {self._colorize('Tab', Fore.YELLOW)} key for command completion")
        print(f"  • Press {self._colorize('↑/↓', Fore.YELLOW)} arrows to navigate command history")
        print(f"  • Type {self._colorize('history', Fore.GREEN)} to see command history")
        print(f"  • Use {self._colorize('numbered commands', Fore.GREEN)} (1-100) for quick access")
        print(f"  • Try {self._colorize('menu', Fore.GREEN)} for interactive command menu")
        print(f"  • Type {self._colorize('chat', Fore.GREEN)} to see conversation history")
        print()
    
    def show_history(self, count: int = 10):
        """Show command history"""
        if not self.command_history:
            print(f"{self._colorize('📝 No command history available', Fore.CYAN)}")
            return
        
        print(f"\n{self._colorize('📜 COMMAND HISTORY', Fore.YELLOW)}")
        print(f"{self._colorize('=' * 50, Fore.BLUE)}")
        
        # Show last 'count' commands
        recent_commands = self.command_history[-count:]
        for i, cmd in enumerate(recent_commands, 1):
            print(f"  {self._colorize(str(i).rjust(3), Fore.CYAN)}. {self._colorize(cmd, Fore.GREEN)}")
        
        print(f"\n{self._colorize(f'Total commands in history: {len(self.command_history)}', Fore.BLUE)}")
        print()
    
    def show_chat_history(self, count: int = 10):
        """Show chat history"""
        if not self.chat_history:
            print(f"{self._colorize('💬 No chat history available', Fore.CYAN)}")
            return
        
        print(f"\n{self._colorize('💬 CHAT HISTORY', Fore.YELLOW)}")
        print(f"{self._colorize('=' * 50, Fore.BLUE)}")
        
        # Show last 'count' messages
        recent_messages = self.chat_history[-count:]
        for i, msg in enumerate(recent_messages, 1):
            role_color = Fore.GREEN if msg["role"] == "user" else Fore.CYAN
            role_icon = "👤" if msg["role"] == "user" else "🤖"
            timestamp = msg.get("timestamp", "")[:19]  # Show only date and time
            print(f"  {self._colorize(str(i).rjust(3), Fore.YELLOW)}. {role_icon} {self._colorize(msg['role'].upper(), role_color)} [{timestamp}]")
            print(f"     {self._colorize(msg['content'][:100] + '...' if len(msg['content']) > 100 else msg['content'], Fore.WHITE)}")
        
        print(f"\n{self._colorize(f'Total messages in history: {len(self.chat_history)}', Fore.BLUE)}")
        print()
    
    def show_stats(self):
        """Show command usage statistics"""
        if not self.command_stats:
            print(f"{self._colorize('📊 No command statistics available', Fore.CYAN)}")
            return
        
        print(f"\n{self._colorize('📊 COMMAND USAGE STATISTICS', Fore.YELLOW)}")
        print(f"{self._colorize('=' * 50, Fore.BLUE)}")
        
        # Sort by usage count
        sorted_stats = sorted(self.command_stats.items(), key=lambda x: x[1], reverse=True)
        
        for cmd, count in sorted_stats[:15]:  # Show top 15
            cmd_info = self.COMMANDS.get(cmd, {})
            icon = cmd_info.get("icon", "🔧")
            print(f"  {icon} {self._colorize(cmd.ljust(20), Fore.GREEN)}: {self._colorize(str(count), Fore.CYAN)} uses")
        
        total_commands = sum(self.command_stats.values())
        print(f"\n{self._colorize(f'Total commands executed: {total_commands}', Fore.BLUE)}")
        print(f"{self._colorize(f'Unique commands used: {len(self.command_stats)}', Fore.BLUE)}")
        print()
    
    def show_interactive_menu(self):
        """Show interactive command menu"""
        print(f"\n{self._colorize('📋 INTERACTIVE COMMAND MENU', Fore.YELLOW)}")
        print(f"{self._colorize('=' * 60, Fore.BLUE)}")
        
        for category_id, category_info in self.CATEGORIES.items():
            category_commands = []
            
            # Find commands in this category
            for cmd, cmd_info in self.COMMANDS.items():
                if cmd_info.get("category") == category_id:
                    category_commands.append((cmd, cmd_info))
            
            if category_commands:
                print(f"\n{self._colorize(category_info['icon'] + ' ' + category_info['name'], category_info.get('color', Fore.WHITE))}")
                print(f"{self._colorize('-' * 40, Fore.BLUE)}")
                
                for cmd, cmd_info in sorted(category_commands, key=lambda x: x[0]):
                    display_cmd = cmd
                    if cmd.isdigit():
                        display_cmd = f"{cmd} (or /{cmd})"
                    print(f"  {cmd_info['icon']} {self._colorize(display_cmd.ljust(25), Fore.GREEN)} - {cmd_info['description']}")
        
        print(f"\n{self._colorize('💡 Menu Navigation:', Fore.CYAN)}")
        print(f"  • Type any command to execute it")
        print(f"  • Use {self._colorize('Tab', Fore.YELLOW)} for autocomplete")
        print(f"  • Press {self._colorize('Ctrl+C', Fore.YELLOW)} to exit menu")
        print()
    
    def get_command_stats(self) -> Dict[str, int]:
        """Get statistics about command usage"""
        return dict(self.command_stats)
    
    def interactive_input(self, prompt: str = "🔥 IBLU> ") -> str:
        """Get interactive input with enhanced command helper"""
        try:
            # Use readline for input with history and completion
            command = input(f"{self._colorize(prompt, Fore.YELLOW)}").strip()
            
            if command:
                self.add_to_history(command)
                
                # Show typing assistant suggestions for next input
                if len(command) > 1:
                    self.show_typing_assistant(command)
            
            return command
        except KeyboardInterrupt:
            print(f"\n{self._colorize('👋 Goodbye!', Fore.CYAN)}")
            return ""
        except EOFError:
            print(f"\n{self._colorize('👋 Goodbye!', Fore.CYAN)}")
            return ""

# Test function
def test_enhanced_command_helper():
    """Test the enhanced command helper"""
    helper = EnhancedCommandHelper()
    
    print("🔥 Testing Enhanced IBLU Command Helper v2.2")
    print("=" * 60)
    
    # Test typing suggestions
    suggestions = helper.get_typing_suggestions("sc")
    print(f"Typing suggestions for 'sc': {suggestions}")
    
    # Test numbered command suggestions
    suggestions = helper.get_typing_suggestions("1")
    print(f"Typing suggestions for '1': {suggestions}")
    
    # Test help
    helper.show_command_help("scan")
    
    # Test stats
    helper.show_stats()
    
    # Test interactive menu
    helper.show_interactive_menu()

if __name__ == "__main__":
    test_enhanced_command_helper()
