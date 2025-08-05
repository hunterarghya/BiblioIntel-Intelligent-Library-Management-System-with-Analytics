print("issuebook loaded")

from tkinter import Toplevel, Label, Entry, Button, messagebox
from services.issue_logic import issue_book_to_student

print("issue_book.py loaded.")

def open_issue_book(root):
    window = Toplevel(root)
    window.title("Issue Book")
    window.geometry("400x350")

    Label(window, text="Issue Book", font=("Arial", 14)).pack(pady=10)

    fields = ['Student ID', 'Book ID']
    entries = {}

    for field in fields:
        Label(window, text=field).pack()
        entry = Entry(window)
        entry.pack()
        entries[field.lower().replace(" ", "_")] = entry

    Label(window, text="Issue Date (YYYY-MM-DD)").pack()
    issue_date_entry = Entry(window)
    issue_date_entry.pack()
    entries["issue_date"] = issue_date_entry

    def handle_issue():
        data = {key: entry.get() for key, entry in entries.items()}
        result = issue_book_to_student(data)
        if result == "OK":
            messagebox.showinfo("Success", "Book issued successfully.")
            window.destroy()
        else:
            messagebox.showerror("Error", result)

    Button(window, text="Issue Book", command=handle_issue).pack(pady=15)
