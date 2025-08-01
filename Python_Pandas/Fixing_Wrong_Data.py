import pandas as pd

data_wrong = {
    "ProductID": ["P001", "P002", "P003", "P004"],
    "Quantity": ["10", "15", "20a", "25"]
}

df_wrong = pd.DataFrame(data_wrong)

wrong_data_rows = df_wrong[df_wrong["Quantity"].str.isnumeric() == False]

print("Identifying wrong data: ")
print(wrong_data_rows)

df_fixed = df_wrong[df_wrong["Quantity"].str.isnumeric()]
print("Fixed data - Removing Invalid rows: ")
print(df_fixed)