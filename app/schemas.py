# for input data validation create a schema using pydantic

from pydantic import BaseModel, Field

class HeartDataInput(BaseModel):
    age: int = Field(..., example=52)
    sex: int = Field(..., example=1, description="1 = male; 0 = female")
    cp: int = Field(..., example=0, description="Chest pain type (0-3)")
    trestbps: int = Field(..., example=125, description="Resting blood pressure")
    chol: int = Field(..., example=212, description="Serum cholestoral in mg/dl")
    fbs: int = Field(..., example=0, description="Fasting blood sugar > 120 mg/dl")
    restecg: int = Field(..., example=1, description="Resting ECG results (0-2)")
    thalach: int = Field(..., example=168, description="Maximum heart rate achieved")
    exang: int = Field(..., example=0, description="Exercise induced angina (1/0)")
    oldpeak: float = Field(..., example=1.0, description="ST depression")
    slope: int = Field(..., example=2, description="Slope of the peak exercise ST")
    ca: int = Field(..., example=2, description="Number of major vessels (0-3)")
    thal: int = Field(..., example=3, description="1 = normal; 2 = fixed defect; 3 = reversable defect")

class PredictionOutput(BaseModel):
    heart_disease: bool