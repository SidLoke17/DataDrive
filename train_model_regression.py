import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from pathlib import Path

# Paths to important files
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_FILE_PATH = BASE_DIR / 'data' / 'all_toyota_data.xlsx'
MODEL_FILE_PATH = BASE_DIR / 'models' / 'fuel_economy_model.pkl'
SCALER_FILE_PATH = BASE_DIR / 'models' / 'scaler.pkl'

# Preprocess the Data
def preprocess_data(file_path):
    # Load the dataset
    df = pd.read_excel(file_path, engine='openpyxl')

    # Select relevant features and target variable
    features = [
        'Eng Displ',
        '# Cyl',
        'City FE (Guide) - Conventional Fuel',
        'Hwy FE (Guide) - Conventional Fuel',
        'Comb CO2 Rounded Adjusted (as shown on FE Label)'
    ]
    target = 'Comb FE (Guide) - Conventional Fuel'

    # Handle missing values by dropping rows with any missing values
    df_filtered = df[features + [target]].dropna()

    # Split data into features (X) and target (y)
    X = df_filtered[features]
    y = df_filtered[target]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Training Features Shape:", X_train.shape)
    # Normalize the features using StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

# Train and Save the Model
def train_and_save_model():
    # Preprocess the data
    X_train_scaled, X_test_scaled, y_train, y_test, scaler = preprocess_data(DATA_FILE_PATH)

    # Initialize the Linear Regression model
    model = LinearRegression()

    # Train the model on the training data
    model.fit(X_train_scaled, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test_scaled)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Print evaluation metrics
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"R-Squared (R2): {r2}")

    # Save the trained model to a file
    joblib.dump(model, MODEL_FILE_PATH)
    # Save the scaler as well, as it will be required to scale new data for predictions
    joblib.dump(scaler, SCALER_FILE_PATH)

# Train the model if this script is run directly
if __name__ == "__main__":
    train_and_save_model()
