# Simple Folder Launcher
## About
This is a simple utility that allows the creation of a custom folder launcher with custom a folder icon via PyInstaller.
The end goal is to be able to pin an exe to the Windows taskbar which will luanch a spesific folder, as Windows does not allow you to pin folders directly.

## Usage
1. Create a virtual env for Python 3.10.4 (or possibly newer): `python -m venv venv`
2. Activate the virtual env: `.\venv\Scripts\activate`
3. Install the dependencies: `python -m pip install -r .\requirements.txt`
4. Launch the builder script: `python builder.py`
5. Enter your launcher executable name.
6. Enter your launcher folder path and your launcher icon path (or leave it blank for the default icon).
7. Press build, and your launcher should be built which will launch your desired folder.
8. Place the launcher somewhere on your system, and then drag it to the taskbar.

## Caveats
This was made with tkinter which is fine, but it is not threaded so the UI will lock up while things are building etc.
If someone feels ambitious they could put in a pull request to fix this. Tests would be welcome as well. Both are low priority for me.

# Attributions
[Application Icon](https://www.flaticon.com/free-icon/folder_3039367?term=folder&page=1&position=94&origin=tag&related_id=3039367)
