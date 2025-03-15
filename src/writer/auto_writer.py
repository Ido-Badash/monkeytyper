import logging
import threading
import time

import pyperclip as pyclip
from pynput.keyboard import Controller

class AutoWriter:
    def __init__(self, sentence: str = "", sleep_duration: float = 0.025, copy_sentence: bool = False):
        self.sentence = sentence
        self.sleep_duration = sleep_duration
        self.copy_sentence = copy_sentence
        if self.copy_sentence:
            pyclip.copy(self.sentence)
        self.user_keyb = Controller()
        self._current_index = 0
        self._stop_event = threading.Event()

    def set_sentence(self, new_sentence: str):
        """Sets the sentence to a new sentence"""
        self.sentence = new_sentence
        if self.copy_sentence:
            pyclip.copy(self.sentence)

    def write(self) -> bool:
        """
        Types out the sentence character by character with a delay.
        
        Returns:
            bool: True if the entire sentence was typed out, False if stopped before completion.
        """
        self._stop_event.clear()
        while self._current_index < len(self.sentence) and not self._stop_event.is_set():
            self.user_keyb.type(self.sentence[self._current_index])
            self._current_index += 1
            time.sleep(self.sleep_duration)
        
        finished = self._current_index == len(self.sentence)
        self._current_index = 0
        return finished

    def stop(self):
        """Stops the typing process."""
        self._stop_event.set()
        self._current_index = 0

    def clear(self):
        """Clears the sentence."""
        self.sentence = ""