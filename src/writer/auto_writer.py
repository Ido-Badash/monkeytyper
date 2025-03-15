import time
import logging
import pyperclip as pyclip
from pynput.keyboard import Controller

class AutoWriter:
    """class for auto writing text"""
    def __init__(self, sentence: str = "", sleep_delay: float = 0.025,
                 copy_sentence: bool = False, start_write_after: float = 3):
        self.sentence = sentence
        self.sleep_delay = sleep_delay
        self.copy_sentence = copy_sentence
        self.start_write_after = start_write_after
        if self.copy_sentence:
            pyclip.copy(self.sentence)
        self.keyb = Controller()

    def set_sentence(self, new_sentence: str):
        """Sets the sentence to a new sentence"""
        self.sentence = new_sentence
        if self.copy_sentence:
            pyclip.copy(self.sentence)

    def write(self) -> bool:
        """
        Types out the sentence character by character with a delay.
        
        Returns:
            bool: True if the entire sentence was typed out, False if stopped before completion or error.
        """
        time.sleep(self.start_write_after)
        try:
            for char in self.split_sentence(self.sentence):
                self.keyb.type(char)
                time.sleep(self.sleep_delay)
            return True
        except Exception as e:
            logging.error(f"Keyboard typing error: {e}")
            return False

    def clear(self):
        """Clears the sentence."""
        self.sentence = ""

    def split_sentence(self, sentence: str):
        """Splits the sentence into characters"""
        return [char for char in sentence]