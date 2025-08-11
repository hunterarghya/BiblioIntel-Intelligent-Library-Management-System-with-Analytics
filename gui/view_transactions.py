
from tkinter import Toplevel, Label, Entry, Button, Frame, messagebox
from tkinter import ttk
from services.transactions_db import (
    get_transactions_by_student,
    get_transactions_by_book,
    get_all_transactions
)

def open_view_transactions(root):
    window = Toplevel(root)
    window.title("Transaction History")
    window.geometry("1000x500")  

    Label(window, text="Enter Student ID or Book ID:", font=("Arial", 12)).pack(pady=10)

    input_entry = Entry(window)
    input_entry.pack()

    button_frame = Frame(window)
    button_frame.pack(pady=10)

    # Treeview frame with scrollbars
    tree_frame = Frame(window)
    tree_frame.pack(pady=10, fill="both", expand=True)

    # Scrollbars
    y_scroll = ttk.Scrollbar(tree_frame)
    y_scroll.pack(side="right", fill="y")

    x_scroll = ttk.Scrollbar(tree_frame, orient="horizontal")
    x_scroll.pack(side="bottom", fill="x")

    # Table columns
    columns = ("studid", "student_name", "bookid", "title", "issue_date", "return_date", "fine")
    tree = ttk.Treeview(
        tree_frame,
        columns=columns,
        show="headings",
        yscrollcommand=y_scroll.set,
        xscrollcommand=x_scroll.set
    )

    # Configure scrollbars
    y_scroll.config(command=tree.yview)
    x_scroll.config(command=tree.xview)

    # Define column headers
    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title())
        tree.column(col, width=140, anchor="center")

    tree.pack(fill="both", expand=True)

    def clear_results():
        for row in tree.get_children():
            tree.delete(row)

    def display_transactions(data, mode):
        clear_results()
        if not data:
            messagebox.showinfo("No Results", "No transactions found.")
            return

        for tx in data:
            if mode == "student":
                tree.insert("", "end", values=(
                    tx["studid"], tx["student_name"], tx["bookid"], tx["title"],
                    tx["issue_date"], tx["return_date"], f"₹{tx['fine']:.2f}"
                ))
            elif mode == "book":
                tree.insert("", "end", values=(
                    tx["studid"], tx["student_name"], tx["bookid"], tx["title"],
                    tx["issue_date"], tx["return_date"], f"₹{tx['fine']:.2f}"
                ))
            else:  # All transactions
                tree.insert("", "end", values=(
                    tx["studid"], tx["student_name"], tx["bookid"], tx["title"],
                    tx["issue_date"], tx["return_date"], f"₹{tx['fine']:.2f}"
                ))

    def search_by_student():
        studid = input_entry.get().strip()
        if not studid:
            messagebox.showwarning("Input Error", "Enter Student ID")
            return
        data = get_transactions_by_student(studid)
        display_transactions(data, mode="student")

    def search_by_book():
        bookid = input_entry.get().strip()
        if not bookid:
            messagebox.showwarning("Input Error", "Enter Book ID")
            return
        data = get_transactions_by_book(bookid)
        display_transactions(data, mode="book")

    def show_all():
        data = get_all_transactions()
        display_transactions(data, mode="all")

    # Buttons
    Button(button_frame, text="Search by Student ID", command=search_by_student, width=20).grid(row=0, column=0, padx=5)
    Button(button_frame, text="Search by Book ID", command=search_by_book, width=20).grid(row=0, column=1, padx=5)
    Button(button_frame, text="View All Transactions", command=show_all, width=20).grid(row=0, column=2, padx=5)
