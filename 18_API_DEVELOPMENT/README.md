# Sales Data API

## 📌 Project Overview
This project demonstrates how to build a simple **Sales Data API** using Python, Flask, and SQLite.  
The API serves data from a database, returns results in JSON format, and can be integrated with frontend applications.

---

## 🎯 Goals
- Serve sales data from a SQLite database  
- Return results in JSON format  
- Provide endpoints for filtering and inserting data  
- Enable frontend or apps to consume API responses  

---

## ⚙️ Technology Stack
- **Python**  
- **Flask**  
- **SQLite**  
- **Pandas**

---

## 🚀 Setup Instructions
1. Install Flask:
   ```bash
   pip install flask
2. Create a project folder SalesAPI and open it in VS Code.
3.Add the main file app.py with the following structure:
- Basic Flask app
- Database connection function
- API endpoints for fetching, filtering, and inserting data

Run the server:
```
python app.py
```
Open in browser:
```
http://127.0.0.1:5000/
```
## 🔑 API Endpoints
1. Home
```
GET /
```
Response:
```
Welcome to Sales API
```
2. Get Sales Data
```
GET /sales
```
Returns all sales records with customer, product, quantity, and total.

3. Filter Sales by City
```
GET /sales/<city>
```
Filters sales data by customer city.

Example: http://127.0.0.1:5000/sales/Lahore

4. Add New Order
```
POST /add_order
```
Request body:
```
{
  "customer_id": 1,
  "product_id": 2,
  "quantity": 3
}
```
Response:
```
{"message": "Order added successfully"}
```
## 📸 Screenshots (Project Results)

## 📖 Conclusion
This project provides a beginner-friendly introduction to API development with Flask.
The linked screenshots illustrate each stage of the API in action, from setup to data retrieval and order insertion.
