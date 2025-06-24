import pandas as pd

# List of input Excel file paths
input_files = [
    'backend/data/2021data.xlsx',
    'backend/data/2022data.xlsx',
    'backend/data/2023data.xlsx',
    'backend/data/2024data.xlsx',
    'backend/data/2025data.xlsx'
]

# Placeholder for all Toyota data
all_toyota_data = []

# Loop through each file and process
for file_path in input_files:
    # Load the current Excel file
    df = pd.read_excel(file_path)
    
    # Filter rows where 'Mfr Name' is 'Toyota'
    toyota_data = df[df['Mfr Name'] == 'Toyota']
    
    # Append the filtered data to the list
    all_toyota_data.append(toyota_data)

# Combine all filtered data into a single DataFrame
combined_toyota_data = pd.concat(all_toyota_data, ignore_index=True)

# Output the combined data to a single Excel file
output_file_path = 'backend/data/all_toyota_data.xlsx'
combined_toyota_data.to_excel(output_file_path, index=False)

print(f"Filtered data from all files saved to {output_file_path}")
