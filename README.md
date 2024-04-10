# Simple Folder Launcher
## About
This is a simple utility that allows me to create a custom folder launcher with a folder icon with PyInstaller.
The end goal is to be able to pin the exe to the Windows taskbar, as Windows does not allow you to pin folders directly.

## Usage
1. Create a virtual env for Python 3.10.x (or possibly newer): `python -m venv venv`
2. Activate the virtual env: `.\venv\Scripts\activate`
3. Install the dependencies: `python -m pip install -r .\requirements.txt`
4. Launch the builder script: `python builder.py`
5. Enter your launcher executable name.
6. Enter your launcher folder path and your launcher icon path (or leave it blank for the default icon).
7. Press build, and your launcher should be built which will launch your desired folder.
8. Place the launcher somewhere on your system, and then drag it to the taskbar.

# Caveats
This was made with tkinter which is fine, but it is not threaded so the UI will lock up while working etc.
If someone feels ambitious they could put in a pull request to fix this. Tests would be welcome as well.

# Attributions
[app icon](https://www.flaticon.com/free-icon/folder_3039367?term=folder&page=1&position=94&origin=tag&related_id=3039367)