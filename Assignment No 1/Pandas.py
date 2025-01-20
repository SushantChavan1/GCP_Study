import pandas as pd

a = [1, 2, 3, 4]

#Creating the pandas series 
pd1 = pd.Series(a) 

print("The pandas series is ", pd1)

#Creating the index to the pandas series 

pd1 = pd.Series(a ,index = ['a', 'b', 'c', 'd'])

print("The pandas series with index ", pd1)