# 📊 Sales Data Analysis System – End-to-End Workflow

This notebook demonstrates how to build a **complete data analysis system** using Pandas.  
It integrates **loading, cleaning, analyzing, and filtering** into one structured workflow, simulating a real data analyst project.

---

## 📘 Concepts Covered
- **Data Loading:** Import CSV files into Pandas DataFrames  
- **Data Cleaning:** Handle missing values, remove duplicates, strip text, drop empty names  
- **Feature Engineering:** Create calculated columns (`total = price * quantity`)  
- **Data Summary:** Preview dataset, columns, and info  
- **Analysis:**  
  - Total revenue  
  - Sales by product  
  - Sales by city  
  - Most sold products  
  - Highest sale record  
- **Filtering:**  
  - High price products (> 60000)  
  - City-specific sales (Islamabad)  

---

## 🧩 Project Workflow

### Features
- Modular functions for each step (`load_data`, `clean_data`, `show_summary`, `analyze_data`, `filter_data`)  
- End-to-end execution via `main()` function  
- Clear separation of responsibilities for readability and reusability  
- Outputs structured insights directly from raw or cleaned datasets  

---

## 🖥️ Example Run
```
Data Loaded Successfully
Cleaning Data...

Total Revenue: 440000

Sales by Product:
Ahmed     100000
Ali        80000
Ayesha    150000
Sara       30000
Usman      80000
Name: total, dtype: int64

Sales by City:
Islamabad    160000
Karachi       30000
Lahore       250000
Name: total, dtype: int64

Highest Sale Record:
name  product  price  quantity    city   total
4 Ayesha  Mobile  50000         3  Lahore  150000
```

---

## ⚙️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Azizulhaq-professional/Aziz.git
2. Open 11_Sales_Data_Analysis_System.ipynb in Google Colab or Jupyter Notebook.
3. Upload your dataset (sales.csv).
4. Run cells sequentially from top to bottom.
5. Observe how the system loads, cleans, analyzes, and filters data automatically.

🚀 I, Aziz Ul Haq, am actively learning, building, and sharing — turning my skills in Python, AI, Data Science, and Cybersecurity into a professional portfolio.
