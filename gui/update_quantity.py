# gui/update_quantity.py

import tkinter as tk
from tkinter import messagebox
from db.database_utils import get_connection

def open_update_quantity_window():
    window = tk.Toplevel()
    window.title("Update Book Quantity")

    tk.Label(window, text="Enter Book ID:").grid(row=0, column=0, padx=10, pady=10)
    bookid_entry = tk.Entry(window)
    bookid_entry.grid(row=0, column=1, padx=10, pady=10)

    info_label = tk.Label(window, text="", fg="blue")
    info_label.grid(row=1, column=0, columnspan=2)

    def fetch_book():
        bookid = bookid_entry.get().strip()
        if not bookid:
            messagebox.showerror("Error", "Book ID is required")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title, qnty FROM books WHERE bookid = ?", (bookid,))
        result = cursor.fetchone()
        conn.close()

        if result:
            title, qnty = result
            info_label.config(text=f"{title} | Current Quantity: {qnty}")
            quantity_frame(bookid, title, qnty)
        else:
            info_label.config(text="Book not found.")

    def quantity_frame(bookid, title, qnty):
        def add_quantity():
            try:
                to_add = int(add_entry.get())
                if to_add < 0:
                    raise ValueError
                new_qnty = qnty + to_add
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE books SET qnty = ? WHERE bookid = ?", (new_qnty, bookid))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", f"Quantity updated to {new_qnty}")
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter valid positive integer")

        def set_quantity():
            try:
                new_qnty = int(set_entry.get())
                if new_qnty < 0:
                    raise ValueError
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE books SET qnty = ? WHERE bookid = ?", (new_qnty, bookid))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", f"Quantity set to {new_qnty}")
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter valid positive integer")

        def delete_book():
            confirm = messagebox.askyesno("Confirm", f"Delete book '{title}'?")
            if confirm:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM books WHERE bookid = ?", (bookid,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Deleted", "Book deleted successfully.")
                window.destroy()

        # Add Quantity
        tk.Label(window, text="Add Quantity:").grid(row=3, column=0)
        add_entry = tk.Entry(window)
        add_entry.grid(row=3, column=1)
        tk.Button(window, text="Add", command=add_quantity).grid(row=3, column=2)

        # Set Quantity
        tk.Label(window, text="Set Quantity:").grid(row=4, column=0)
        set_entry = tk.Entry(window)
        set_entry.grid(row=4, column=1)
        tk.Button(window, text="Set", command=set_quantity).grid(row=4, column=2)

        # Delete Book
        tk.Button(window, text="🗑️ Delete Book", fg="red", command=delete_book).grid(row=5, column=0, columnspan=3, pady=10)

    tk.Button(window, text="Search", command=fetch_book).grid(row=0, column=2)

