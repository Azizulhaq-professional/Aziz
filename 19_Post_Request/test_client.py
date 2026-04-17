import requests

# Test POST route
url = "http://127.0.0.1:5000/submit"
data = {"name": "Ali", "age": 22}

response = requests.post(url, json=data)
print("POST /submit response:", response.json())

# Test GET route
url_sales = "http://127.0.0.1:5000/sales"
response_sales = requests.get(url_sales)
print("GET /sales response:", response_sales.json())

# Test GET route with city filter
url_city = "http://127.0.0.1:5000/sales/Lahore"
response_city = requests.get(url_city)
print("GET /sales/Lahore response:", response_city.json())
