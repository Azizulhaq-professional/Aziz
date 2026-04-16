# Real Database Project (SQL + Business Thinking)

## 📌 Project Overview
This notebook implements a **Customer Order Management System** using **SQLite** and **Pandas**.  
It demonstrates relational database design, SQL joins, aggregation, and business queries that mirror real-world company logic.

---

## 🎯 Learning Goals
- Work like a Data Analyst / Backend Engineer.
- Design normalized relational databases.
- Write SQL queries for business insights.
- Compare SQL logic with Pandas equivalents.

---

## ⚙️ Database Design
Three tables were created to model customer orders:
- **Customers** → customer_id, name, city  
- **Products** → product_id, product_name, price  
- **Orders** → order_id, customer_id, product_id, quantity  

**Why 3 tables?**
- Avoid duplicate data  
- Enable scaling  
- Support fast queries  

---

## 📊 Business Queries Implemented
1. **Show All Orders (Full Details)**  
   - Join customers, products, and orders.  
   - Output: Customer, Product, Quantity, Total Price.  

2. **Customer Spending**  
   - Total amount spent per customer.  

3. **Top Customer**  
   - Identify highest spender (Ali).  

4. **Most Sold Product**  
   - Find product with highest sales volume (Mobile).  

5. **City-Wise Revenue**  
   - Lahore ₨130,000, Karachi ₨100,000.  

6. **Inactive Customers**  
   - Detect customers with no orders (Ahmed).  

---

## 🔄 SQL vs Pandas Comparison
| Purpose              | SQL Command | Pandas Equivalent |
|----------------------|-------------|-------------------|
| Combine tables       | `JOIN`      | `merge()`         |
| Group data           | `GROUP BY`  | `groupby()`       |
| Calculate totals     | `SUM()`     | `sum()`           |

---

## 🧠 Key Takeaways
- SQL joins allow combining multiple tables for complete business views.  
- Aggregation (`GROUP BY`) provides customer and product insights.  
- Subqueries and filtering detect advanced patterns (e.g., inactive customers).  
- Pandas and SQL share the same logic — different tools, same thinking.  

---

## 🚀 Skills Demonstrated
- Relational database design (SQLite)  
- SQL joins and aggregation  
- Business analytics queries  
- Pandas integration for clean reporting  
