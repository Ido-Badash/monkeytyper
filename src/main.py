import sys
import logging
import traceback
import customtkinter as ctk
from writer import AutoWriter
from monkeytype import MTsentenceGetter
from launcher import launch_mt
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
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        datefmt="%H:%M:%S")
    
    logging.info("Program started")

    # --- data ---
    data_folder = SafePath("data")
    sentence_file = data_folder.path("sentence.txt", as_string=True)

    # --- sentence getter ---
    mt_sentence_getter = MTsentenceGetter()
    sentence = mt_sentence_getter.get_sentence()
    mt_sentence_getter.put_into_file(sentence_file)

    # --- writer ---
    writer = AutoWriter(sentence, copy_sentence=True)

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
    button_frame = ctk.CTkFrame(root)
    button_frame.pack(padx=100, pady=5, expand=True, fill='both')

    # launch monkeytype button
    launch_mt_func = lambda: launch_mt()
    launch_mt_b = ctk.CTkButton(button_frame, text="Launch Monkeytype", **buttons_specs, command=launch_mt_func,
                                text_color="#e2b314", fg_color="#21130d")
    launch_mt_b.pack(**buttons_pack_specs)

    # fetch sentence button
    fetch_sentence_b = ctk.CTkButton(button_frame, text="Fetch Sentence", **buttons_specs,
                                     fg_color="#27319c")
    fetch_sentence_b.pack(**buttons_pack_specs)

    # start writing button
    start_write = lambda: write_and_disable(writer, 3, start_writing_b, fetch_sentence_b)
    start_writing_b = ctk.CTkButton(button_frame, text="Start Writing", **buttons_specs, command=start_write,
                                     fg_color="#27319c")
    start_writing_b.pack(**buttons_pack_specs)

    # stop writing button
    stop_writing_b = ctk.CTkButton(button_frame, text="Stop Writing", **buttons_specs, command=writer.stop,
                                   fg_color="#27319c")
    stop_writing_b.pack(**buttons_pack_specs)

    # exit button
    exit_func = lambda: exit_program(root)
    exit_b = ctk.CTkButton(
        button_frame, text="Exit", **buttons_specs,
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
        6. Make sure you can click on the `Stop Writing` button to stop the program.\n"""

    instructions_label = ctk.CTkLabel(instructions_frame, text=instructions_msg, font=ctk.CTkFont(family="Helvetica", size=16))
    instructions_label.pack(padx=5, pady=10, expand=True)

    # Right frame for tips
    tips_frame = ctk.CTkFrame(text_frame)
    tips_frame.pack(side="right", padx=10, pady=5, expand=True, fill='both')

    tips_msg = """Tips:\n\n
        7. If you want to write another sentence, click 'Fetch Sentence' again.\n
        8. If you want to write the same sentence again, click 'Start Writing' again.\n
        9. If you want to stop the program, click 'Stop Writing'.\n
        10. If you want to exit the program, click 'Exit'.\n
        11. Do not spam the buttons, it may cause the program to crash.\n
        12. Make sure you have a good internet connection.\n"""

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