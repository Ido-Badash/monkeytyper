import sys
import logging
import traceback
import customtkinter as ctk
from writer import AutoWriter
from web_scrap import MTSentenceGetter
from utils import *

# ----------------------- Test play ground -----------------------
"""

"""
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

def update_sentence(writer: AutoWriter, sentence_getter: MTSentenceGetter) -> str | None:
    """Returns the sentence and updates the writer"""
    sentence = sentence_getter.get_sentence()
    writer.set_sentence(sentence)
    return sentence

@catch_it
def main():
    # logging config
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        datefmt="%H:%M:%S")
    
    logging.info("Program started")

    # --- sentence getter ---
    # gets the sentence from the html file and puts it in a file in the data folder
    CHROME_DRIVER_PATH = "C:/Users/idoba/.wdm/drivers/chromedriver/win64/134.0.6998.45/chromedriver.exe"
    BRAVE_EXE_PATH = "C:/Users/idoba/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe"
    mt_sentence_getter = MTSentenceGetter(BRAVE_EXE_PATH, CHROME_DRIVER_PATH)

    # --- writer ---
    writer = AutoWriter(copy_sentence=True)

    # --- customtkinter ---
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    root = ctk.CTk()
    root.title("Monkytype Auto Writer")
    user_w, user_h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{user_w//2}x{user_h//2}")

    button_font = ctk.CTkFont(family="Helvetica", size=16)

    # space at the top
    top_space = ctk.CTkLabel(root, text="")
    top_space.pack(pady=10)

    # --- buttons ---
    buttons_specs = {"font": button_font, "width": 100, "height": 50}
    buttons_pack_specs = {"padx": 5, "pady": 8, "expand": True, "fill": "both"}

    # buttons frame
    buttons_frame = ctk.CTkFrame(root)
    buttons_frame.pack(padx=100, pady=5, expand=True, fill='both')

    left_button_frame = ctk.CTkFrame(buttons_frame)
    left_button_frame.pack(side="left", padx=10, pady=5, expand=True, fill='both')

    right_button_frame = ctk.CTkFrame(buttons_frame)
    right_button_frame.pack(side="right", padx=10, pady=5, expand=True, fill='both')

    # launch monkeytype button
    launch_mt_func = lambda: mt_sentence_getter.open_monkeytype()
    launch_mt_b = ctk.CTkButton(left_button_frame, text="Launch Monkeytype", **buttons_specs, command=launch_mt_func,
                                text_color="#e2b314", fg_color="#21130d", hover_color="#29160e")
    launch_mt_b.pack(**buttons_pack_specs)

    # fetch sentence button
    update_sentence_func = lambda: update_sentence(writer, mt_sentence_getter)
    update_sentence_b = ctk.CTkButton(left_button_frame, text="Fetch Sentence", **buttons_specs,
                                     fg_color="#27319c", command=update_sentence_func)
    update_sentence_b.pack(**buttons_pack_specs)

    # clear sentence button
    clear_sentence = lambda: writer.clear()
    clear_sentence_b = ctk.CTkButton(left_button_frame, text="Clear Sentence", **buttons_specs, command=clear_sentence,
                                        fg_color="#27319c")
    clear_sentence_b.pack(**buttons_pack_specs)

    # start writing button
    start_write = lambda: write_and_disable(writer, 3, start_writing_b, update_sentence_b)
    start_writing_b = ctk.CTkButton(right_button_frame, text="Start Writing", **buttons_specs, command=start_write,
                                     fg_color="#27319c")
    start_writing_b.pack(**buttons_pack_specs)

    # stop writing button
    stop_writing_b = ctk.CTkButton(right_button_frame, text="Stop Writing", **buttons_specs, command=writer.toggle,
                                   fg_color="#27319c")
    stop_writing_b.pack(**buttons_pack_specs)

    # exit button
    exit_func = lambda: exit_program(root)
    exit_b = ctk.CTkButton(
        right_button_frame, text="Exit", **buttons_specs,
        command=exit_func, fg_color="#27119c")
    exit_b.pack(**buttons_pack_specs)

    # --- Text ---
    text_frame = ctk.CTkFrame(root)
    text_frame.pack(padx=100, pady=5, expand=True, fill='both')

    # Left frame for instructions
    instructions_frame = ctk.CTkFrame(text_frame)
    instructions_frame.pack(side="left", padx=10, pady=5, expand=True, fill='both')

    instructions_msg = """Instructions:\n\n
        1. Click the 'Launch Monkeytype' button.\n
        2. Click 'Fetch Sentence' to get the sentence.\n
        3. Click 'Start Writing' to start writing the sentence.\n
        4. After you clicked 'Start Writing', quickly switch to the Monkeytype tab.\n
        5. The program will start writing the sentence.\n
        6. While writing, DO NOT click on the keyboard.\n
        7. If you want to stop the program, click 'Stop Writing'.\n"""

    instructions_label = ctk.CTkLabel(instructions_frame, text=instructions_msg, font=ctk.CTkFont(family="Helvetica", size=16))
    instructions_label.pack(padx=5, pady=10, expand=True)

    # Right frame for tips
    tips_frame = ctk.CTkFrame(text_frame)
    tips_frame.pack(side="right", padx=10, pady=5, expand=True, fill='both')

    tips_msg = """Tips:\n\n
        1. Make sure you can click on `Stop Writing` (split the screen).\n
        2. If you want to write another sentence, click 'Fetch Sentence' again.\n
        3. If you want to write the same sentence again, click 'Start Writing' again.\n
        4. If you want to stop the program, click 'Stop Writing'.\n
        5. If you want to exit the program, click 'Exit'.\n
        6. Do not spam the buttons, it may cause the program to crash.\n
        7. Make sure you have a good internet connection.\n"""

    tips_label = ctk.CTkLabel(tips_frame, text=tips_msg, font=ctk.CTkFont(family="Helvetica", size=16))
    tips_label.pack(padx=5, pady=10, expand=True)

    # space at the bottom
    bottom_space = ctk.CTkLabel(root, text="")
    bottom_space.pack(pady=10)

    root.mainloop()
    logging.info("Program ended")
    sys.exit(0) # exit with success

if __name__ == "__main__":
    main()