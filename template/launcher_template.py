from pathlib import Path
import os
<<<<<<< HEAD:template/launcher_template.py
=======
import sys


def get_users_document_folder():
    try:
        user_profile = os.environ["USERPROFILE"]
    except KeyError:
        raise

    users_document_folder = os.path.join(user_profile, "Documents")
    if check_path_exists(users_document_folder):
        return users_document_folder
    return None
>>>>>>> a606962ac930fde7fb067cbe318b9baa416eec94:simple_folder_launcher.py


def check_path_exists(directory):
    directory = Path(directory)
    return directory.exists()


def launch_directory(directory):
    os.startfile(str(directory) + "\\")


def main(directory):
    if 2 <= len(sys.argv) and "-p" in sys.argv[1]:
        pass
    elif 2 == len(sys.argv) and "-h" in sys.argv[1]:
        pass
    elif 2 <= len(sys.argv):
        print(f"Error - Invalid command switch: {sys.argv[1]}")
    if check_path_exists(directory):
        launch_directory(directory)


if __name__ == "__main__":
<<<<<<< HEAD:template/launcher_template.py
    directory = r"%%%PATH_STRING%%%"
    main(directory)
=======
    main()
>>>>>>> a606962ac930fde7fb067cbe318b9baa416eec94:simple_folder_launcher.py
