import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# Adjust BASE_DIR to correctly reference the backend directory
BASE_DIR = Path(__file__).resolve().parent  # Reference to backend folder

# Construct paths using BASE_DIR
DATA_FILE_PATH = BASE_DIR / 'data' / 'all_toyota_data.xlsx'
MODEL_FILE_PATH = BASE_DIR / 'models' / 'fuel_economy_model.pkl'
SCALER_FILE_PATH = BASE_DIR / 'models' / 'scaler.pkl'
VISUALIZATIONS_DIR = BASE_DIR / 'visualizations'

# Make sure the visualizations directory exists
VISUALIZATIONS_DIR.mkdir(exist_ok=True)  # Creates the directory if it doesn't exist

def calculate_and_plot_shap_summary():
    # Load model and data
    model = joblib.load(MODEL_FILE_PATH)
    scaler = joblib.load(SCALER_FILE_PATH)
    df = pd.read_excel(DATA_FILE_PATH, engine='openpyxl')

    # Prepare data
    features = ['Eng Displ', '# Cyl', 'City FE (Guide) - Conventional Fuel', 'Hwy FE (Guide) - Conventional Fuel', 'Comb CO2 Rounded Adjusted (as shown on FE Label)']
    X = df[features].dropna()
    X_scaled = scaler.transform(X)

    # Create SHAP explainer and compute SHAP values
    explainer = shap.Explainer(model, X_scaled)
    shap_values = explainer(X_scaled)

    # Plot and save SHAP summary plot
    plt.figure()
    shap.summary_plot(shap_values.values, X, feature_names=features, show=False)
    shap_summary_path = VISUALIZATIONS_DIR / 'shap_summary_plot.png'
    plt.savefig(shap_summary_path)  # Save the summary plot

    print(f"SHAP summary plot saved to: {shap_summary_path}")

    return shap_values  # Optionally return SHAP values if needed

# Example Usage
if __name__ == '__main__':
    calculate_and_plot_shap_summary()
