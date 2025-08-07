# Nhập thư viện pandas với tên viết tắt là pd
import pandas as pd

# Đọc dữ liệu từ file CSV có tên 'data.csv' và lưu vào biến df (DataFrame)
df = pd.read_csv('data.csv')

# In ra 5 dòng đầu tiên của DataFrame để xem trước dữ liệu
print(df.head())

# In ra 5 dòng cuối cùng của DataFrame để xem phần cuối của dữ liệu
print(df.tail())

# In ra thông tin tổng quan về DataFrame: số dòng, số cột, kiểu dữ liệu, số giá trị không null,...
print(df.info())
