# 🧹 Data Cleaning + Filtering – Sales Dataset

This notebook demonstrates **data cleaning and filtering techniques using Pandas**, a critical skill for every data analyst.  
It introduces common problems in real-world datasets and shows how to systematically clean and filter data for meaningful insights.

---

## 📘 Concepts Covered
- **Why Data Cleaning?** – Real datasets often contain missing values, duplicates, wrong values, and extra spaces  
- **Detecting Issues:** Using `isnull()` and `isnull().sum()` to identify missing data  
- **Handling Missing Values:**  
  - Remove incomplete rows (`dropna()`)  
  - Fill missing values with defaults or averages (`fillna()`)  
- **Removing Duplicates:** `drop_duplicates()`  
- **Cleaning Text:** Stripping extra spaces with `.str.strip()`  
- **Filtering Data:**  
  - By city (e.g., Islamabad sales)  
  - By numeric conditions (e.g., price > 60000)  
  - Multiple conditions combined with logical operators  

---

## 🧩 Mini Project: Cleaning & Filtering Sales Data

A professional project that demonstrates how to transform messy sales data into clean, structured datasets ready for analysis.

### Features
- Load a deliberately “dirty” dataset with missing values, duplicates, and extra spaces  
- Apply cleaning steps to fix issues  
- Create a calculated column (`total = price * quantity`)  
- Filter data by city, high-value sales, and multiple conditions  

---

## 🖥️ Example Run
```
Original Data:
name  product   price  quantity       city
0    Ali   Laptop  80000.0       1.0  Islamabad
1  Ahmed   Mobile  50000.0       2.0     Lahore
2   Sara   Tablet      NaN       1.0    Karachi
3  Usman   Laptop  80000.0       1.0  Islamabad
4 Ayesha   Mobile  50000.0       NaN     Lahore
5    Ali   Laptop  80000.0       1.0  Islamabad
6          Tablet  30000.0       1.0    Karachi

Cleaned Data:
name  product   price  quantity       city  total
0    Ali   Laptop  80000.0       1.0  Islamabad  80000.0
1  Ahmed   Mobile  50000.0       2.0     Lahore 100000.0
2   Sara   Tablet  30000.0       1.0    Karachi  30000.0
3  Usman   Laptop  80000.0       1.0  Islamabad  80000.0
4 Ayesha   Mobile  50000.0       3.0     Lahore 150000.0

Islamabad Sales:
name  product   price  quantity       city   total
0    Ali   Laptop  80000.0       1.0  Islamabad  80000.0
3  Usman   Laptop  80000.0       1.0  Islamabad  80000.0

High Price Products:
name  product   price  quantity       city   total
0    Ali   Laptop  80000.0       1.0  Islamabad  80000.0
3  Usman   Laptop  80000.0       1.0  Islamabad  80000.0
```

---

## ⚙️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Azizulhaq-professional/Aziz.git
2. Open 09_Data_Cleaning+Filtering.ipynb in Google Colab or Jupyter Notebook.
3. Run cells sequentially from top to bottom.
4. Observe how the dataset is cleaned and filtered step by step.

🚀 I, Aziz Ul Haq, am actively learning, building, and sharing — turning my skills in Python, AI, Data Science, and Cybersecurity into a professional portfolio.
