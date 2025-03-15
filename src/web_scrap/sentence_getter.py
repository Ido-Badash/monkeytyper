import logging
from pathlib import Path
from .tab_checker import TabChecker

class SentenceGetter:
    def __init__(self, url: str):
        self.url = url
        self.mt_tab_checker = TabChecker(self.url)
        self.sentence = None

    def get_sentence(self):
        """gets a sentence from the url
        Returns:
            str: sentence
        """
        if self.mt_tab_checker.is_tab_open():
            logging.debug(f"Trying to get sentence from {self.url}")
            try:
                # get the sentence here
                self.sentence = "This is a sentence"
                return self.sentence
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                return None
        else:
            self.mt_tab_checker.open_tab()
            return self.get_sentence()
    
    def put_into_file(self, file_path: str) -> bool:
        """puts the sentence into a file
        Returns:
            bool: True if the sentence is written to the file False otherwise
        """
        if self.sentence:
            with open(Path(file_path), "w", encoding="utf-8") as f:
                f.write(self.sentence)
            return True
        else:
            logging.error("No sentence to write, first get the sentence maybe?")
            return False