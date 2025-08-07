# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Đọc dữ liệu từ file CSV có tên "data.csv" và lưu vào biến df (DataFrame)
df = pd.read_csv("data.csv")

# In toàn bộ nội dung DataFrame ra màn hình
print(df)
