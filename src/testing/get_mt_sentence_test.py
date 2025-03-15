import os
import sys
import logging

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

BRAVE_EXE_PATH = "C:/Users/idoba/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe"
MONKEYTYPE_URL = "https://monkeytype.com/"
CHROME_DRIVER_PATH = "C:/Users/idoba/.wdm/drivers/chromedriver/win64/134.0.6998.45/chromedriver.exe"

class GetMTSentence:
    def __init__(self, browser_exe_path: str):
        self.browser_exe_path = browser_exe_path
        self.driver = self._get_brave_driver()
        self.wait = None

    def _get_brave_driver(self) -> WebDriver | None:
        """Returns the brave driver"""
        try:
            options = Options()
            options.binary_location = self.browser_exe_path
            service = Service(CHROME_DRIVER_PATH)
            return Chrome(service=service, options=options)
        except Exception as e:
            logging.error(f"Failed to get brave driver: {e}")
            return None
    
    def open_monkeytype(self, wait_for: float = 10) -> WebDriver | None:
        """Opens monkeytype and waits for the sentence to load"""
        try:
            self.driver.get(MONKEYTYPE_URL)
            self.wait = WebDriverWait(self.driver, wait_for)
            return self.driver
        except Exception as e:
            logging.error(f"Failed to open monkeytype: {e}")
            return None


    def get_sentence(self) -> str | None:
        try:
            if self.wait:
                # wait until one word is loaded
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "word")))

                # waits until the sentence is loaded
                element = self.wait.until(EC.presence_of_element_located((By.ID, "words")))

                # format the sentence
                sentence = " ".join([
                    "".join(letter.text for letter in word.find_elements(By.TAG_NAME, "letter"))
                    for word in element.find_elements(By.CLASS_NAME, "word")
                ])
                return sentence
            else:
                logging.error("Wait object is not initialized, make sure to open the monkeytype first.")
                return None
        
        except Exception as e:
            logging.error(f"Failed to get sentence: {e}")
            return None
    
def clear_terminal():
    """Clear the terminal"""
    # if in windows it uses the `cls` and if other then `clear`
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO) # TODO: remove later
    mt = GetMTSentence(BRAVE_EXE_PATH)
    mt.open_monkeytype()
    clear_terminal()

    # Input area
    running = True
    while running:
        user_input = str(input("Write `exit` to end the program: ")).lower()
        match user_input:
            case "exit":
                running = False
        clear_terminal()
    sys.exit(0)