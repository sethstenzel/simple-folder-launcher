import tkinter as tk
from tkinter import ttk
from functions.files_and_folders import choose_folder, choose_file
from classes.ui.popups import error_message_popup
from functions.build_executable import build_executable


class AppMainWindow:

    def __init__(
        self,
        title="AppMainWindow",
        width=600,
        height=400,
        icon="icons/default.ico",
        columns=3,
        rows=4,
    ):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.iconbitmap(icon)
        self.columns = columns
        self.rows = rows
        self.icon = icon

        self.widgets = {}

        self.build_details = {
            "launcher_name": None,
            "folder_path": None,
            "icon_path": None,
        }

        # Configure the grid layout manager
        for i in range(self.columns):
            self.root.columnconfigure(i, weight=0)
            self.root.grid_columnconfigure(i, minsize=20)
        for i in range(self.rows):
            self.root.rowconfigure(i, weight=0)
            self.root.grid_rowconfigure(i, minsize=20)

        self.add_widgets()

    def run(self):
        # Starting the Tkinter event loop
        self.root.mainloop()

    def add_widgets(self):

        # Label and Entry for Launcher Name
        self.widgets["launcher_name_label"] = ttk.Label(
            self.root, text="Launcher Name:"
        )
        self.widgets["launcher_name_label"].grid(
            row=0, column=0, padx=20, pady=5, sticky="w"
        )

        self.widgets["launcher_name_entry"] = ttk.Entry(self.root, width=50)
        self.widgets["launcher_name_entry"].grid(
            row=0, column=1, padx=0, pady=5, sticky="w", columnspan=2
        )

        # Label and Entry for Folder Path
        self.widgets["folder_path_label"] = ttk.Label(self.root, text="Launch Path:")
        self.widgets["folder_path_label"].grid(
            row=1, column=0, padx=20, pady=5, sticky="w"
        )
        self.widgets["folder_path_entry"] = ttk.Entry(self.root, width=50)
        self.widgets["folder_path_entry"].grid(
            row=1, column=1, padx=0, pady=5, sticky="w"
        )
        self.widgets["choose_folder_button"] = ttk.Button(
            self.root,
            text="Choose Launch Folder",
            command=self.choose_folder_button_press,
        )
        self.widgets["choose_folder_button"].grid(
            row=1, column=2, padx=10, pady=5, sticky="ew"
        )

        # Label and Entry for File Path
        self.widgets["icon_path_label"] = ttk.Label(self.root, text="Launcher Icon:")
        self.widgets["icon_path_label"].grid(
            row=2, column=0, padx=20, pady=5, sticky="w"
        )
        self.widgets["icon_path_entry"] = ttk.Entry(self.root, width=50)
        self.widgets["icon_path_entry"].grid(
            row=2, column=1, padx=0, pady=5, sticky="w"
        )
        self.widgets["choose_file_button"] = ttk.Button(
            self.root, text="Choose Icon File", command=self.choose_file_button_press
        )
        self.widgets["choose_file_button"].grid(
            row=2, column=2, padx=10, pady=5, sticky="ew"
        )

        # Button to print the info
        self.widgets["print_info_button"] = ttk.Button(
            self.root,
            text="Build Executable",
            command=self.build_executable_button_press,
        )
        self.widgets["print_info_button"].grid(
            row=3, column=1, columnspan=1, padx=0, pady=20, sticky="ew"
        )

    def choose_folder_button_press(self):
        folder_path = choose_folder()
        self.widgets["folder_path_entry"].delete(0, tk.END)
        self.widgets["folder_path_entry"].insert(0, folder_path)

    def choose_file_button_press(self):
        icon_path = choose_file()
        self.widgets["icon_path_entry"].delete(0, tk.END)
        self.widgets["icon_path_entry"].insert(0, icon_path)

    def build_executable_button_press(self):
        self.build_details["launcher_name"] = (
            self.widgets["launcher_name_entry"].get().replace("\\", "\\\\")
        )
        self.build_details["folder_path"] = (
            self.widgets["folder_path_entry"].get().replace("\\", "\\\\")
        )
        self.build_details["icon_path"] = (
            self.widgets["icon_path_entry"].get().replace("\\", "\\\\")
        )

        if (
            self.build_details["launcher_name"] is None
            or self.build_details["launcher_name"] == ""
        ):
            error_message_popup("Launcher Name is required!")
            return

        if (
            self.build_details["folder_path"] is None
            or self.build_details["folder_path"] == ""
        ):
            error_message_popup("Folder Path is required!")
            return

        if (
            self.build_details["icon_path"] is None
            or self.build_details["icon_path"] == ""
        ):
            self.build_details["icon_path"] = self.icon

        successful_build = build_executable(
            launcher_name=self.build_details["launcher_name"],
            launch_path=self.build_details["folder_path"],
            launcher_icon_path=self.build_details["icon_path"],
        )
        if successful_build:
            self.root.destroy()
