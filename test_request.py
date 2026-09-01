import requests

url = 'http://127.0.0.1:5000/predict'

# ✅ Sample test data (use the same features your model was trained on)
data = {
    "Age": 35,
    "Income": 50000,
    "Loan_Amount": 15000,
    "Loan_Term_Months": 36,
    "Credit_Score": 720,
    "Past_Defaults": 0
}

response = requests.post(url, json=data)

print("Prediction:", response.json())
