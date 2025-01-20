import pandas as pd

def get_data():
    data = pd.read_csv('EV.csv')
    return data

def transform_data(data):
    data = data.dropna()
    print("Price is converted to INR")
    data['Price_India'] = data['Price_USD'] * 83
    print("Price_USD column is removed")
    data = data.drop('Price_USD', axis=1)
    return data

def save_data(data):
    data.to_csv('EV_India.csv')
    print("Data saved successfully")

data = get_data()



print("Data loaded successfully")
data = transform_data(data)
print("Data transformed successfully")
save_data(data)
print("The data is::",data)
print("The cloumns are::",data.columns)
