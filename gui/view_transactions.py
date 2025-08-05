from tkinter import Toplevel, Label, Entry, Button, Frame, messagebox
from services.transactions_db import (
    get_transactions_by_student,
    get_transactions_by_book,
    get_all_transactions
)

def open_view_transactions(root):
    window = Toplevel(root)
    window.title("Transaction History")
    window.geometry("700x500")

    Label(window, text="Enter Student ID or Book ID:", font=("Arial", 12)).pack(pady=10)

    input_entry = Entry(window)
    input_entry.pack()

    button_frame = Frame(window)
    button_frame.pack(pady=10)

    result_frame = Frame(window)
    result_frame.pack(pady=10)

    def clear_results():
        for widget in result_frame.winfo_children():
            widget.destroy()

    def display_transactions(data, mode):
        clear_results()
        if not data:
            Label(result_frame, text="No records found.").pack()
            return

        for tx in data:
            if mode == "student":
                text = f"{tx['bookid']} - {tx['title']} | Issued: {tx['issue_date']} | Returned: {tx['return_date']} | Fine: ₹{tx['fine']:.2f}"
            elif mode == "book":
                text = f"{tx['studid']} - {tx['student_name']} | Issued: {tx['issue_date']} | Returned: {tx['return_date']} | Fine: ₹{tx['fine']:.2f}"
            else:  # all
                text = f"{tx['studid']} - {tx['student_name']} | {tx['bookid']} - {tx['title']} | Issued: {tx['issue_date']} | Returned: {tx['return_date']} | Fine: ₹{tx['fine']:.2f}"
            Label(result_frame, text=text, anchor="w", justify="left").pack(fill="x")

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

    Button(button_frame, text="Search by Student ID", command=search_by_student, width=20).grid(row=0, column=0, padx=5)
    Button(button_frame, text="Search by Book ID", command=search_by_book, width=20).grid(row=0, column=1, padx=5)
    Button(button_frame, text="View All Transactions", command=show_all, width=20).grid(row=0, column=2, padx=5)
