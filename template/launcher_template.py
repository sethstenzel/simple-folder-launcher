from pathlib import Path
import os


def check_path_exists(directory):
    directory = Path(directory)
    return directory.exists()


def launch_directory(directory):
    os.startfile(str(directory) + "\\")


def main(directory):
    if check_path_exists(directory):
        launch_directory(directory)


if __name__ == "__main__":
    directory = r"%%%PATH_STRING%%%"
    main(directory)
