## Connect ML Model with API 🚀
### 📌 Project Overview
This project demonstrates how to connect a Machine Learning model with a Flask API and make it usable by clients, websites, or applications.

The workflow:

1. Train a simple ML model (Logistic Regression).
2. Save the trained model (model.pkl).
3. Build a Flask API (app.py) to serve predictions.
4. Test the API using Python scripts and Postman.
5. Integrate with a frontend (index.html) for user interaction.
### 🛠️ Tech Stack
- Python (Flask, scikit-learn, numpy, pickle)
- Flask API for serving predictions
- Postman / Python requests for testing
- HTML (index.html) for frontend form
### 📂 Repository Structure
```
20_Connect_ML_Model_with_API/
│── app.py              # Flask API
│── train_model.py      # Train and save ML model
│── test_api.py         # Test API with requests
│── model.pkl           # Serialized trained model
│── 20_Connect_ML_Model_with_API.ipynb  # Full notebook workflow
│── templates/
│    └── index.html     # Frontend form
│── screenshots/        # Step-by-step project screenshots
│── README.md           # Documentation
```
⚙️ How It Works
1. Train the Model  
Run train_model.py to train and save the logistic regression model as model.pkl.
2. Start Flask API  
Run app.py to start the API server at http://127.0.0.1:5000/.
3. Test Predictions
- Using test_api.py (Python requests)
- Using Postman (send JSON to /predict)
- Using browser form (index.html)
4. Output  
The API returns prediction results (Pass / Fail) based on student marks.
### 📸 Screenshots
Recruiters and collaborators can view the step-by-step screenshots here:  
👉 [Screenshots Folder](https://github.com/Azizulhaq-professional/Aziz/tree/main/20_Connect_ML_Model_with_API/screenshots)

Key screenshots include:
- [Run Flask API](https://github.com/Azizulhaq-professional/Aziz/blob/main/20_Connect_ML_Model_with_API/screenshots/Run_Flask_API.JPG)
- [Test Using JSON](https://github.com/Azizulhaq-professional/Aziz/blob/main/20_Connect_ML_Model_with_API/screenshots/Test_Using_JSON.JPG)
- [Prediction API Test](https://github.com/Azizulhaq-professional/Aziz/blob/main/20_Connect_ML_Model_with_API/screenshots/Test_the_predict_API.JPG)
- [index.html Form](https://github.com/Azizulhaq-professional/Aziz/blob/main/20_Connect_ML_Model_with_API/screenshots/index_html.JPG)
- [Flask App Code](https://github.com/Azizulhaq-professional/Aziz/blob/main/20_Connect_ML_Model_with_API/screenshots/python_app_py.JPG)
- [Training Script](https://github.com/Azizulhaq-professional/Aziz/blob/main/20_Connect_ML_Model

### 🚀 Getting Started
Clone the repository and install dependencies:
```
git clone https://github.com/Azizulhaq-professional/Aziz.git
cd Aziz/20_Connect_ML_Model_with_API
pip install -r requirements.txt
```
Run the workflow:
```
python train_model.py
python app.py
python test_api.py
```
### 🎯 Key Learning Outcomes
- How to train and serialize ML models with scikit-learn.
- How to build REST APIs with Flask.
- How to integrate ML models into production-ready APIs.
- How to test APIs using Postman and Python scripts.
-How to connect APIs with a frontend (HTML form).
