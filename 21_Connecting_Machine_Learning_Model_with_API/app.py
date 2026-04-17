from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model.pkl")


# Home route (to check server is running)
@app.route('/')
def home():
    return "Salary Prediction API is running 🚀"


# Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Check if data exists
        if not data or "experience" not in data:
            return jsonify({"error": "Please provide experience value"}), 400

        # Convert experience to float
        experience = float(data["experience"])

        # Convert into 2D array (model requirement)
        input_data = np.array([[experience]])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Return result as JSON
        return jsonify({
            "experience": experience,
            "predicted_salary": int(prediction)
        })

    except Exception as e:
        return jsonify({"error": str(e)})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)