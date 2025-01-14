#Pandas is python library used for working with the data sets
# pip install pandas it will install the pandas

import pandas as pd

#creating the smaple data

data = {
    'Name' : ['Sushant','Rohan','Vinayak','Shivtej','Vaibhav'],
    'Age' : [21,22,23,24,25],
    'Division' : ['A','B','C','D','E'],
}

print(data)

#creating the dataframe

my_data = pd.DataFrame(data)#It will create the dataframe

print(my_data)

#