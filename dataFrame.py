import pandas as pd

dict = { "name" : ["Sushant", "Rohan", "Shivtej", "Vinayak", "Vaibhav", "Shahaji"],
          "marks" : [80, 90, 91, 92, 93, 95]
        }
#Here I create the dataframe by using the dictonary  

dFrame = pd.DataFrame( dict )

#Printing the type of dFrame
print("The type ",type(dFrame))

print("The DataFrame is ")

print(dFrame)

# The loc attribute is used to return the specific row with the help of specifing the row and coloumn index we can retrive the specific value

print("The first row is ",dFrame.loc[0][1]) 

#Dataframe creating with specified index

dFrame = pd.DataFrame( dict , ["st1", "st2", "st3", "st4", "st5", "st6"])

print(dFrame)

#The head() method return the headers and top 5 rows by default
print("The header ",dFrame.head(10))

#The tail() mthod return the bottom 5 records by default same as like the head()
print("The bottom records ",dFrame.tail())

#The info() method return the information about the dataframe
print("Information about the DataFrame ",dFrame.info())

#Loading the csv file into the DataFrame

dFrame_csv = pd.read_csv('username.csv')

print(dFrame_csv.to_string())

#Creating the dataframe from csv

dFrame = pd.DataFrame(dFrame_csv )

print(dFrame)

#Creating the DataFrame using the json file

dFrame_json = pd.read_json('sample.json')

print(dFrame_json.to_string())



