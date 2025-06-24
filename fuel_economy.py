import pandas as pd

# Load the Excel data
data = pd.DataFrame()  # Placeholder, to load data correctly in other contexts

def generate_insights(data):
    avg_fuel = data['fuel_consumption'].mean()
    if avg_fuel > 15:
        print("Recommended maintenance")
