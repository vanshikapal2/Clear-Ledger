# app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load model
model = joblib.load('C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\Finance & Banking\\loan_risk_model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "ClearLedger API — POST /predict with JSON."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read JSON from request
        data = request.get_json()

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Predict
        pred = model.predict(df)[0]
        risk = 'HIGH' if pred == 1 else 'LOW'

        return jsonify({'risk': risk})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
