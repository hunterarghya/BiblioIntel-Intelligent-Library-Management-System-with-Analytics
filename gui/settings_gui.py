# gui/settings_gui.py

import tkinter as tk
from tkinter import messagebox
from db.database_utils import get_connection

def open_settings_window():
    window = tk.Toplevel()
    window.title("Library Settings")

    tk.Label(window, text="Max Days Before Fine:").grid(row=0, column=0, padx=10, pady=10)
    maxdays_entry = tk.Entry(window)
    maxdays_entry.grid(row=0, column=1)

    tk.Label(window, text="Fine Per Day (₹):").grid(row=1, column=0, padx=10, pady=10)
    fine_entry = tk.Entry(window)
    fine_entry.grid(row=1, column=1)

    def load_settings():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT maxdays, fine FROM settings WHERE id = 1")
        result = cursor.fetchone()
        conn.close()
        if result:
            maxdays_entry.insert(0, str(result[0]))
            fine_entry.insert(0, str(result[1]))

    def save_settings():
        try:
            maxdays = int(maxdays_entry.get())
            fine = float(fine_entry.get())

            if maxdays <= 0 or fine < 0:
                raise ValueError

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE settings SET maxdays = ?, fine = ? WHERE id = 1", (maxdays, fine))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Settings updated successfully")
            window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid values")

    tk.Button(window, text="Save", command=save_settings).grid(row=2, column=0, columnspan=2, pady=10)

    load_settings()
