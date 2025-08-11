# gui/manage_books.py



print ("loading successful")

from tkinter import Toplevel, Label, Entry, Button, messagebox
import sqlite3
from db.database_utils import get_connection

def open_manage_books(root):
    window = Toplevel(root)
    window.title("Manage Books")
    window.geometry("400x400")

    Label(window, text="Add New Book", font=("Arial", 14)).pack(pady=10)

    fields = ['Book ID', 'Title', 'Author', 'Subject', 'Department', 'Quantity', 'Shelf No']
    entries = {}

    for field in fields:
        Label(window, text=field).pack()
        entry = Entry(window)
        entry.pack()
        entries[field.lower().replace(" ", "_")] = entry

    

    def save_book():
        
        conn = sqlite3.connect("library.db")
        cur = conn.cursor()

        try:
            data = {key: entry.get() for key, entry in entries.items()}

            # Basic validation
            if not all(data.values()):
                raise ValueError("Please fill in all fields.")

            cur.execute("""
                INSERT INTO books (bookid, title, author, subject, dept, qnty, shelfno)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                data['book_id'],
                data['title'],
                data['author'],
                data['subject'],
                data['department'],
                int(data['quantity']),
                data['shelf_no']
            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Book successfully added!")
            window.destroy()  

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", "Failed to add book.\n" + str(e))
            conn.close()


    # def save_book():
    #     # data = {key: entry.get() for key, entry in entries.items()}
    #     # print("Saving book:", data)

    #     # insert_book(data)  # Connect to DB

    #     # import sqlite3
    #     # conn = sqlite3.connect("library.db")
    #     # cur = conn.cursor()

    #     # data = {key: entry.get() for key, entry in entries.items()}
    #     # print("Saving book:", data)

    #     # cur.execute("""
    #     #     INSERT INTO books (bookid, title, author, subject, dept, qnty, shelfno)
    #     #     VALUES (?, ?, ?, ?, ?, ?, ?)
    #     # """, (
    #     #     data['book_id'],
    #     #     data['title'],
    #     #     data['author'],
    #     #     data['subject'],
    #     #     data['department'],
    #     #     int(data['quantity']),
    #     #     data['shelf_no']
    #     # ))

    #     # conn.commit()
    #     # conn.close()
    #     # print("Book inserted successfully.")
    #     conn = get_connection()
    #     cur = conn.cursor()

    #     data = {key: entry.get() for key, entry in entries.items()}
    #     print("Saving book:", data)

    #     try:
    #         cur.execute("""
    #             INSERT INTO books (bookid, title, author, subject, dept, qnty, shelfno)
    #             VALUES (?, ?, ?, ?, ?, ?, ?)
    #         """, (
    #             data['book_id'],
    #             data['title'],
    #             data['author'],
    #             data['subject'],
    #             data['department'],
    #             int(data['quantity']),
    #             data['shelf_no']
    #         ))
    #         conn.commit()
    #         print("Book inserted successfully.")
    #     except sqlite3.IntegrityError:
    #         messagebox.showerror("Error", "Book ID already exists.")
    #     finally:
    #         conn.close()

    Button(window, text="Save Book", command=save_book).pack(pady=10)
