import sqlite3

def get_db_connection():
    conn = sqlite3.connect('blood_bank.db')
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn
