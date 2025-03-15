import sys
from typing import Literal
import customtkinter as ctk

def toggle_button_text(button: ctk.CTkButton, text1: str, text2: str):
    if button.cget("text") == text1:
        button.configure(text=text2)
    else:
        button.configure(text=text1)

def disable_buttons(*buttons: ctk.CTkButton) -> Literal[True]:
    """Disables ctk buttons
    Returns:
        True: if finished"""
    for button in buttons:
        button.configure(state="disabled")
    return True

def exit_program(root):
    root.quit()
    root.destroy()
    sys.exit(0)