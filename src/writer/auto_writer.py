import time
import logging
import threading
from typing import Iterable, List
import pyperclip as pyclip
from pynput.keyboard import Controller

class AutoWriter:
    """class for auto writing text"""
    def __init__(self, sentence: str = "", base_delay: float = 0.01,
                 copy_sentence: bool = False, start_write_after: float = 3):
        self.sentence = sentence
        self.base_delay = base_delay
        self.copy_sentence = copy_sentence
        self.start_write_after = start_write_after
        self._sentence_track = ""
        self._max_chars = 0
        self._max_words = 0
        self.keyb = Controller()
        if self.copy_sentence:
            pyclip.copy(self.sentence)


    def set_sentence(self, new_sentence: str):
        """Sets the sentence to a new sentence"""
        self.sentence = new_sentence
        if self.copy_sentence:
            pyclip.copy(self.sentence)

    def set_base_delay(self, new_base_delay: float):
        """Sets the sleep delay to a new sleep delay"""
        self.base_delay = new_base_delay
        logging.debug(f"Sleep delay set to: {self.base_delay}")

    def set_max_words(self, max_words: int):
        """Sets a max for the writer to type"""
        self._max_words = max_words

    def set_max_chars(self, max_chars: int):
        """Sets a max for the writer to type"""
        self._max_chars = max_chars

    def write(self) -> bool:
        """
        Types out the sentence character by character with a delay.
        
        Returns:
            bool: True if the entire sentence was typed out, False if stopped before completion or error.
        """
        time.sleep(self.start_write_after)
        try:
            self._sentence_track = "" # resets the _sentence_track
            for char in self.split_sentence(self.sentence):
                self._sentence_track += char
                if self._max_chars > 0 and self._max_chars_reached():
                    break
                if self._max_words > 0 and self._max_words_reached():
                    break

                self.keyb.type(char) # types the chars into the keyboard
                self.sleep_delay = self.base_delay
                time.sleep(self.sleep_delay) # time delay between each press
            return True
        except Exception as e:
            logging.error(f"An error in the writer: {e}")
            logging.error("Traceback:", exc_info=True)
            return False
        
    def split_sentence(self, sentence: str) -> List[str]:
        """Splits the sentence into characters"""
        return [char for char in sentence]

    def clear(self):
        """Clears the sentence."""
        self.sentence = ""

    @staticmethod
    def _check_max_reached(max: int, iterable: Iterable, max_reach_msg: str = None,
                            logging_level: str = "debug", min_of_max: int = 0):
        """Checks for a max of something
        Returns:
            bool: True if max is reached, False if not
        """
        if max > min_of_max and len(iterable) > max:
            if max_reach_msg:
                eval(f"logging.{logging_level}('{max_reach_msg}')")
            return True
        return False
    
    def _max_words_reached(self) -> bool:
        """Checks if the max words is reached"""
        return self._check_max_reached(self._max_words, self._sentence_track.split(), "Max words reached")
    
    def _max_chars_reached(self) -> bool:
        """Checks if the max characters is reached"""
        return self._check_max_reached(self._max_chars, self._sentence_track, "Max characters reached")
