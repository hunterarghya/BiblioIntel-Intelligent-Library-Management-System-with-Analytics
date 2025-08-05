# import sqlite3
# import os

# def get_connection():
#     return sqlite3.connect("library.db")

# def init_db():
#     if not os.path.exists("library.db"):
#         print("Initializing database...")
#     conn = get_connection()
#     with open("db/schema.sql", "r") as f:
#         schema = f.read()
#     conn.executescript(schema)
#     conn.commit()
#     conn.close()

import sys
import os
import sqlite3

def resource_path(relative_path):
    
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_connection():
    db_path = resource_path("library.db")
    return sqlite3.connect(db_path)

def init_db():
    db_path = resource_path("library.db")
    if not os.path.exists(db_path):
        print("Initializing database...")
    conn = get_connection()
    with open(resource_path("db/schema.sql"), "r") as f:
        schema = f.read()
    conn.executescript(schema)
    conn.commit()
    conn.close()
