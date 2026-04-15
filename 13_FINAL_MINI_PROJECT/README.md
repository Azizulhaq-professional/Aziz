# 📊 Smart Sales Analysis Dashboard – Final Mini Project

This notebook demonstrates how to build a **complete advanced sales dashboard system** using Pandas and Matplotlib.  
It integrates **data cleaning, analysis, visualization, and smart insights** into one structured workflow, simulating a real industry project.

---

## 📘 Concepts Covered
- **Data Handling:**  
  - Load CSV files into Pandas DataFrames  
  - Handle missing values  
  - Remove duplicates and empty names  
  - Clean text fields  
  - Create calculated columns (`total = price * quantity`)  

- **Analysis:**  
  - Total revenue  
  - Sales by product  
  - Sales by city  
  - Most sold product  
  - Top customer  
  - Cheapest product  

- **Visualization:**  
  - Bar chart – Sales by product  
  - Pie chart – Sales by city  
  - Histogram – Price distribution  

- **Smart Insights (Interview-Level):**  
  - Best revenue city  
  - Best selling product  

---

## 🧩 Project Workflow

### Features
- Modular functions for each step (`load_data`, `clean_data`, `analyze`, `visualize`, `insights`)  
- End-to-end execution via `main()` function  
- Clear separation of responsibilities for readability and reusability  
- Outputs structured insights and visualizations directly from raw or cleaned datasets  

---

## 🖥️ Example Run
```
Data Loaded
Cleaning Data...
Data Cleaned

Total Revenue: 440000

Sales by Product:
Laptop     160000
Mobile     250000
Tablet      30000
Name: total, dtype: int64

Sales by City:
Islamabad    160000
Karachi       30000
Lahore       250000
Name: total, dtype: int64

Most Sold Product: Laptop

Top Customer:
name   product  price  quantity    city   total
4 Ayesha   Mobile   50000        3   Lahore  150000

Cheapest Product:
name   product  price  quantity    city   total
2   Sara   Tablet   30000        1   Karachi  30000

SMART INSIGHTS:
Best Revenue City: Lahore
Best Selling Product: Mobile
```

---

## ⚙️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Azizulhaq-professional/Aziz.git
2. Open 13_Advanced_Sales_Dashboard_System.ipynb in Google Colab or Jupyter Notebook.
3. Upload your dataset (sales.csv).
4. Run cells sequentially from top to bottom.
5. Observe how the system loads, cleans, analyzes, visualizes, and generates smart insights automatically.

🚀 I, Aziz Ul Haq, am actively learning, building, and sharing — turning my skills in Python, AI, Data Science, and Cybersecurity into a professional portfolio.
