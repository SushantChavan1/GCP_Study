import pandas as pd

# Sample dataset in list format
data = [
    ["Alice", 25, "Female", "North"],
    ["Bob", 17, "Male", "South"],
    ["Charlie", 40, "Male", "East"],
    ["David", 30, "Male", "West"],
    ["Emma", 22, "Female", "North"],
]

# Column names
columns = ["Name", "Age", "Gender", "Region"]

# Convert list data to DataFrame
df = pd.DataFrame(data, columns=columns)

# Add a prefix based on gender
for i in range(len(df)):

    if df.loc[i, "Gender"] == "Male":  #the purpose of the loc function is to access a group of rows and columns by labels or a boolean array.
        prefix = "Mr. "  
    else:
        prefix = "Mrs. "
    df.loc[i, "Name"] = prefix + df.loc[i, "Name"]

# Categorize age group
for i in range(len(df)):
    if df.loc[i, "Age"] < 18 :
        df.loc[i, "Age Category"] = "Young" 
    else :
        df.loc[i, "Age Category"] = "Adult"

# Display results
print("Transformed DataFrame:")
print(df)
