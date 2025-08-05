# models/book_model.py

from db.database_utils import get_connection

def insert_book(book):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO books (bookid, title, author, subject, dept, qnty, shelfno)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            book['book_id'],
            book['title'],
            book['author'],
            book['subject'],
            book['department'],
            int(book['quantity']),
            book['shelf_no']
        ))

        conn.commit()
        print("Book inserted successfully!")

    except Exception as e:
        print("Error inserting book:", e)

    finally:
        conn.close()
