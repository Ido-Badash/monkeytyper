# This is a test to get data from html file and put it in a file

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

    def get_html_file(self) -> str | None:
        """Get the html file from the url"""
        try:
            website_r = requests.get(self._url)
            website_r.raise_for_status()
            return website_r.text
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
    
    def find_in_file(self):
        """Finds data from the html file"""
        pass
