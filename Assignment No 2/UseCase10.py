import pandas as pd

# Step 1: Load data from JSON
def load_json_data(json_file):
    # Read JSON data into a pandas DataFrame
    df = pd.read_json(json_file)
    return df

# Step 2: Convert DataFrame to CSV with compression
def convert_to_csv(df, csv_file):
    # Save the DataFrame as a CSV file with GZIP compression
    df.to_csv(csv_file, index=False, compression='gzip')
    print(f"Data saved as compressed CSV file: {csv_file}")

# Step 3: Load data from CSV
def load_csv_data(csv_file):
    # Read CSV data into a pandas DataFrame
    df = pd.read_csv(csv_file)
    return df

# Example Usage:
json_file = 'C:\\Users\\Admin\\Desktop\\Python\\GCP_Study\\Assignment No 2\\data.json'  # Replace with your JSON file path
csv_file = 'C:\\Users\\Admin\\Desktop\\Python\\GCP_Study\\Assignment No 2\\data_compressed.csv.gz'  # Path to save the CSV file with compression

# Load data from JSON and convert it to CSV
df_json = load_json_data(json_file)
convert_to_csv(df_json, csv_file)

# Load the CSV file (to verify)
df_csv = load_csv_data(csv_file)
print(df_csv.head())  # Print first few rows
