# print("view books loaded")

# from tkinter import Toplevel, Label
# from services.fetch_records import get_all_books

# def open_view_books(root):
#     window = Toplevel(root)
#     window.title("All Books")
#     books = get_all_books()

#     Label(window, text="All Books", font=("Arial", 14)).pack(pady=10)
#     for book in books:
#         Label(window, text=str(book)).pack()


from tkinter import Toplevel, Label, Frame
from tkinter import ttk
from services.fetch_records import get_all_books

def open_view_books(root):
    window = Toplevel(root)
    window.title("All Books")
    window.geometry("900x500")

    Label(window, text="All Books", font=("Arial", 14)).pack(pady=10)

    columns = ("bookid", "title", "author", "subject", "dept", "qnty", "shelfno")
    tree = ttk.Treeview(window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col.title())
        tree.column(col, width=120)

    tree.pack(fill="both", expand=True)

    books = get_all_books()
    for book in books:
        tree.insert("", "end", values=book)
