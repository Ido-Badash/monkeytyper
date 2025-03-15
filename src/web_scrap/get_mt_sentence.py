import logging

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

MONKEYTYPE_URL = "https://monkeytype.com/"

class MTSentenceGetter:
    """class for getting monkeytype sentence"""
    def __init__(self, chromium_browser_path: str, chrome_driver_path: str):
        """Only use chromium based browsers"""
        self._chromium_browser_path = chromium_browser_path
        self._chrome_driver_path = chrome_driver_path
        self.driver: WebDriver = None
        self.wait: WebDriverWait = None

    def _get_brave_driver(self) -> WebDriver | None:
        """Returns the brave driver"""
        try:
            options = Options()
            options.binary_location = self._chromium_browser_path
            service = Service(self._chrome_driver_path)
            return Chrome(service=service, options=options)
        except Exception as e:
            logging.error(f"Failed to get brave driver: {e}")
            return None
    
    def open_monkeytype(self, wait_for: float = 10) -> WebDriver | None:
        """Opens monkeytype and waits for the sentence to load"""
        try:
            self.driver = self._get_brave_driver()
            self.driver.get(MONKEYTYPE_URL)
            self.wait = WebDriverWait(self.driver, wait_for)
            return self.driver
        except Exception as e:
            logging.error(f"Failed to open monkeytype: {e}")
            return None


    def get_sentence(self) -> str | None:
        """Gets the monkytype sentence
        Returns:
            str: if the fetch went good None otherwise
        """
        try:
            if self.wait and self.driver:
                # wait until one word is loaded
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "word")))

                # waits until the sentence is loaded
                element = self.wait.until(EC.presence_of_element_located((By.ID, "words")))

                # format the sentence
                sentence = " ".join([
                    "".join(letter.text for letter in word.find_elements(By.TAG_NAME, "letter"))
                    for word in element.find_elements(By.CLASS_NAME, "word")
                ])
                logging.debug(f"Monkeytype sentence: {sentence}")
                return sentence
            else:
                logging.error("Wait or driver object is not initialized, make sure to open the monkeytype first.\n\
                              Use the `open_monkeytype` function.")
                return None
        
        except Exception as e:
            logging.error(f"Failed to get sentence: {e}")
            return None
        
