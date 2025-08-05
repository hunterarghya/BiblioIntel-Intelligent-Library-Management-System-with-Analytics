from db.database_utils import get_connection
import datetime

def issue_book_to_student(data):
    try:
        studid = data['student_id']
        bookid = data['book_id']
        issue_date = data['issue_date'] or datetime.date.today().isoformat()

        conn = get_connection()
        cursor = conn.cursor()

        # 1. Check book quantity
        cursor.execute("SELECT qnty FROM books WHERE bookid = ?", (bookid,))
        book = cursor.fetchone()
        if not book:
            return "Book not found."
        if book[0] <= 0:
            return "Book not available."

        # 2. Check student's current issued books
        cursor.execute("SELECT COUNT(*) FROM transactions WHERE studid=? AND return_date IS NULL", (studid,))
        issued_count = cursor.fetchone()[0]

        cursor.execute("SELECT maxbk FROM settings WHERE id=1")
        max_books = cursor.fetchone()[0]

        if issued_count >= max_books:
            return f"Student has already reached the issue limit of {max_books} books."

        # issue
        cursor.execute("""
            INSERT INTO transactions (bookid, studid, issue_date)
            VALUES (?, ?, ?)
        """, (bookid, studid, issue_date))

        # 4. Decrease book quantity
        cursor.execute("UPDATE books SET qnty = qnty - 1 WHERE bookid = ?", (bookid,))

        conn.commit()
        conn.close()
        return "OK"

    except Exception as e:
        return f"Error: {str(e)}"
