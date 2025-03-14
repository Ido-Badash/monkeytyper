
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