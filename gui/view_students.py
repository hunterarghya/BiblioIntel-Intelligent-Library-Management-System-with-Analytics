

from tkinter import Toplevel, Label
from tkinter import ttk
from services.fetch_records import get_all_students

def open_view_students(root):
    window = Toplevel(root)
    window.title("All Students")
    window.geometry("800x500")

    Label(window, text="All Students", font=("Arial", 14)).pack(pady=10)

    columns = ("studid", "name", "phone", "semester", "year", "dept")
    tree = ttk.Treeview(window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col.title())
        tree.column(col, width=110)

    tree.pack(fill="both", expand=True)

    students = get_all_students()
    for student in students:
        tree.insert("", "end", values=student)
