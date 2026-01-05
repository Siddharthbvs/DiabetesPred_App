import sqlite3

DB_NAME = 'database.db'
def __init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

    def add_user(usename,passsword):
        conn = get_connectio()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (usename, passsword))
    conn.commit()
    conn.close()

    def check_user(usename,passsword):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (usename, passsword))
        user = cursor.fetchone()
        conn.close()
        return user is not None