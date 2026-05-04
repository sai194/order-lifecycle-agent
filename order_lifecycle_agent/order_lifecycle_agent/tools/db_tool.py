import sqlite3

def get_order_details(order_id: str):
    conn = sqlite3.connect("data/orders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
    order = cursor.fetchone()

    cursor.execute("SELECT * FROM returns WHERE order_id=?", (order_id,))
    ret = cursor.fetchone()

    conn.close()

    return {"order": order, "return": ret}
