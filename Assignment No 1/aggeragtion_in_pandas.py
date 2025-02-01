import pandas as pd
data = {'students': ['sushant', 'Rohan', 'sushant'], 'marks': [30, 20, 50]}
df = pd.DataFrame(data)
grouped = df.groupby('students').sum()  # Group by 'students' and sum the marks
#the groupby() method is used to split the data into groups based on some criteria.
print(grouped)
