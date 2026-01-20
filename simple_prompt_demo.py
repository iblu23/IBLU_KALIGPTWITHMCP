#!/usr/bin/env python3
"""
💬 Simple prompt_toolkit Demo 💬
"""

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter

commands = WordCompleter(
    ['hello', 'help', 'exit', 'how are you'],
    ignore_case=True
)

text = prompt(
    'You: ',
    completer=commands,
    history=FileHistory('chat_history.txt'),
    complete_while_typing=True
)

print("You typed:", text)
