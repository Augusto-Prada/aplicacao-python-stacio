import sqlite3

def connect_db():
    return sqlite3.connect('business_management.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      description TEXT NOT NULL,
                      amount REAL NOT NULL,
                      date TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS budget (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      total REAL NOT NULL,
                      spent REAL NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def get_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_transaction(description, amount, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transactions (description, amount, date) VALUES (?, ?, ?)',
                   (description, amount, date))
    conn.commit()
    conn.close()

def get_transactions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def set_budget(total, spent):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO budget (total, spent) VALUES (?, ?)', (total, spent))
    conn.commit()
    conn.close()

def get_budget():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM budget ORDER BY id DESC LIMIT 1')
    budget = cursor.fetchone()
    conn.close()
    return budget
