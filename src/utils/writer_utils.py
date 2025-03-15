import time
import customtkinter as ctk
from writer import AutoWriter
from .ctk_utils import disable_buttons


def timed_write(writer: AutoWriter, sleep_time: float = 3):
    time.sleep(sleep_time)
    return writer.write()

def write_and_disable(writer: AutoWriter, sleep_time: float = 3, *buttons: ctk.CTkButton):
    disable_buttons(*buttons)
    if timed_write(writer, sleep_time):
        for button in buttons:
            button.configure(state="normal")