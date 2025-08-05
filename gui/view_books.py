print("view books loaded")

from tkinter import Toplevel, Label
from services.fetch_records import get_all_books

def open_view_books(root):
    window = Toplevel(root)
    window.title("All Books")
    books = get_all_books()

    Label(window, text="All Books", font=("Arial", 14)).pack(pady=10)
    for book in books:
        Label(window, text=str(book)).pack()
