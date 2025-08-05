from tkinter import Toplevel, Button, Label
from gui.manage_books import open_manage_books
from gui.manage_students import open_manage_students
from gui.view_books import open_view_books
from gui.view_students import open_view_students    
from gui.return_book_gui import open_return_book
from gui.issue_book import open_issue_book
from gui.view_transactions import open_view_transactions
from gui.settings_gui import open_settings_window
from gui.update_quantity import open_update_quantity_window





print("Using dashboard.py from:", __file__)
def open_dashboard(root):
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Library Management System", font=("Arial", 20)).pack(pady=20)

    Button(root, text="View All Books", width=30, command=lambda: open_view_books(root)).pack(pady=5)
    Button(root, text="View All Students", width=30, command=lambda: open_view_students(root)).pack(pady=5)
    Button(root, text="Manage Books", width=30, command=lambda: open_manage_books(root)).pack(pady=5)
    Button(root, text="Update Book Quantity", width=30, command=open_update_quantity_window).pack(pady=5)
    Button(root, text="Manage Students", width=30, command=lambda: open_manage_students(root)).pack(pady=5)
    Button(root, text="Issue Book", width=30, command=lambda: open_issue_book(root)).pack(pady=5)
    Button(root, text="Return Book", width=30, command=lambda: open_return_book(root)).pack(pady=5)
    Button(root, text="View Transaction History", width=30, command=lambda: open_view_transactions(root)).pack(pady=5)
    Button(root, text="Settings", width=30, command=open_settings_window).pack(pady=5)
    Button(root, text="Analytics", width=30, state="disabled").pack(pady=5)  # disabled for MVP
    Button(root, text="Exit", width=30, command=root.quit).pack(pady=20)
