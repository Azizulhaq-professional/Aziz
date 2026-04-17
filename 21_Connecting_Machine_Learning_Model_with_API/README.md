## Connecting Machine Learning Model with API ⚡
### 📌 Project Overview
This project demonstrates how to connect a Machine Learning model with a Flask API to build a real-world AI system.

The workflow:
1. Train a Salary Prediction ML model.
2. Save the trained model (model.pkl) using joblib.
3. Build a Flask API (app.py) to serve predictions.
4. Test the API using Postman and Python requests.
5. Document the process with screenshots for clarity.
### 🛠️ Tech Stack
- Python (Flask, scikit-learn, pandas, joblib)
- Flask API for serving predictions
- Postman / Python requests for testing
- Jupyter Notebook for step-by-step workflow
### 📂 Repository Structure
```
21_Connecting_Machine_Learning_Model_with_API/
│── app.py              # Flask API
│── train_model.py      # Train and save ML model
│── model.pkl           # Serialized trained model
│── 21_Connecting_Machine_Learning_Model_with_API.ipynb  # Notebook workflow
│── screenshots/        # Step-by-step project screenshots
│── README.md           # Documentation
```
### ## 📸 Screenshots
Recruiters and collaborators can view the step-by-step screenshots here:  
👉 [Screenshots Folder](https://github.com/Azizulhaq-professional/Aziz/tree/main/21_Connecting_Machine_Learning_Model_with_API/screenshots)

Key screenshots include:
- [Run Flask API](https://github.com/Azizulhaq-professional/Aziz/blob/main/21_Connecting_Machine_Learning_Model_with_API/screenshots/app_py.JPG)
- [Browser Message](https://github.com/Azizulhaq-professional/Aziz/blob/main/21_Connecting_Machine_Learning_Model_with_API/screenshots/broswer_message.JPG)
- [Serialized Model File](https://github.com/Azizulhaq-professional/Aziz/blob/main/21_Connecting_Machine_Learning_Model_with_API/screenshots/model_pkl.JPG)
- [Training Script](https://github.com/Azizulhaq-professional/Aziz/blob/main/21_Connecting_Machine_Learning_Model_with_API/screenshots/train_model_py.JPG)

### ⚙️ How It Works
1. Train the Model  
Run train_model.py to train a simple linear regression model and save it as model.pkl.
2, Start Flask API  
Run app.py to start the API server at http://127.0.0.1:5000/.
3. Test Predictions
- Using Postman (send JSON to /predict)
- Using Python requests
- Browser message confirms API is running
4. Output  
The API returns predicted salary based on years of experience.
### 🚀 Getting Started
Clone the repository and install dependencies:
```
git clone https://github.com/Azizulhaq-professional/Aziz.git
cd Aziz/21_Connecting_Machine_Learning_Model_with_API
pip install -r requirements.txt
```
Run the workflow:
```
python train_model.py
python app.py
```
Test with Postman:
```
POST http://127.0.0.1:5000/predict
{
  "experience": 3
}
```
Expected output:
{
  "experience": 3,
  "predicted_salary": 40000
}```

### 🎯 Professional Journey
I am **Aziz**, a passionate learner and developer focused on **Machine Learning, Data Science, and API Development**.  
My journey includes building end-to-end projects that integrate ML models with real-world applications, documenting workflows with clarity, and sharing reproducible code for recruiters and collaborators.  
Through these projects, I aim to demonstrate not only technical skills but also the ability to communicate solutions professionally and effectively.
