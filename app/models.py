import sqlite3

def init_db():
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS products (name TEXT, price REAL)")
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def validate_user(username, password):
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def add_product(name, price):
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()
    c.execute("INSERT INTO products VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    result = c.fetchall()
    conn.close()
    return result
