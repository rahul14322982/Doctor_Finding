from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS   # ✅ ADDED

app = Flask(__name__)
CORS(app)                     # ✅ ADDED

# Load trained model
model = joblib.load("doctor_model.pkl")

# Load dataset (for filtering doctors)
data = pd.read_csv("doctor_Finding.csv.csv")


@app.route("/")
def home():
    return "Doctor Recommendation API is running"


@app.route("/predict", methods=["POST"])
def predict_doctor():
    try:
        # Get JSON data from request
        input_data = request.get_json()

        symptoms = input_data.get("symptoms")
        address = input_data.get("address")

        # Convert input to DataFrame
        user_input = pd.DataFrame({
            "symptoms": [symptoms],
            "address": [address]
        })

        # Predict specialization
        predicted_specialization = model.predict(user_input)[0]

        # Filter doctors based on specialization
        filtered_doctors = data[
            data["specialization"].str.contains(
                predicted_specialization, case=False, na=False
            )
        ]

        # Select required columns
        output_df = filtered_doctors[
            ["doctor_name", "opening_time", "closing_time", "phone_number"]
        ]

        # Convert to JSON
        output = output_df.to_dict(orient="records")

        return jsonify({
            "predicted_specialization": predicted_specialization,
            "doctors": output
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1000))
    app.run(host="0.0.0.0", port=port)
