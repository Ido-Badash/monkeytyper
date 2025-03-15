import sys
import logging
import webbrowser

def launch_website(url: str, browser_name: str = "default"):
    """Opens a website in a browser, if no browser is specified, it will use the default browser."""
    try:
        if browser_name == "default":
            webbrowser.open(url)
        else:
            browser = webbrowser.get(browser_name)
            browser.open(url)
    except webbrowser.Error as e:
        logging.error(f"Cant open {url} in {browser_name} browser. Error: {e}")
        logging.info("Make sure the browser is installed and the name is correct.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)