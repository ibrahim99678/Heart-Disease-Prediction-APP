import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from app.schemas import HeartDataInput, PredictionOutput

app = FastAPI(title="Heart Disease Prediction API")

# Load the pre-trained model
MODEL_PATH = os.path.join("model", "heart_model.joblib")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model file not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", 
    "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/info")
def get_info():
    return {
        "model_type": type(model).__name__,
        "features": FEATURES
    }

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: HeartDataInput):
    try:
        # Convert input data to DataFrame
        data_dict = input_data.model_dump()
        input_df = pd.DataFrame([data_dict])
        
        # Make prediction (1 = Disease, 0 = No Disease)
        prediction = model.predict(input_df)[0]
        
        return PredictionOutput(heart_disease=bool(prediction == 1))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))