#Here I am going to connect with the database and executing the queries
#Transforming the data like the appling the grade and status to the table adding new columns

#importing the packages
from google.cloud import bigquery   
import pandas as pd

#Function to authenticate the service account

def get_connection_to_bigquery() -> bigquery.Client:
    try:
        service_account_path = "C:\\Users\\Admin\\Desktop\\Python\\GCP_Study\\BigQuery With Python\\BigqueryJsonKey.json"
        client = bigquery.Client.from_service_account_json(service_account_path)
        print("Connection is get successfully.....")

        return client_bq
    
    except Exception as e:
        print("Connection is failed........")
        print(e)
        raise


#function that will read data from table and convert into the dataframe

def get_records_from_table(client, query) -> pd.DataFrame:
    try:
        query_job = client.query(query).to_dataframe()
        return query_job
    except Exception as e:
        print("Records featching get Failed........")
        print(e)
        raise

#Function to transform the data

def transform_data(data_frame) -> pd.DataFrame:
    try:
        #adding the status column to the dataframe according to the marks

        data_frame['Status'] = data_frame['StudentMarks'].apply(lambda x: 'Pass' if x >= 35 else 'Fail')

        #adding the grade column to the dataframe according to the marks

        data_frame['Grade'] = data_frame['StudentMarks'].apply(lambda x: 'A' if x >= 80 else ('B' if x >= 60 else ('C' if x >= 40 else 'D')))

        return data_frame
    except Exception as e:
        print("Transformation is failed.........")
        print(e)
        raise

#Function to insert the records into the table

def insert_records_into_table(client, data_frame, table_id, project_id) -> None:
    try:
        data_frame.to_gbq(destination_table=table_id, project_id=project_id, if_exists='replace')
        print("Records inserted successfully")
        
    except Exception as e:
        print("Records insertion failed")
        print(e)
        raise

#Removing the duplicate records from the table

def remove_duplicate_records(data_frame) -> pd.DataFrame:
    try:
        data_frame.drop_duplicates(inplace=True)
        return data_frame
    except Exception as e:
        print(f"Removing the duplicate records get failed........{e}")
        raise

if __name__ == "__main__":
    client = get_connection_to_bigquery()
    table_id = "model-calling-452106-v1.StudentDataSet.Student"
    priject_id = "model-calling-452106-v1"
    query = """
    SELECT * FROM `model-calling-452106-v1.StudentDataSet.Student`
    """
    data_frame = get_records_from_table(client, query)
    print("Original Data")
    print(data_frame)
    data_frame = transform_data(data_frame)
    print("Transformed Data")
    print(data_frame)
    data_frame = remove_duplicate_records(data_frame)
    insert_records_into_table(client, data_frame, table_id, priject_id)
