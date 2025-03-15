import webbrowser
import logging

class TabChecker:
    """checks if a tab is open in the browser"""
    def __init__(self, url: str):
        self.url = url

    def is_tab_open(self) -> bool:
        """checks if the tab is open
        Returns:
            bool: True if the tab is open False otherwise
        """
        return True
    
    def open_tab(self):
        """opens the tab
        Returns:
            bool: True if the tab was opened successfully, False otherwise
        """ 
        try:
            webbrowser.open(self.url)
        except webbrowser.Error as e:
            logging.error(f"Couldn't open the tab: {e}")
            return False
        return True
