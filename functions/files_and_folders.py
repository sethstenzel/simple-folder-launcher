from tkinter import filedialog

# Function to open a folder dialog and set the folder path in the folder_path_entry
def choose_folder():
    folder_path = filedialog.askdirectory()
    return folder_path.replace("/", "\\")


# Function to open a file dialog and set the file path in the file_path_entry
def choose_file():
    file_path = filedialog.askopenfilename()
    return file_path.replace("/", "\\")


