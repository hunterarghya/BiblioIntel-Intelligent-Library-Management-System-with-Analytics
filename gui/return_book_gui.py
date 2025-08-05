# gui/return_book.py

print("return_book.py loaded.")
print("Available symbols in return_book.py:", dir())


from tkinter import Toplevel, Label, Entry, Button, Frame, messagebox
from services.return_logic import return_book_for_student, get_issued_books_for_student

def open_return_book(root):
    window = Toplevel(root)
    window.title("Return Book")
    window.geometry("500x400")

    Label(window, text="Enter Student ID", font=("Arial", 12)).pack(pady=10)
    entry_studid = Entry(window)
    entry_studid.pack()

    result_frame = Frame(window)
    result_frame.pack(pady=10)

    def search_issued_books():
        for widget in result_frame.winfo_children():
            widget.destroy()

        studid = entry_studid.get().strip()
        if not studid:
            messagebox.showwarning("Input Error", "Please enter a student ID.")
            return

        books = get_issued_books_for_student(studid)

        if not books:
            Label(result_frame, text="No books found or all books returned.").pack()
            return

        for book in books:
            Label(result_frame, text=f"{book['bookid']} - {book['title']} (Issued: {book['issue_date']})").pack()

            Button(result_frame, text="Return", command=lambda b=book: return_selected_book(b, result_frame)).pack(pady=5)

    def return_selected_book(book, frame):
        msg = return_book_for_student(book)
        messagebox.showinfo("Return Book", msg)
        search_issued_books()  # Refresh

    Button(window, text="Search", command=search_issued_books).pack(pady=10)
