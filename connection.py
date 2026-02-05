import sqlite3
def get_connection():
    return sqlite3.connect('student.db')

#CREATE TABLE
def create_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("Table created successfully.")