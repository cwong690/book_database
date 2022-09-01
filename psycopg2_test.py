import psycopg2

def create_table():
    # Create connection to psycopg2. If no database, new one will be created
    conn = psycopg2.connect("dbname='book_db' user='postgres' password='postgres123' host='localhost' port='5432'")

    # Add cursor
    cur = conn.cursor()

    # Create table and add value
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    # Commit changes and close
    conn.commit()
    conn.close()

def insert_in(item, quantity, price):
    conn = psycopg2.connect("dbname='book_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view_db():
    conn = psycopg2.connect("dbname='book_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='book_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='book_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

print(view_db())