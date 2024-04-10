from tkinter import messagebox

def error_message_popup(message):
    messagebox.showerror("Error", message)

def info_message_popup(message):
    messagebox.showinfo("Info", message)