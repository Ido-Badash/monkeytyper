import sys
import logging
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

def exit_program(root: ctk.CTk = None, sys_exit: bool = True, exit_code: int = 0, input_holder: bool = False):
    """Exits the program"""
    try:
        if input_holder:
            if root:
                root.destroy()
            input("Press enter to exit...")
        else:
            if root:
                root.destroy()
        if sys_exit:
            sys.exit(exit_code)
    except Exception as e:
        logging.error(f"There was an error while trying to exit: {e}")