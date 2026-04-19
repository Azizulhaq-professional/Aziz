# ==========================================
# Student Pass/Fail Prediction API
# app.py
# ==========================================

from flask import Flask, request, jsonify
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)

# ------------------------------------------
# Load trained model
# ------------------------------------------
try:
    model = pickle.load(open("model.pkl", "rb"))
    print(" Model loaded successfully")
except:
    print(" ERROR: model.pkl not found")
    model = None


# ------------------------------------------
# Home Route (Browser Test)
# ------------------------------------------
@app.route("/")
def home():
    return """
    <h1> ML Flask API is Running</h1>
    <p>Use Postman to test prediction</p>
    <p><b>POST URL:</b> http://127.0.0.1:5000/predict</p>
    """


# ------------------------------------------
# Prediction Route (Postman Test)
# ------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Check if marks exist
        if "marks" not in data:
            return jsonify({"error": "Please send marks in JSON"}), 400

        marks = float(data["marks"])

        # Model prediction
        prediction = model.predict([[marks]])[0]

        result = "Pass" if prediction == 1 else "Fail"

        return jsonify({
            "marks": marks,
            "prediction": result
        })

    except Exception as e:
        return jsonify({"error": str(e)})


# ------------------------------------------
# Run Flask App
# ------------------------------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    