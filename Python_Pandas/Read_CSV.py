# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Đường dẫn tới file CSV
file_path = "data.csv"

# Đọc dữ liệu từ file CSV và lưu vào DataFrame
df = pd.read_csv(file_path)

# In ra nội dung DataFrame đọc được từ CSV (sẽ bị giới hạn số dòng nếu file lớn)
print("DataFrame from CSV: ")
print(df)

# In ra số dòng tối đa được pandas hiển thị khi in DataFrame (giá trị mặc định là 10 hoặc 60 tuỳ phiên bản)
print(pd.options.display.max_rows)

# Cập nhật tuỳ chọn hiển thị: cho phép hiển thị tối đa 9999 dòng khi in DataFrame
pd.options.display.max_rows = 9999

# Đọc lại dữ liệu từ file CSV sau khi tăng giới hạn hiển thị
df1 = pd.read_csv("data.csv")

# In toàn bộ nội dung DataFrame (được phép hiển thị nhiều dòng hơn trước)
print(df1)
