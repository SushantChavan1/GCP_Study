from google.cloud import bigquery
import pandas as pd

# Function to authenticate using service account key
def authenticate_service_account(service_account_path: str) -> bigquery.Client:
    """
    Authenticate using the service account key JSON file and return a BigQuery client.
    """
    return bigquery.Client.from_service_account_json(service_account_path)

# Function to read data from BigQuery table
def read_data_from_bq(client: bigquery.Client, query: str) -> pd.DataFrame:
    """
    Run the given query on BigQuery and return the result as a Pandas DataFrame.
    """
    return client.query(query).to_dataframe()

# Function to process data and summarize sales by customer_id
def summarize_sales_by_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize the sales amount by customer_id and return the summary DataFrame.
    """
    summary_df = df.groupby('customer_id', as_index=False)['sale_amount'].sum()
    return summary_df

# Main function to coordinate the workflow
def main(service_account_path: str, query: str):
    """
    Main function to authenticate, read data, and process the results.
    """
    # Authenticate and get the BigQuery client
    client = authenticate_service_account(service_account_path)
    
    # Read data from BigQuery
    df = read_data_from_bq(client, query)
    
    # Print the original data
    print("Original Data:")
    print(df)
    
    # Summarize the sales data
    summary_df = summarize_sales_by_customer(df)
    
    # Print the summary results
    print("\nSummary of Sales by Customer ID:")
    print(summary_df)

# Define the SQL query and service account path
query = """
    SELECT order_id, customer_id, product_id, product_name, sale_amount, sale_date
    FROM `root-wharf-441908-f0.demosql.sales_data`
"""
service_account_path = "bigqueryjsonfile.json"

# Run the main function
if __name__ == "__main__":
    main(service_account_path, query)
