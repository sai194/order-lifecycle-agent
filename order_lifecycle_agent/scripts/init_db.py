import sqlite3

conn = sqlite3.connect("data/orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT,
    order_status TEXT,
    order_date TEXT,
    delivery_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS returns (
    order_id TEXT,
    return_status TEXT,
    refund_status TEXT,
    return_date TEXT
)
""")

cursor.execute("DELETE FROM orders")
cursor.execute("DELETE FROM returns")

cursor.execute("INSERT INTO orders VALUES ('1001','DELIVERED','2026-04-20','2026-04-25')")
cursor.execute("INSERT INTO returns VALUES ('1001','COMPLETED','INITIATED','2026-04-27')")

conn.commit()
conn.close()
