# services/return_logic.py

print("return_logic.py loaded.")

from db.database_utils import get_connection
import datetime

def get_issued_books_for_student(studid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t.bookid, b.title, t.issue_date
        FROM transactions t
        JOIN books b ON t.bookid = b.bookid
        WHERE t.studid = ? AND t.return_date IS NULL
    """, (studid,))
    
    results = cursor.fetchall()
    conn.close()

    books = []
    for row in results:
        books.append({
            "bookid": row[0],
            "title": row[1],
            "issue_date": row[2],
            "studid": studid
        })

    return books


def return_book_for_student(book):
    # conn = get_connection()
    # cursor = conn.cursor()

    # today = datetime.date.today()
    # issue_date = datetime.datetime.strptime(book['issue_date'], "%Y-%m-%d").date()

    # # Load settings
    # cursor.execute("SELECT fine, maxdays FROM settings WHERE id=1")
    # fine_per_day, maxdays = cursor.fetchone()

    # days_late = (today - issue_date).days - maxdays
    # fine = fine_per_day * days_late if days_late > 0 else 0

    # # Update transaction
    # cursor.execute("""
    #     UPDATE transactions
    #     SET return_date = ?, stud_fine = ?
    #     WHERE studid = ? AND bookid = ? AND return_date IS NULL
    # """, (today.isoformat(), fine, book['studid'], book['bookid']))

    # # Increment book quantity
    # cursor.execute("UPDATE books SET qnty = qnty + 1 WHERE bookid = ?", (book['bookid'],))

    # conn.commit()
    # conn.close()

    # return f"Returned successfully. Fine: ₹{fine:.2f}"

    try:
        conn = get_connection()
        cursor = conn.cursor()

        today = datetime.date.today()
        issue_date = datetime.date.fromisoformat(book['issue_date'])

        # Calculate difference in days
        days_held = (today - issue_date).days
        allowed_days = 14  # grace period
        fine_per_day = 2  # Rs. per day

        fine = 0
        if days_held > allowed_days:
            fine = (days_held - allowed_days) * fine_per_day

        # Update return date and fine in transactions table
        cursor.execute("""
            UPDATE transactions
            SET return_date = ?, stud_fine = ?
            WHERE bookid = ? AND studid = ? AND return_date IS NULL
        """, (today.isoformat(), fine, book['bookid'], book['studid']))

        # Increase book quantity back by 1
        cursor.execute("UPDATE books SET qnty = qnty + 1 WHERE bookid = ?", (book['bookid'],))

        conn.commit()
        conn.close()

        return f"Book returned. Fine: ₹{fine:.2f}"

    except Exception as e:
        return f"Error: {str(e)}"
