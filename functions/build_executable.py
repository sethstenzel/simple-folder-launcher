import subprocess
import tempfile
from classes.ui.popups import info_message_popup, error_message_popup
from .files_and_folders import choose_folder
import os


def build_executable(*, launcher_name, launch_path, launcher_icon_path):
    print(
        f"Launcher Name: {launcher_name}\nFolder Path: {launch_path}\nFile Path: {launcher_icon_path}"
    )

    with open("template/launcher_template.py", "r") as template_file:
        executable_script = template_file.read().replace(
            "%%%PATH_STRING%%%", launch_path
        )

    new_tempfile = tempfile.NamedTemporaryFile(delete=False, suffix=".py")

    new_tempfile.write(bytes(executable_script, "utf-8"))
    new_tempfile.close()

    info_message_popup("Please select the output\ndirectory of this launcher.")

    pyinstaller_output_directory = choose_folder()

    if pyinstaller_output_directory is not None:
        if os.path.isfile(pyinstaller_output_directory + "\\" + launcher_name + ".exe"):
            os.remove(pyinstaller_output_directory + "\\" + launcher_name + ".exe")
        pyinstaller_command = f'pyinstaller --windowed --onefile --icon={launcher_icon_path} --name="{launcher_name}" --distpath="{pyinstaller_output_directory}" {new_tempfile.name}'
    else:
        error_message_popup("Output directory is required!")

    subprocess.call(pyinstaller_command, shell=False)

    if os.path.isfile(pyinstaller_output_directory + "\\" + launcher_name + ".exe"):
        info_message_popup("Executable created successfully!")
        return True
    else:
        error_message_popup("Executable creation failed!")
        return False
