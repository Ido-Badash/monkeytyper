import sys
import time
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

@catch_it
def main():
    # logging config
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s - %(message)s",
        datefmt="%H:%M:%S")
    
    logging.info("Program started")

    # --- colors ---
    DEEP_BLUE = "#27319c" # used for writer button
    PALE_BLUE = "#27119c" # used for exit buttons
    YELLOW = "#e2b314" # used for launch monkeytype button text
    DARK_BROWN= "#21130d" # used for launch monkeytype button background
    DARKER_BROWN= "#29160e" # used for launch monkeytype button hover
    NORMAL_TEXT_COLOR = "#ffffff"

    # --- sentence getter ---
    # gets the sentence from the html file and puts it in a file in the data folder
    CHROME_DRIVER_PATH = "C:/Users/idoba/.wdm/drivers/chromedriver/win64/134.0.6998.45/chromedriver.exe"
    BRAVE_EXE_PATH = "C:/Users/idoba/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe"
    mt_sentence_getter = MTSentenceGetter(BRAVE_EXE_PATH, CHROME_DRIVER_PATH)

    # --- writer ---o
    SPEED_FACTOR = 1.5
    writer = AutoWriter(copy_sentence=True, base_delay=0.012)

    # --- customtkinter ---
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
    
    root = ctk.CTk()
    root.title("Monkytype Auto Writer")
    user_w, user_h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{int(user_w/2.5)}x{int(user_h/2.5)}")

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

    # fetch sentence button
    update_sentence_func = lambda: update_sentence(writer, mt_sentence_getter)
    update_sentence_b = ctk.CTkButton(right_button_frame, text="Fetch Sentence", **buttons_specs,
                                     fg_color=PALE_BLUE, text_color=NORMAL_TEXT_COLOR, command=update_sentence_func)
    update_sentence_b.pack(**buttons_pack_specs)

    # start writing button
    start_write = lambda: write_and_disable(writer, 3, start_writing_b, update_sentence_b)
    start_writing_b = ctk.CTkButton(right_button_frame, text="Start Writing", **buttons_specs, command=start_write,
                                     fg_color=PALE_BLUE, text_color=NORMAL_TEXT_COLOR)
    start_writing_b.pack(**buttons_pack_specs)

    # increase speed button
    increase_speed_func = lambda: writer.set_sleep_delay(writer.get_sleep_delay() / SPEED_FACTOR)
    increase_speed_b = ctk.CTkButton(right_button_frame, text="Increase Speed", **buttons_specs,
                                        fg_color=PALE_BLUE, text_color=NORMAL_TEXT_COLOR, command=increase_speed_func)
    increase_speed_b.pack(**buttons_pack_specs)

    # decrease speed button
    decrease_speed_func = lambda: writer.set_sleep_delay(writer.get_sleep_delay() * SPEED_FACTOR)
    decrease_speed_b = ctk.CTkButton(right_button_frame, text="Decrease Speed", **buttons_specs,
                                        fg_color=PALE_BLUE, text_color=NORMAL_TEXT_COLOR, command=decrease_speed_func)
    decrease_speed_b.pack(**buttons_pack_specs)

    # launch monkeytype button
    launch_mt_func = lambda: mt_sentence_getter.open_monkeytype()
    launch_mt_b = ctk.CTkButton(left_button_frame, text="Launch Monkeytype",
                                font=button_font, width=100, height=90,
                                command=launch_mt_func, text_color=YELLOW,
                                fg_color=DARK_BROWN, hover_color=DARKER_BROWN)
    launch_mt_b.pack(**buttons_pack_specs)

    # exit monkeytype button
    exit_mt_func = lambda: mt_sentence_getter.close()
    exit_mt_b = ctk.CTkButton(
            left_button_frame, text="Exit Monkeytype", font=button_font, width=100, height=5,
            command=exit_mt_func, fg_color=DEEP_BLUE, text_color=NORMAL_TEXT_COLOR)
    exit_mt_b.pack(**buttons_pack_specs)

    # exit all button
    exit_all_b = ctk.CTkButton(
        left_button_frame, text="Exit all", font=button_font, width=100, height=5,
        command=root.destroy, fg_color=DEEP_BLUE, text_color=NORMAL_TEXT_COLOR)
    exit_all_b.pack(**buttons_pack_specs)

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
        5. Avoid pressing buttons while loading (has a hover color).\n"""

    instructions_label = ctk.CTkLabel(instructions_frame, text=instructions_msg, font=ctk.CTkFont(family="Helvetica", size=16))
    instructions_label.pack(padx=5, pady=10, expand=True)

    # Right frame for tips
    tips_frame = ctk.CTkFrame(text_frame)
    tips_frame.pack(side="right", padx=10, pady=5, expand=True, fill='both')

    tips_msg = """Tips:\n\n
        1. If you want to write another sentence, click 'Fetch Sentence' again.\n
        2. If you want to write the same sentence again, click 'Start Writing' again.\n
        3. If you want to exit the program, click 'Exit all'.\n
        4. Do not spam the buttons, it may cause the program to crash.\n
        5. Make sure you have a good internet connection.\n"""

    tips_label = ctk.CTkLabel(tips_frame, text=tips_msg, font=ctk.CTkFont(family="Helvetica", size=16))
    tips_label.pack(padx=5, pady=10, expand=True)

    # space at the bottom
    bottom_space = ctk.CTkLabel(root, text="")
    bottom_space.pack(pady=10)

    root.mainloop()
    time.sleep(1)
    logging.info("Program ended")
    exit_program()
