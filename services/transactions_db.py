from db.database_utils import get_connection

def get_transactions_by_student(studid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t.bookid, b.title, t.issue_date, t.return_date, t.stud_fine
        FROM transactions t
        JOIN books b ON t.bookid = b.bookid
        WHERE t.studid = ?
        ORDER BY t.issue_date DESC
    """, (studid,))
    
    rows = cursor.fetchall()
    conn.close()

    return _map_transaction_rows(rows)

def get_transactions_by_book(bookid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t.studid, s.name, t.issue_date, t.return_date, t.stud_fine
        FROM transactions t
        JOIN students s ON t.studid = s.studid
        WHERE t.bookid = ?
        ORDER BY t.issue_date DESC
    """, (bookid,))
    
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "studid": row[0],
            "student_name": row[1],
            "issue_date": row[2],
            "return_date": row[3] or "Not Returned",
            "fine": row[4]
        } for row in rows
    ]

def get_all_transactions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t.studid, s.name, t.bookid, b.title, t.issue_date, t.return_date, t.stud_fine
        FROM transactions t
        JOIN books b ON t.bookid = b.bookid
        JOIN students s ON t.studid = s.studid
        ORDER BY t.issue_date DESC
    """)
    
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "studid": row[0],
            "student_name": row[1],
            "bookid": row[2],
            "title": row[3],
            "issue_date": row[4],
            "return_date": row[5] or "Not Returned",
            "fine": row[6]
        } for row in rows
    ]

def _map_transaction_rows(rows):
    return [
        {
            "bookid": row[0],
            "title": row[1],
            "issue_date": row[2],
            "return_date": row[3] or "Not Returned",
            "fine": row[4]
        } for row in rows
    ]

print("transactions_db symbols:", dir())

