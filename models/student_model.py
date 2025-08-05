from db.database_utils import get_connection

def save_student(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO students (studid, name, phone, sem, year, dept)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data['student_id'],     
        data['name'],
        data['phone'],
        int(data['semester']),
        int(data['year']),
        data['department']
    ))

    conn.commit()
    conn.close()
    print("Student saved successfully.")
