import logging
import requests
from bs4 import BeautifulSoup

class HtmlHandler:
    """Class to handle html files"""
    def __init__(self, url: str, path_to_file: str):
        self._url = url
        self._path_to_file = path_to_file
        
    def set_url(self, new_url: str):
        """Sets the url to a diffent url"""
        self._url = new_url

    def set_path_to_file(self, new_path_to_file: str):
        """Sets the path to file to a new or other file"""
        self._path_to_file = new_path_to_file

    def get_html_file(self, prettify: bool = True) -> str | None:
        """Get the html file from the url
        Returns:
            str | None: The html file if it was gotten successfully, None otherwise
        """
        try:
            r = requests.get(self._url)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            return soup.prettify() if prettify else soup
        except Exception as e:
            logging.error(f"Coudn't get the html file: {e}")
            return None

    def put_in_file(self, html_text: str) -> bool:
        """Put the html text in a file
        Returns:
            bool: True if the html text was put in the file successfully, False otherwise
        """
        try:
            with open(self._path_to_file, "w", encoding="utf-8") as f:
                f.write(html_text)
        except Exception as e:
            logging.error(f"Couldn't put the html text in the file: {e}")
            return False
        return True
    
    def get_and_put(self) -> bool:
        """Get the html file from the url and put it in the file"""
        html_text = self.get_html_file()
        if html_text is None:
            return False
        return self.put_in_file(str(html_text))
    
    def wipe_file(self) -> bool:
        """Wipes the file
        Returns:
            bool: True if the file was wiped successfully, False otherwise
        """
        try:
            with open(self._path_to_file, "w", encoding="utf-8") as f:
                f.write("")
        except Exception as e:
            logging.error(f"Couldn't wipe the file: {e}")
            return False
        return True
    
    def get_mt_sentence(self) -> str | None:
        """Get a javascript variable from the html file"""
        try:
            # makes sure the file is up to date
            html_text = self.get_html_file()
            self.put_in_file(html_text)

            pass
        except Exception as e:
            logging.error(f"Couldn't get the sentence: {e}")
            return None
    