## 📌 Flask POST Request API
- This project demonstrates how to build and test a simple Flask API that accepts POST requests with JSON data. It covers:
- Creating a Flask app (app.py)
- Sending data via a client script (test_client.py)
- Testing the API using Postman
- Documenting results with screenshots
## 🚀 Features
- Accepts JSON input (name, age)
- Returns a personalized response
- Tested with both Python client and Postman
- Beginner-friendly step-by-step workflow
## 📂 Project Structure
```
19_Post_Request/
│── app.py
│── test_client.py
│── 19_POST_Request.ipynb
│── README.md
│── screenshots/
    ├── Postman.JPG
    ├── Postman1.JPG
    ├── Postmanworkspace.JPG
    ├── Sales_Api_Welcome.JPG
    ├── app_py.JPG
    ├── pip_install_flask.JPG
    ├── python_app_py.JPG
```
## ⚙️ Setup Instructions
1. Install Flask:
```
pip install flask
```
2. Run the server:
```
python app.py
```
Server runs at: http://127.0.0.1:5000/

3. Install requests (for client testing):d
```
pip install requests
```
4.Run the client:
```
python test_client.py
```
## 🧪 Testing with Postman
- Method: POST
- URL: http://127.0.0.1:5000/submit
- Body (JSON):
```
{
  "name": "Aziz",
  "age": 23
}
```
Response:
```
{
  "message": "Hello Aziz, you are 23 years old"
}
```
## 📸 Screenshots

## 📖 Learning Outcomes
- Difference between GET and POST
- How to send JSON data to an API
- Using Flask to build APIs
- Testing APIs with Postman and Python requests
