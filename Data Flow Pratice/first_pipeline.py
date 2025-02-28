#In this example I am creating the in memmory data and then 
#creating the pipeline in simple way then just applying the ParDo for printing the elements 

import apache_beam as beam 

# Create a pipeline object
pipeline = beam.Pipeline()

# Create a list of elements
list_elements = ['apple', 'banana', 'cherry', 'mango', 'orange']

# Create a PCollection from a list of elements

elements = pipeline | 'Create PCollection' >> beam.Create(list_elements) #create method is used to create the PCollection

# Apply a ParDo transform to the PCollection



elements = elements | 'Print elements' >> beam.ParDo(lambda element: print(element))
#here we dont need to pass the parameter to the function it will automatically managed by the beam
# Run the pipeline

pipeline.run()