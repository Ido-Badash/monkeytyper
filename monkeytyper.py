# Runs the app for main.py
import os
import sys

parent_path = os.path.dirname(__file__)
src_path = os.path.join(parent_path, "src")
sys.path.append(src_path)

from src import run_mt_app

if __name__ == "__main__":
    run_mt_app()