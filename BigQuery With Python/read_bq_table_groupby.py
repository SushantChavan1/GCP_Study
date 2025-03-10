from google.cloud import bigquery
import pandas as pd

# Set the path to your service account key JSON file
service_account_path = "bigqueryjsonfile.json"

# Authenticate with the service account
client = bigquery.Client.from_service_account_json(service_account_path)

# Define the SQL query to select data from the table
query = """
    SELECT order_id, customer_id, product_id, product_name, sale_amount, sale_date
    FROM `root-wharf-441908-f0.demosql.sales_data`
"""

# Run the query and load the result into a Pandas DataFrame
df = client.query(query).to_dataframe()

# Print the original data
print("Original Data:")
print(df)

# Summarize the sales amount by customer_id
summary_df = df.groupby('customer_id', as_index=False)['sale_amount'].sum()

# Print the summary results
print("\nSummary of Sales by Customer ID:")
print(summary_df)