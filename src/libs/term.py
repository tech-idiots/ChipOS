import subprocess
import os
def clear_terminal():
    """Clears the terminal screen."""
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)