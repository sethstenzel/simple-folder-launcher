from classes.ui.main_window import AppMainWindow

app_name = "Simple Folder Launcher: Bulider"
app = AppMainWindow(
    title=app_name, icon="icons/default.ico", columns=3, rows=4, width=590, height=160
)
app.run()
