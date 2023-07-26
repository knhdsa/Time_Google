from tkinter import *
import psutil

def start(program_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == program_name:
            return True
    return False