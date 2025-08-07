# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Tạo dữ liệu đầu vào với cột "Quantity" có một giá trị sai định dạng ("20a" chứa ký tự không hợp lệ)
data_wrong = {
    "ProductID": ["P001", "P002", "P003", "P004"],   # Mã sản phẩm
    "Quantity": ["10", "15", "20a", "25"]            # Số lượng (chuỗi), nhưng có 1 giá trị không hợp lệ
}

# Tạo DataFrame từ dữ liệu
df_wrong = pd.DataFrame(data_wrong)

# Tìm các dòng có dữ liệu sai định dạng ở cột "Quantity"
# Dùng str.isnumeric() để kiểm tra xem chuỗi chỉ toàn số hay không
wrong_data_rows = df_wrong[df_wrong["Quantity"].str.isnumeric() == False]

# In ra các dòng có dữ liệu không hợp lệ
print("Identifying wrong data: ")
print(wrong_data_rows)

# Loại bỏ các dòng chứa giá trị không hợp lệ trong cột "Quantity"
df_fixed = df_wrong[df_wrong["Quantity"].str.isnumeric()]

# In ra DataFrame đã được "làm sạch" - chỉ giữ lại dòng hợp lệ
print("Fixed data - Removing Invalid rows: ")
print(df_fixed)
