import pandas as pd

file_path = "data.csv"
df = pd.read_csv(file_path)

print("DataFrame from CSV: ")
print(df)

print(pd.options.display.max_rows)
pd.options.display.max_rows = 9999

df1 = pd.read_csv("data.csv")
print(df1)
