# ________  ___  ___  ___  ________  ________  ________      
#|\   ____\|\  \|\  \|\  \|\   __  \|\   __  \|\   ____\     
#\ \  \___|\ \  \\\  \ \  \ \  \|\  \ \  \|\  \ \  \___|_    
# \ \  \    \ \   __  \ \  \ \   ____\ \  \\\  \ \_____  \   
#  \ \  \____\ \  \ \  \ \  \ \  \___|\ \  \\\  \|____|\  \  
#   \ \_______\ \__\ \__\ \__\ \__\    \ \_______\____\_\  \ 
#    \|_______|\|__|\|__|\|__|\|__|     \|_______|\_________\
#                                                \|_________|
#                                                                
#  Copyright © 2026 Marcos Dominguez. All rights reserved.
#  Licensed under the MIT License. See LICENSE file in the project root for full license information                                                              

logo = r"""
 ________  ___  ___  ___  ________  ________  ________      
|\   ____\|\  \|\  \|\  \|\   __  \|\   __  \|\   ____\     
\ \  \___|\ \  \\\  \ \  \ \  \|\  \ \  \|\  \ \  \___|_    
 \ \  \    \ \   __  \ \  \ \   ____\ \  \\\  \ \_____  \   
  \ \  \____\ \  \ \  \ \  \ \  \___|\ \  \\\  \|____|\  \  
   \ \_______\ \__\ \__\ \__\ \__\    \ \_______\____\_\  \ 
    \|_______|\|__|\|__|\|__|\|__|     \|_______|\_________\
                                                \|_________|
                                                
===============================================================    
                         Version 1.0.0                                                     
"""

print(logo)
import os
import importlib
commands = []
command_dir = os.path.join(os.path.dirname(__file__), "command")
# get command filenames
for f in os.listdir(command_dir):
    if f.endswith(".py") and f != "__init__.py":
        commands.append(f.replace(".py", ""))


co = {}
for cmd_name in commands:
    module = importlib.import_module(f"command.{cmd_name}")
    try:
        co[cmd_name] = module.run
    except AttributeError:
        print(f"Command {cmd_name} does not have a run function. ignored.")

def command_line_interface():
    command = input("ChipOS> ")
    args = command.split()
    if not args:
        return
    command_args = args[1:]  # get all arguments after the command name
    if args[0] in co:
        co[args[0]](*command_args)  # call the function with arguments
    else:
        print(f"Unknown command: {args[0]}")

while True:
    command_line_interface()
