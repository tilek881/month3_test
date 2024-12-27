import sqlite3

class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_tables(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS complaints (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    complaint TEXT NOT NULL
                );
            """)
            conn.commit()

    def insert_complaint(self, name: str, contact: str, complaint: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO complaints (name, contact, complaint)
                VALUES (?, ?, ?);
            """, (name, contact, complaint))
            conn.commit()

    def get_all_complaints(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, contact, complaint FROM complaints;")
            return cursor.fetchall()
