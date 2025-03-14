# This is a test to get data from html file and put it in a file

import logging
import requests

class HtmlHandler:
    """Class to handle html files"""
    def __init__(self, url: str, path_to_file: str):
        self.url = url
        self.path_to_file = path_to_file

    def get_html_file(self) -> str:
        """Get the html file from the url"""
        r = requests.get(self.url)
        return r.text

    def put_in_file(self, html_text: str):
        """Put the html text in a file"""
        with open(self.path_to_file, "w", encoding="utf-8") as f:
            f.write(html_text)

    # TODO: add try and except to handle errors in the methods
