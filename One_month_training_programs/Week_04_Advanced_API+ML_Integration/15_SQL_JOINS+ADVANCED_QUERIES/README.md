# SQL Joins + Advanced Queries

## 📌 Project Overview
This notebook demonstrates how to use **SQL joins** and advanced queries with **SQLite** and **Pandas**.  
It covers combining multiple tables, performing aggregations, using subqueries, and handling missing relationships — all essential skills for backend development and data engineering.

---

## 🎯 Learning Goals
- Understand why joins are needed in relational databases.
- Learn different types of joins (`INNER`, `LEFT`, `RIGHT`, `FULL`).
- Apply joins to solve real-world problems (e.g., customer orders).
- Use aggregation (`GROUP BY`) and subqueries for business insights.
- Integrate SQL with Python for clean analysis and reporting.

---

## ⚙️ Steps Implemented
1. **Database Setup**
   - Created SQLite database (`company.db`).
   - Defined `customers` and `orders` tables.
   - Inserted sample records.

2. **Joins**
   - `INNER JOIN` → Match customers with their orders.
   - `LEFT JOIN` → Show all customers, including those without orders.
   - `RIGHT JOIN` → Show all orders, even if customer info is missing.
   - `FULL JOIN` → Display all data across both tables.

3. **Advanced Queries**
   - Aggregation with `GROUP BY` to calculate total spending per customer.
   - Subquery to identify the highest spender.
   - Filtering with `NULL` to find customers who placed no orders.

---

## 📊 Project Tasks
- **Task 1:** Join customers and orders to show who bought what.  
- **Task 2:** Calculate total spending per customer.  
- **Task 3:** Find the customer who spent the most (Ali).  
- **Task 4:** Identify customers with no orders (Ahmed).  

---

## 🔄 Key Concepts
| Concept        | Meaning                          |
|----------------|----------------------------------|
| INNER JOIN     | Only matching rows               |
| LEFT JOIN      | All left table rows + matches    |
| GROUP BY + JOIN| Business analytics (totals)      |
| Subquery       | Query inside another query       |
| NULL filtering | Find missing relationships       |

---

## 🧠 Key Takeaways
- **Joins** combine data across multiple tables using a common column.  
- **GROUP BY** enables powerful business insights like customer spending.  
- **Subqueries** allow advanced filtering and ranking.  
- **SQLite + Pandas** integration makes results easy to analyze and visualize.  

---

## 🚀 Skills Demonstrated
- Relational database design
- SQL joins and filtering
- Aggregation and subqueries
- Business analytics with SQL
- Python integration with Pandas

