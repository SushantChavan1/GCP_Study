from google.cloud import bigquery
import pandas as pd
from pandas_gbq import to_gbq

# Function to authenticate using service account key
def authenticate_service_account(service_account_path: str) -> bigquery.Client:
    """
    Authenticate using the service account key JSON file and return a BigQuery client.
    """
    try:
        client = bigquery.Client.from_service_account_json(service_account_path)
        print("Authentication successful.")
        return client
    except Exception as e:
        print(f"Error authenticating with service account: {e}")
        raise

# Function to read data from BigQuery table
def read_data_from_bq(client: bigquery.Client, query: str) -> pd.DataFrame:
    """
    Run the given query on BigQuery and return the result as a Pandas DataFrame.
    """
    try:
        print("Reading data from BigQuery...")
        df = client.query(query).to_dataframe()
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error reading data from BigQuery: {e}")
        raise

# Function to process data and summarize sales by customer_id
def summarize_sales_by_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize the sales amount by customer_id and return the summary DataFrame.
    """
    try:
        print("Summarizing sales by customer_id...")
        summary_df = df.groupby('customer_id', as_index=False)['sale_amount'].sum()
        print("Summary created successfully.")
        return summary_df
    except Exception as e:
        print(f"Error summarizing sales by customer_id: {e}")
        raise

# Function to write the summary DataFrame to a new BigQuery table
def write_summary_to_bq(client: bigquery.Client, summary_df: pd.DataFrame, table_id: str) -> None:
    """
    Write the summary DataFrame to a new BigQuery table.
    """
    try:
        print(f"Writing summary data to BigQuery table: {table_id}...")
        
        # Create a BigQuery table reference
        table_ref = client.dataset('demosql').table(table_id)
        print("Table reference value", table_ref)
        #Write the summary DataFrame to a BigQuery table using pandas_gbq.to_gbq(). 

         
        to_gbq(summary_df, destination_table=table_id, project_id=client.project, if_exists='replace')
        
        print(f"Summary written successfully to {table_id}.")
    except Exception as e:
        print(f"Error writing summary to BigQuery: {e}")
        raise

# Main function to coordinate the workflow
def main(service_account_path: str, query: str, table_id: str):
    """
    Main function to authenticate, read data, process the results, and write the summary to BigQuery.
    """
    try:
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
        
        # Write the summary DataFrame to a new BigQuery table
        write_summary_to_bq(client, summary_df, table_id)
        
    except Exception as e:
        print(f"An error occurred in the main process: {e}")

# Define the SQL query, service account path, and table ID for the summary table
query = """
    SELECT order_id, customer_id, product_id, product_name, sale_amount, sale_date
    FROM `root-wharf-441908-f0.demosql.sales_data`
"""
service_account_path = "bigqueryjsonfile.json"
table_id = 'root-wharf-441908-f0.demosql.sales_summary'  # Specify the destination table name

# Run the main function
if __name__ == "__main__":
    main(service_account_path, query, table_id)
