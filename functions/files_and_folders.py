from tkinter import filedialog
import os


# Function to open a folder dialog and set the folder path in the folder_path_entry
def choose_folder():
    folder_path = filedialog.askdirectory(initialdir=f"{os.getcwd()}")
    return folder_path.replace("/", "\\")


# Function to open a file dialog and set the file path in the file_path_entry
def choose_file():
    file_path = filedialog.askopenfilename(initialdir=f"{os.getcwd()}")
    return file_path.replace("/", "\\")
