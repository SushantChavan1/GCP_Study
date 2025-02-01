import apache_beam as beam
import pandas as pd


# Function to parse CSV lines into lists with ',' as the delimiter
def parse_csv(line):
    return line.split(',')


# Function to convert elements into a Pandas DataFrame
def convert_to_pandas(elements):
    return pd.DataFrame(elements)


# Function to print Pandas DataFrame (for debugging purposes)
def print_pandas_data(data):
    print(data)


# Create a pipeline object
pipeline = beam.Pipeline()

# Read CSV file and process it
data = (
    pipeline
    | 'Read from CSV' >> beam.io.ReadFromText(
        'C:\\Users\\Admin\\Desktop\\Python\\GCP_Study\\Data Flow Pratice\\sample1000.csv')
    | 'Parse CSV' >> beam.Map(parse_csv)  # Parse each line into a list
)

# Collect data into a list for Pandas DataFrame conversion
pandas_data = data | 'Collect data' >> beam.ParDo(convert_to_pandas)

# Print the Pandas DataFrame
pandas_data | 'Print Pandas Data' >> beam.Map(print_pandas_data)

# Run the pipeline
pipeline.run()
