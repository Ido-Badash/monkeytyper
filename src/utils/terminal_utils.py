import os

def clear_terminal():
    """Clear the terminal"""
    # if in windows it uses the `cls` and if other then `clear`
    os.system('cls' if os.name == 'nt' else 'clear')