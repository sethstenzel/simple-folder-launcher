# Simple Folder Launcher
## About
This is a simple utility that allows me to create a custom folder launcher with a folder icon with PyInstaller.
The end goal is to be able to pin the exe to the Windows taskbar, as Windows does not allow you to pin folders directly.

## Requirements
This was built with Python version 3.10.4, pyinstaller and some other packages are known to lag behind for newer versions of Python meaning `python -m pip install ./requirements` may not work for you on newer versions until those modules have pip installable packages for newer versions.

## Usage
1. Create a virtual env for Python 3.10.x (or possibly newer): `python -m venv venv`
2. Activate the virtual env: `.\venv\Scripts\activate`
3. Install the dependencies: `python -m pip install -r .\requirements.txt`
4. Launch the builder script: `python builder.py`
5. Enter your launcher executable name.
6. Enter your launcher folder path and your launcher icon path (or leave it blank for the default icon).
7. Press build, and your launcher should be built which will launch your desired folder.
8. Place the launcher somewhere on your system, and then drag it to the taskbar.

# Atrributions
[app icon](https://www.flaticon.com/free-icon/folder_3039367?term=folder&page=1&position=94&origin=tag&related_id=3039367)