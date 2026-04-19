# train_model.py
# STEP 1 — Import libraries
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle

# STEP 2 — Training Data (marks vs pass/fail)
X = np.array([[30], [40], [50], [60], [70]])
y = np.array([0, 0, 0, 1, 1])  # 0 = Fail, 1 = Pass

# STEP 3 — Create model
model = LogisticRegression()

# STEP 4 — Train model
model.fit(X, y)

# STEP 5 — Save model to file
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully!")
