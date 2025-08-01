import pandas as pd

data_with_duplicates = {
    "ProductID": ["P001", "P002", "P003", "P004"],
    "Quantity": [10, 15, 20, 20]
}

df_with_duplicates = pd.DataFrame(data_with_duplicates)

duplicates_rows = df_with_duplicates[df_with_duplicates.duplicated()]
print("Duplicates Data: ")
print(duplicates_rows)

df_no_duplicates = df_with_duplicates.drop_duplicates(keep="first")
print("\nRemoving Duplicates: ")
print(df_no_duplicates)