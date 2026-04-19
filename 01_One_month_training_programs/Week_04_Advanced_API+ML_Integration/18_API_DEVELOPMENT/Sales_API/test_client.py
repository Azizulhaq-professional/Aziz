import requests

# 1. Add a new order
response = requests.post(
    "http://127.0.0.1:5000/add_order",
    json={"customer_id": 1, "product_id": 2, "quantity": 3}
)
print("POST /add_order:", response.json())

# 2. Fetch all sales to confirm the new order is saved
sales_response = requests.get("http://127.0.0.1:5000/sales")
print("GET /sales:", sales_response.json())

# 3. Add another order with different data
response2 = requests.post(
    "http://127.0.0.1:5000/add_order",
    json={"customer_id": 2, "product_id": 1, "quantity": 5}
)
print("POST /add_order (second):", response2.json())

# 4. Fetch sales again to confirm both orders are present
sales_response2 = requests.get("http://127.0.0.1:5000/sales")
print("GET /sales (after second insert):", sales_response2.json())
