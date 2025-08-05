from tkinter import Tk, Button
from gui.dashboard import open_dashboard
from db.database_utils import init_db

def run_app():
    # Initialize DB on first run
    init_db()

    # Main window
    root = Tk()
    root.title("Library Management System")
    root.geometry("600x400")

    # Open Dashboard
    open_dashboard(root)

    root.mainloop()

if __name__ == "__main__":
    run_app()
