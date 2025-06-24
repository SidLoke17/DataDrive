import numpy as np
import joblib
import os

# Paths to model and scaler files
MODEL_FILE_PATH = '../backend/models/fuel_economy_model.pkl'
SCALER_FILE_PATH = '../backend/models/scaler.pkl'

# Load the model and scaler
def load_model_and_scaler():
    try:
        model = joblib.load(MODEL_FILE_PATH)
        scaler = joblib.load(SCALER_FILE_PATH)
        return model, scaler
    except FileNotFoundError as e:
        raise Exception("Model or Scaler file not found. Please train the model first.")

# Predict fuel efficiency
def predict_fuel_efficiency(input_data):
    # Load the model and scaler
    model, scaler = load_model_and_scaler()

    # Convert to numpy array and reshape
    input_array = np.array(input_data).reshape(1, -1)

    # Scale the input data
    input_scaled = scaler.transform(input_array)

    # Predict using the loaded model
    prediction = model.predict(input_scaled)
    return prediction[0]
