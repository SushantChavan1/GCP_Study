#In this eg I am ggoing to read the data from the in memmory data source and then converting into the data frame

import apache_beam as beam
import pandas as pd

# Create a pipeline object
pipeline = beam.Pipeline()

# Create a list of elements

list_elements = ['apple', 'banana', 'cherry', 'mango', 'orange']

# Create a PCollection from a list of elements

elements = pipeline | 'Create PCollection' >> beam.Create(list_elements)

# Apply a ParDo transform to the PCollection

def convert_to_dataframe(element):
    data = pd.DataFrame(element)
    print(data)

elements = elements | 'Convert to DataFrame' >> beam.ParDo(convert_to_dataframe)

# Run the pipeline

pipeline.run()