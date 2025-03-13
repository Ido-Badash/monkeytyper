import sys
import logging
import traceback
from writer import AutoWriter

# ----------------------- Test play ground -----------------------
# 
# 
#
# ----------------------------------------------------------------

def catch_it(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            logging.error(traceback.format_exc())
            sys.exit(1)
    return wrapper

@catch_it
def main():
    # logging config
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S")
    
    logging.info("Program started")

    writer = AutoWriter("BDOSUUU ahh $%^& we out baby")
    writer.run()

    logging.info("Program ended")
    sys.exit(0) # exit with success

if __name__ == "__main__":
    main()