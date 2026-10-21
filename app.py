from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

report_history = []

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    bp = int(data['bp'])
    sugar = int(data['sugar'])
    oxygen = int(data['oxygen'])
    symptoms = data['symptoms']

    prediction = "Normal"
    risk = "Low"
    recommendation = "Maintain healthy lifestyle"

    if bp > 140:
        prediction = "Hypertension Risk"
        risk = "High"
        recommendation = "Consult doctor and monitor BP regularly"

    elif sugar > 180:
        prediction = "Diabetes Risk"
        risk = "High"
        recommendation = "Reduce sugar intake and consult doctor"

    elif oxygen < 92:
        prediction = "Low Oxygen Risk"
        risk = "Critical"
        recommendation = "Seek immediate medical attention"

    elif "fever" in symptoms.lower():
        prediction = "Possible Infection"
        risk = "Medium"
        recommendation = "Take rest and monitor symptoms"

    report = {
        "bp": bp,
        "sugar": sugar,
        "oxygen": oxygen,
        "symptoms": symptoms,
        "prediction": prediction,
        "risk": risk,
        "recommendation": recommendation,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    report_history.append(report)

    return jsonify(report)

@app.route('/history', methods=['GET'])
def history():
    return jsonify(report_history)

@app.route("/")
def home():
    return "VitalScan AI Backend Running Successfully"
if __name__ == "__main__":
    import os

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))