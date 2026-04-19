# train_model.py
# STEP 1 - Import libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# STEP 2 - Training Data (experience vs salary)
# Example dataset: years of experience and corresponding salaries
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])  # Experience in years
y = np.array([30000, 35000, 40000, 45000, 50000, 60000, 65000, 70000, 75000, 80000])  # Salaries

# STEP 3 - Create and train model
model = LinearRegression()
model.fit(X, y)

# STEP 4 - Save model to file
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully as model.pkl")