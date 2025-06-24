import pandas as pd

# File paths
INPUT_CSV = "backend/data/all_toyota_data.csv"  # Replace with the path to your original CSV file
OUTPUT_CSV = "backend/data/cleaned_car_data.csv"  # Output file for the cleaned data

# Columns to extract
COLUMNS_TO_KEEP = [
    "Model Year",
    "Mfr Name",
    "Carline",
    "Eng Displ",
    "# Cyl",
    "City FE (Guide) - Conventional Fuel",
    "Hwy FE (Guide) - Conventional Fuel",
    "Comb FE (Guide) - Conventional Fuel",
    "Annual Fuel1 Cost - Conventional Fuel",
    "Comb CO2 Rounded Adjusted (as shown on FE Label)",
]

# Rename columns for consistency
COLUMN_RENAMES = {
    "Model Year": "model_year",
    "Mfr Name": "manufacturer",
    "Carline": "model",
    "Eng Displ": "engine_displacement",
    "# Cyl": "cylinders",
    "City FE (Guide) - Conventional Fuel": "city_fuel_efficiency",
    "Hwy FE (Guide) - Conventional Fuel": "highway_fuel_efficiency",
    "Comb FE (Guide) - Conventional Fuel": "combined_fuel_efficiency",
    "Annual Fuel1 Cost - Conventional Fuel": "annual_fuel_cost",
    "Comb CO2 Rounded Adjusted (as shown on FE Label)": "co2_emissions",
}

def clean_csv(input_file, output_file):
    # Load the CSV file
    try:
        df = pd.read_csv(input_file)
        print(f"Loaded data with {df.shape[0]} rows and {df.shape[1]} columns.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return

    # Filter only the necessary columns
    df_cleaned = df[COLUMNS_TO_KEEP]

    # Rename columns for readability
    df_cleaned.rename(columns=COLUMN_RENAMES, inplace=True)

    # Remove rows with missing values
    df_cleaned.dropna(inplace=True)

    # Save cleaned data to a new CSV file
    df_cleaned.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}. Total rows: {df_cleaned.shape[0]}")

if __name__ == "__main__":
    clean_csv(INPUT_CSV, OUTPUT_CSV)
