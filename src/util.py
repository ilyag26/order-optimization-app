import sqlite3
from tkinter import ttk, messagebox

def remove_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()

def get_data(entry_login,state):
     with sqlite3.connect('src/app/db/database.db') as db:
        cursor = db.cursor()
        login = entry_login.get()
        cursor.execute(f"SELECT * FROM users WHERE login = '{str(login)}'")
        for user in cursor:
                passw = user[state]
        return passw