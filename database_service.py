import sqlite3
from datetime import datetime

def save_file_info(email, file_path, database):
    """Сохраняет информацию о загруженном файле в базу данных."""
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("INSERT INTO files (email, file_path, upload_date) VALUES (?, ?, ?)",
              (email, file_path, datetime.now()))
    conn.commit()
    conn.close()

def create_files_table(database):
    """Создает таблицу 'files' в базе данных, если она еще не существует."""
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS files
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 email TEXT,
                 file_path TEXT,
                 upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()
