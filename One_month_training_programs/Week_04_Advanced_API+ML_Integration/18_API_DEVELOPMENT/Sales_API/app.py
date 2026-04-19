from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
def get_db_connection():
    conn = sqlite3.connect("sales.db")
    conn.row_factory = sqlite3.Row
    return conn

#  CREATE TABLES FIRST TIME
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY,
        name TEXT,
        city TEXT)
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        product_name TEXT,
        price INTEGER)
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER)
    """)

    # insert sample data if empty
    cur.execute("SELECT COUNT(*) FROM customers")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO customers VALUES (1,'Ali','Lahore')")
        cur.execute("INSERT INTO customers VALUES (2,'Sara','Karachi')")

    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO products VALUES (1,'Laptop',100000)")
        cur.execute("INSERT INTO products VALUES (2,'Mobile',50000)")

    conn.commit()
    conn.close()

# -----------------------------
@app.route("/")
def home():
    return "Sales API Running Successfully!"

# -----------------------------
@app.route("/sales", methods=["GET"])
def get_sales():
    conn = get_db_connection()

    query = """
    SELECT customers.name, products.product_name, orders.quantity,
           (products.price * orders.quantity) AS total
    FROM orders
    JOIN customers ON orders.customer_id = customers.id
    JOIN products ON orders.product_id = products.id
    """

    data = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# -----------------------------
@app.route("/add_order", methods=["GET", "POST"])
def add_order():
    
    #  If user opens page in browser (GET request)
    if request.method == "GET":
        return """
        <h2>Add New Order</h2>
        <form method="POST">
            Customer ID:<br>
            <input type="number" name="customer_id"><br><br>
            
            Product ID:<br>
            <input type="number" name="product_id"><br><br>
            
            Quantity:<br>
            <input type="number" name="quantity"><br><br>
            
            <input type="submit" value="Add Order">
        </form>
        """

    #  If user clicks SUBMIT (POST request)
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        product_id = request.form["product_id"]
        quantity = request.form["quantity"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO orders (customer_id, product_id, quantity) VALUES (?,?,?)",
            (customer_id, product_id, quantity)
        )
        conn.commit()
        conn.close()

        return "<h3> Order added successfully!</h3><a href='/sales'>View Sales</a>"

# -----------------------------
if __name__ == "__main__":
    init_db()   #  VERY IMPORTANT
    app.run(debug=True)