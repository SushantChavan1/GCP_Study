import pandas as pd

# Function to check for missing values
def check_missing_values(df):
    missing = df.isnull().sum()
    return missing[missing > 0]

# Function to check for incorrect data types
def check_data_types(df):
    incorrect_types = {}
    if not pd.api.types.is_integer_dtype(df['CustomerID']):
        incorrect_types['CustomerID'] = 'Should be Integer'
    if not pd.api.types.is_float_dtype(df['Price_USD']):
        incorrect_types['Price_USD'] = 'Should be Float'
    return incorrect_types

# Function to check for duplicate records
def check_duplicates(df):
    duplicates = df[df.duplicated()]
    return duplicates

# Simple report generation
def generate_report(df):
    report = {}

    # Check for missing values
    missing = check_missing_values(df)
    if not missing.empty:
        report['Missing Values'] = missing

    # Check for incorrect data types
    incorrect_types = check_data_types(df)
    if incorrect_types:
        report['Incorrect Data Types'] = incorrect_types

    # Check for duplicate records
    duplicates = check_duplicates(df)
    if not duplicates.empty:
        report['Duplicates'] = duplicates

    return report

# Sample data
data = {
    'CustomerID': [101, 102, 103, 104, None],
    'Price_USD': [250.5, -300, 450, 500, 600],
    'Product': ['A', 'B', 'C', 'D', 'E']
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Generate report
report = generate_report(df)

# Display the report
for issue, details in report.items():
    print(f"{issue}:")
    print(details)
    print()
