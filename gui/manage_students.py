# print("manage_students.py loaded.")


# from tkinter import Toplevel, Label, Entry, Button
# from models.student_model import save_student

# def open_manage_students(root):
#     window = Toplevel(root)
#     window.title("Manage Students")
#     window.geometry("400x500")

#     Label(window, text="Add New Student", font=("Arial", 14)).pack(pady=10)

#     fields = ['Student ID', 'Name', 'Phone', 'Semester', 'Year', 'Department']
#     entries = {}

#     for field in fields:
#         Label(window, text=field).pack()
#         entry = Entry(window)
#         entry.pack()
#         entries[field.lower().replace(" ", "_")] = entry

#     def save():
#         data = {key: entry.get() for key, entry in entries.items()}
#         save_student(data)

#     Button(window, text="Save Student", command=save).pack(pady=10)


print("manage_students.py loaded.")

from tkinter import Toplevel, Label, Entry, Button, messagebox
from models.student_model import save_student

def open_manage_students(root):
    window = Toplevel(root)
    window.title("Manage Students")
    window.geometry("400x500")

    Label(window, text="Add New Student", font=("Arial", 14)).pack(pady=10)

    fields = ['Student ID', 'Name', 'Phone', 'Semester', 'Year', 'Department']
    entries = {}

    for field in fields:
        Label(window, text=field).pack()
        entry = Entry(window)
        entry.pack()
        entries[field.lower().replace(" ", "_")] = entry

    def save():
        data = {key: entry.get() for key, entry in entries.items()}

        # Basic validation
        if not all(data.values()):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            save_student(data)
            messagebox.showinfo("Success", "Student successfully added!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save student.\n{str(e)}")

    Button(window, text="Save Student", command=save).pack(pady=10)
