import logging
import time

import pyperclip as pyclip
from pynput.keyboard import Controller

class AutoWriter:
    def __init__(self, sentence: str, sleep_duration: float = 0.05, copy_sentence: bool = False):
        self.sentence = sentence
        self.sleep_duration = sleep_duration
        self.copy_sentence = copy_sentence
        if self.copy_sentence:
            pyclip.copy(self.sentence)
        self.user_keyb = Controller()

    def run(self):
        """Runs the writer"""
        logging.info(f"Writing sentence: {self.sentence}")
        try:
            for char in self.sentence:
                self.user_keyb.type(char)
                time.sleep(self.sleep_duration)
        except KeyboardInterrupt as keyb_interrupt:
            logging.info(f"Interrupted the writer: {keyb_interrupt}")
        logging.info("Finished writing the sentence")
