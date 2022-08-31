import sqlite3

def create_table():
    # Create connection to sqlite3. If no database, new one will be created
    conn = sqlite3.connect("lite.db")

    # Add cursor
    cur = conn.cursor()

    # Create table and add value
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    # Commit changes and close
    conn.commit()
    conn.close()

def insert_in(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view_db():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

print(view_db())
