from tkinter import Toplevel, Label
from services.fetch_records import get_all_students

def open_view_students(root):
    window = Toplevel(root)
    window.title("All Students")
    students = get_all_students()

    Label(window, text="All Students", font=("Arial", 14)).pack(pady=10)
    for student in students:
        Label(window, text=str(student)).pack()
