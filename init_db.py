# init_db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('blood_bank.db')  # Creates DB if not exists
    with open('database/schema.sql', 'r') as f:
        conn.executescript(f.read())          # Executes the entire .sql file
    conn.commit()
    conn.close()
    print("✅ Database initialized with tables.")

if __name__ == "__main__":
    init_db()
