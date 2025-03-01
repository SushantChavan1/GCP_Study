#In this program I am going to extract the information like function are in the packages
#that are imported in the program
#I will be using the inspect module to extract the information of the functions

#Importing the packages

import google.cloud.bigquery as bigquery

import pandas_gbq as pd

print("Extracting the functions from the BigQuery package")
print(dir(bigquery))

print()

print("Extracting the functions from the pandas.gbq package")
print(dir(pd))

print()



