from flask import Flask, request, jsonify

# create flask app
app = Flask(__name__)

# Home route (GET)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to Sales API"

# Example GET route
@app.route('/sales', methods=['GET'])
def get_sales():
    # sample data (replace with DB query if needed)
    sales_data = [
        {"name": "Ali", "product_name": "Laptop", "quantity": 1, "total": 1200.0},
        {"name": "Sara", "product_name": "Phone", "quantity": 2, "total": 1600.0}
    ]
    return jsonify(sales_data)

# Example GET route with filter
@app.route('/sales/<city>', methods=['GET'])
def get_sales_by_city(city):
    # sample filtered data
    filtered_data = [
        {"name": "Ali", "product_name": "Laptop", "quantity": 1, "total": 1200.0, "city": city}
    ]
    return jsonify(filtered_data)

# POST route
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    return jsonify({"message": f"Hello {name}, you are {age} years old"})

# run server
if __name__ == '__main__':
    app.run(debug=True)
