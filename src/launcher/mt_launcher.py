from .web_launcher import launch_website

def launch_mt(browser_name: str = "default"):
    """Launches the Monkytype website."""
    launch_website("https://monkeytype.com", browser_name)
