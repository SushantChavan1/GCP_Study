#In this particular I am going to work with the dataset of student 
#I will be creating a table and inserting records into the table


from google.cloud import bigquery
import pandas as pd

def get_connection_to_bigquery() -> bigquery.Client:
    try:
        # Set the path to your service account key JSON file
        service_account_path = "C:\\Users\\Admin\\Desktop\\Python\\GCP_Study\\BigQuery With Python\\BigqueryJsonKey.json"
        client = bigquery.Client.from_service_account_json(service_account_path)
        print("Connection is get successfully.....")
        #returning the client object
        return client
    except Exception as e:
        print("Connection is get failed.....")
        print(e)
        raise

#Function insert the records into the table
def insert_records_into_table(client, query):
    try:
        query_job = client.query(query)
        print("Records inserted successfully")
    except Exception as e:
        print("Records insertion failed")
        print(e)
        raise
#getting the records from the table
def get_records_from_table(client, query) -> None:
    try:
        query_job = client.query(query)
        results = query_job.result()
        data_frame = results.to_dataframe()
        print("This are the records from the table")
        print(data_frame)
    except Exception as e:
        print("Records fetching failed")
        print(e)
        raise


#inserting records into the table Student

if __name__ == "__main__":
    client = get_connection_to_bigquery()
    query = """
    INSERT INTO `model-calling-452106-v1.StudentDataSet.Student` (StudentID, StudentName, StudentAge, StudentMarks)
    VALUES (1, 'John', 21, 32.00),
           (2, 'Alice', 21, 35.00),
           (3, 'Bob', 21, 38.00),
           (4, 'Charlie', 21, 40.00),
           (5, 'Sushant', 21, 80.00),
           (6,'Shivtej', 21, 90.00),
           (7, 'Rohan', 21, 95.00),
           (8, 'Vinayak', 21, 92.00),
           (9, 'Sahaji', 21, 85.00),
            (10, 'Vaibhav', 21, 88.00) """

    #insert_records_into_table(client, query)
    query = """
    SELECT * FROM `model-calling-452106-v1.StudentDataSet.Student`
    """
    #get_records_from_table(client, query)






