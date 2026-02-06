
commands = []
import os
command_dir = os.path.join(os.path.dirname(__file__))
""" get command filenames"""
for f in os.listdir(command_dir):
    if f.endswith(".py") and f != "__init__.py":
        commands.append(f.replace(".py", ""))


def run(*args):
    if args == ():
        print("List of available commands:")
        for cmd in commands:
            print(f" - {cmd}")
    
