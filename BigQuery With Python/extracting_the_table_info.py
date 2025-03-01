#In this program I am going to extract the information of the table like the schema, table_id, project_id, dataset_id
#I will be using the BigQuery API to extract the information of the table

#Importing the packages
from google.cloud import bigquery


#Function to authenticate the service account

def get_connection_to_bigquery() -> bigquery.Client:
    try:
        service_account_path = "C:\\Users\\Admin\\Desktop\\Python\\GCP_Study\\BigQuery With Python\\BigqueryJsonKey.json"

        client = bigquery.Client.from_service_account_json(service_account_path)
        print("Connection is get successfully.....")
        #returning the client object
        return client
    
    except Exception as e:
        print("Connection is failed........")
        print(e)
        raise

#Function to extract the information of the table

def extract_table_info(client, dataset_id, table_id) -> None:
    try:
        #Extracting the table information
        table = client.get_table(f"{dataset_id}.{table_id}")
        print("Table Information")
        print(f"Table ID: {table.table_id}")
        print(f"Project ID: {table.project}")
        print(f"Dataset ID: {table.dataset_id}")
        print("Schema")
        for schema in table.schema:
            print(f"Name: {schema.name}, Type: {schema.field_type}, Mode: {schema.mode}")
    except Exception as e:
        print("Table information extraction failed........")
        print(e)
        raise

#Extracting the information of the table

if __name__ == "__main__":
    client = get_connection_to_bigquery()
    dataset_id = "model-calling-452106-v1.StudentDataSet"
    table_id = "Student"
    extract_table_info(client, dataset_id, table_id)

