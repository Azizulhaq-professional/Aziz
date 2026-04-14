# 🐍 Python Lists & Loops – Student Marks Analyzer

A hands‑on Python notebook covering core programming concepts with a real‑world mini project.

---

## 📘 Concepts Covered

| Concept       | Description                                |
|---------------|--------------------------------------------|
| Lists         | Store multiple values in one variable       |
| For loop      | Iterate through sequences                   |
| While loop    | Repeat until condition changes              |
| Do‑while      | Simulate with `while True` + `break`        |
| If / Elif / Else | Conditional decision making             |
| Nested if     | Decision inside a decision                  |
| Nested loops  | Loop inside a loop (matrices/patterns)      |

---

## 🎯 Mini Project: Student Marks Analyzer

```python
marks = [95, 70, 40, 85]
total = 0
passed = 0
failed = 0

for mark in marks:
    total += mark
    if mark >= 50:
        passed += 1
    else:
        failed += 1

average = total / len(marks)

print(f"Average: {average}, Passed: {passed}, Failed: {failed}")

Expected Output:
Average: 72.5, Passed: 3, Failed: 1

⚙️ How to Run
1. Clone this repository.

2. Open 02_Lists_&_Loops.ipynb in Google Colab or Jupyter Notebook.

3. Run cells sequentially from top to bottom.

4.Try modifying the marks list with your own data to test different scenarios.

🌍 Applications
- Data Science – processing datasets

- Cybersecurity – analyzing log files

- AI/ML – iterating over training data

- Web Apps – handling user records

- Loan Approval Systems – nested condition checks

📌 Project Files
- 02_Lists_&_Loops.ipynb – Complete Jupyter notebook with all examples

- README.md – This documentation file
