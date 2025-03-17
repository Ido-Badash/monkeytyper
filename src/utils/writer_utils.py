import customtkinter as ctk
from writer import AutoWriter
from web_scrap import MTSentenceGetter
from .ctk_utils import disable_buttons

def write_and_disable(writer: AutoWriter, sleep_time: float = 3, *buttons: ctk.CTkButton):
    buttons_are_disable = disable_buttons(*buttons)
    writer.start_write_after = sleep_time
    finished_writing = writer.write()
    if buttons_are_disable and finished_writing:
        for button in buttons:
            button.configure(state="normal")

def update_sentence(writer: AutoWriter, sentence_getter: MTSentenceGetter) -> str | None:
    """Returns the sentence and updates the writer"""
    sentence = sentence_getter.get_sentence()
    writer.set_sentence(sentence)
    return sentence