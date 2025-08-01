import pandas as pd

data_with_empty_cells = {"name": ['alice', "bob", None, "david"],
                         "age": [25, 30, None, 35],
                         "salary": [50000, None, 35000, 30000]}

df_with_empty_cells = pd.DataFrame(data_with_empty_cells)

empty_cells = df_with_empty_cells.isnull()
print("Identifying empty cells: ")
print(empty_cells)

cleaned_df_rows = df_with_empty_cells.dropna()
print("\nRemoving rows with empty cells: ")
print(cleaned_df_rows)