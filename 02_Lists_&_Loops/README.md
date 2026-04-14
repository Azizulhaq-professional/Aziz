# Python Lists & Loops – Student Marks Analyzer

A hands-on Python notebook covering core programming concepts with a real-world mini project.

## 📌 Concepts Covered

| Concept | Description |
|---------|-------------|
| Lists | Store multiple values in one variable |
| `for` loop | Iterate through sequences |
| `while` loop | Repeat until condition changes |
| Do-while (Python style) | Simulate with `while True` + `break` |
| `if`/`elif`/`else` | Conditional decision making |
| Nested `if` | Decision inside a decision |
| Nested loops | Loop inside a loop (matrices/patterns) |

## 🎓 Mini Project: Student Marks Analyzer

```python
marks = [55, 70, 90, 40, 85]

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

Output: Average: 68.0, Passed: 4, Failed: 1

 Run the Notebook
Open the .ipynb file in Google Colab or Jupyter Notebook

Run cells sequentially from top to bottom

Try modifying the marks list with your own data

🌍 Real-World Applications
Data science – processing datasets

Cybersecurity – analyzing log files

AI – iterating over training data

Web apps – handling user records

Loan approval systems – nested condition checks

📁 Files
02_Lists_&_Loops.ipynb – Complete Jupyter notebook with all examples

README.md – This file

Part of my Python learning journey – exploring fundamentals with practical examples.
