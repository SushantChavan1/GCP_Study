import pandas as pd
#apply() method is used to apply a function along an axis of the DataFrame or on values of Series.
df = pd.DataFrame({'A': [1, 2, 3]})
df['B'] = df['A'].apply(lambda x: x**2)  # Square each value in column 'A'
print(df)
