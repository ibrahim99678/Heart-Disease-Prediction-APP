import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
df = pd.read_csv("D:\\AI-Engineering\\AL ML Engineering\\Module 17 Assignment\\heart.csv")

# Separate the features and target
X = df.drop(columns=["target"])
y = df["target"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Create the model directory and save the trained model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/heart_model.joblib")
print("Model saved to model/heart_model.joblib")