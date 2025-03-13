import logging
from utils import SafePath

class MTAutoWriter:
    def __init__(self):
        self.data_folder = SafePath("data")
        self.mt_sentence_txt = self.data_folder.path("mt_sentence.txt", as_string=True)

        with open (self.mt_sentence_txt, "a") as f:
            f.write("Hello, World!\n")
            f.write("This is a test sentence.\n")
        with open(self.mt_sentence_txt, "r") as f:
            self.mt_sentence = f.readlines()[-1].strip()
            logging.info(f'Read sentence: "{self.mt_sentence}"')

    def flush_sentence(self):
        """Flushs the sentences file"""
        with open(self.mt_sentence_txt, "w") as f:
            f.write("")
        logging.info("Flushed the sentences file")

    def run(self):
        pass