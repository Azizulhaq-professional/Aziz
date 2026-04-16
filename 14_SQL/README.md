# SQL Fundamentals with Python (SQLite + Pandas)

## 📌 Project Overview
This notebook demonstrates **SQL fundamentals** and their integration with **Python** using SQLite and Pandas.  
It covers database creation, data insertion, querying, filtering, aggregation, and grouping — all displayed in clean Pandas DataFrames.

---

## 🎯 Learning Goals
- Understand what SQL is and how databases work.
- Learn to retrieve and filter data like a backend/data engineer.
- Practice SQL commands (`SELECT`, `WHERE`, `ORDER BY`, `SUM`, `COUNT`, `AVG`, `GROUP BY`).
- Compare SQL queries with **Pandas equivalents** for interview readiness.

---

## ⚙️ Steps Implemented
1. **Database Setup**
   - Created SQLite database (`sales.db`).
   - Defined `employees` and `sales` tables.
   - Inserted sample records.

2. **Basic SQL Commands**
   - `SELECT *` → Retrieve all data.
   - `SELECT column` → Specific fields.
   - `WHERE` → Filtering rows (e.g., city = Lahore).
   - Multiple conditions with `AND`.
   - `ORDER BY` → Sorting results.

3. **Aggregate Functions**
   - `COUNT(*)` → Number of records.
   - `SUM(salary)` → Total salary.
   - `AVG(salary)` → Average salary.

4. **Grouping**
   - `GROUP BY` → Total sales by product or city.

---

## 📊 Sales Analysis Tasks
- **Task 1:** Get all sales data.  
- **Task 2:** Extract product and price columns.  
- **Task 3:** Filter sales where city = Lahore.  
- **Task 4:** Calculate total revenue (₨ 400,000).  
- **Task 5:** Compute total sales by product:  
  - Laptop → ₨160,000  
  - Mobile → ₨150,000  
  - Tablet → ₨90,000  

---

## 🔄 SQL vs Pandas Comparison
| SQL Command | Pandas Equivalent |
|-------------|-------------------|
| `SELECT * FROM sales` | `df` |
| `SELECT col` | `df['col']` |
| `WHERE city='Lahore'` | `df[df.city == 'Lahore']` |
| `SUM(price*qty)` | `(df.price*df.qty).sum()` |
| `GROUP BY product` | `df.groupby('product')` |

---

## 🧠 Key Takeaways
- **SQLite** acts as the database (storage).  
- **Cursor / Pandas** execute SQL queries.  
- **Pandas DataFrame** displays results in a clean, Excel‑like format.  
- SQL and Pandas are complementary: SQL is declarative, Pandas is procedural.  

---

## 🚀 Skills Demonstrated
- Database fundamentals (SQLite)
- SQL querying and filtering
- Aggregate analysis (`SUM`, `COUNT`, `AVG`)
- Business insights with `GROUP BY`
- Python integration with Pandas

---

## 📂 File Included
- `14_SQL.ipynb` → Notebook with full SQL + Python workflow

🚀 I, Aziz Ul Haq, am actively learning, building, and sharing — turning my skills in Python, AI, Data Science, and Cybersecurity into a professional portfolio.
