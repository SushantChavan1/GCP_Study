import pandas as pd
data = {'A': [1, 2], 'B': [3, 4]}
df = pd.DataFrame(data)

# loc (label-based)
print(df.loc[0])  # Access row with index label 0

# iloc (integer position-based)
print(df.iloc[0])  # Access row at position 0
