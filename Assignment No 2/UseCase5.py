import pandas as pd

# Create list-based data
customers = [
    [1, "Alice", 25, "Female"],
    [2, "Bob", 17, "Male"],
    [3, "Charlie", 40, "Male"],
    [4, "David", 30, "Male"],
    [5, "Emma", 22, "Female"]
]
products = [
    [101, "Laptop", "Electronics"],
    [102, "Shirt", "Clothing"],
    [103, "Book", "Stationery"]
]
sales = [
    [1, 101, 2],
    [2, 103, 1],
    [3, 102, 3],
    [4, 101, 1],
    [5, 103, 2]
]

# Convert to DataFrame
customers_df = pd.DataFrame(customers, columns=["CustomerID", "Name", "Age", "Gender"])
products_df = pd.DataFrame(products, columns=["ProductID", "Product", "Category"])
sales_df = pd.DataFrame(sales, columns=["CustomerID", "ProductID", "Quantity"])

# Function to add name prefix
def add_name_prefix(df):
    df["Full Name"] = df["Gender"].apply(lambda g: "Mr. " if g == "Male" else "Mrs. ") + df["Name"]

def categorize_age(df):
    df["Age Category"] = df["Age"].apply(lambda x: "Young" if x < 18 else "Adult")

def merge_sales_data(sales_df, customers_df, products_df):
    sales_df = sales_df.merge(customers_df[["CustomerID", "Age Category"]], on="CustomerID")
    sales_df = sales_df.merge(products_df[["ProductID", "Category"]], on="ProductID")
    return sales_df

# Apply transformations
add_name_prefix(customers_df)
categorize_age(customers_df)
sales_df = merge_sales_data(sales_df, customers_df, products_df)

# Save to CSV files
customers_df.to_csv("customers.csv", index=False)
products_df.to_csv("products.csv", index=False)
sales_df.to_csv("sales.csv", index=False)

print("Data saved to CSV files successfully!")
