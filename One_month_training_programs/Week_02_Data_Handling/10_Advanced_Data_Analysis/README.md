# 📊 Advanced Data Analysis – Sales Insights

This notebook demonstrates **advanced data analysis techniques using Pandas**, moving beyond cleaning into extracting actionable insights.  
It introduces sorting, advanced filtering, grouping, and answering business questions with structured data.

---

## 📘 Concepts Covered
- **Sorting Data:** By price, total sales, and custom conditions  
- **Advanced Filtering:** Multiple conditions, city-based filters, product-specific queries  
- **Unique Values:** Exploring distinct products and cities  
- **Group Analysis:** Aggregating sales by product and city  
- **Business Insights:** Identifying top customers, most sold products, and highest revenue cities  

---

## 🧩 Mini Project: Advanced Sales Data Analysis

A professional project that demonstrates how to transform messy sales data into **business intelligence insights**.

### Features
- Create and clean dataset (`sales_data.csv`)  
- Handle missing values, duplicates, and empty names  
- Feature engineering: add `total = price * quantity`  
- Sort data by price, total sales, and revenue  
- Extract top and lowest sales records  
- Group analysis for product sales and city averages  
- Answer business questions:
  - Which product sells the most?  
  - Which city generates the highest revenue?  
  - Who is the top customer?  

---

## 🖥️ Example Run
```
Top 3 Highest Sales:
name   price  quantity       city    total
8   Phone  409.375       5.0  Islamabad  2046.875
0  Laptop 1200.000       1.0  Islamabad  1200.000
3 Monitor  409.375       1.0  Islamabad   409.375

City Revenue:
city
Islamabad    3656.25
Karachi       445.00
Lahore        210.00
Name: total, dtype: float64

Top Customer:
name   price  quantity       city    total
8   Phone  409.375       5.0  Islamabad  2046.875
```

---

## ⚙️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Azizulhaq-professional/Aziz.git
2. Open 10_Advanced_Data_Analysis.ipynb in Google Colab or Jupyter Notebook.
3. Run cells sequentially from top to bottom.
4. Observe how the dataset is cleaned, sorted, and analyzed to answer business questions.

🚀 I, Aziz Ul Haq, am actively learning, building, and sharing — turning my skills in Python, AI, Data Science, and Cybersecurity into a professional portfolio.
