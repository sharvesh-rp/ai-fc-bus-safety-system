from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("../backend/fc_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    
    data = request.json
    
    features = np.array([[
        data["brake_condition"],
        data["tire_condition"],
        data["engine_health"],
        data["leakage"],
        data["rust_level"]
    ]])
    
    prediction = model.predict(features)[0]
    
    if prediction == 1:
        result = "PASS"
    else:
        result = "REJECT"
    
    return jsonify({"FC_Status": result})

if __name__ == "__main__":
    app.run(debug=True)
