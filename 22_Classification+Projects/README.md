## 🛒 Customer Purchase Prediction System
### 📌 Project Overview
This project demonstrates a classification system that predicts whether a customer will purchase a product (1) or not (0) based on features such as Age and Salary.

It covers the full machine learning workflow:
- Data preparation and feature scaling
- Training models (Logistic Regression & Decision Tree)
- Evaluating performance with accuracy, precision, recall, F1-score
- Visualizing results with Confusion Matrix and ROC Curve
### 🛠️ Tech Stack
- Python (NumPy, Pandas, Matplotlib, scikit-learn)
- Machine Learning Models: Logistic Regression, Decision Tree
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score, ROC Curve, AUC
### 📂 Repository Structure
```
Customer_Purchase_Prediction_System/
│── 22_Customer_Purchase_Prediction_System.ipynb   # Jupyter Notebook workflow
│── README.md                                      # Documentation
```
### ⚙️ How It Works
1. Dataset Creation  
A small dataset is created manually with features: Age, Salary, and target Purchased (0/1).
2. Train-Test Split  
Data is split into training (70%) and testing (30%).
3. Feature Scaling  
StandardScaler is applied to normalize values for better model performance.
4. Model Training
- Logistic Regression
- Decision Tree Classifier
5. Evaluation  
Models are evaluated using accuracy, precision, recall, F1-score, confusion matrix, and ROC curve.
6. Results
- Logistic Regression achieved 100% accuracy on test data.
- Decision Tree achieved ~66% accuracy.
- ROC Curve shows perfect classification with AUC = 1.0.
### 🚀 Getting Started
Clone the repository and install dependencies:
```
git clone https://github.com/Azizulhaq-professional/Aziz.git
cd Aziz/22_Customer_Purchase_Prediction_System
pip install -r requirements.txt
```
Run the notebook:
```
jupyter notebook 22_Customer_Purchase_Prediction_System.ipynb
```
### 🎯 Professional Journey
I am Aziz, a developer passionate about Machine Learning, Data Science, and API Development.
This project reflects my ability to design end-to-end ML workflows, evaluate models with industry-standard metrics, and document projects professionally for recruiters and collaborators.
