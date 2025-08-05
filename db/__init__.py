import sys
import os
import sqlite3

def resource_path(relative_path):
    # Use _MEIPASS if bundled by PyInstaller
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

def get_connection():
    db_path = resource_path("library.db")
    return sqlite3.connect(db_path)

def init_db():
    conn = get_connection()
    schema_path = resource_path(os.path.join("db", "schema.sql"))
    if os.path.exists(schema_path):
        with open(schema_path, "r") as f:
            schema = f.read()
        conn.executescript(schema)
        conn.commit()
    conn.close()
