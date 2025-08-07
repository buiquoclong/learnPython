# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Tạo dữ liệu có các dòng bị trùng lặp
data_with_duplicates = {
    "ProductID": ["P001", "P002", "P003", "P004"],  # Mã sản phẩm
    "Quantity": [10, 15, 20, 20]                    # Số lượng, dòng cuối trùng với dòng trước đó về Quantity
}

# Tạo DataFrame từ dữ liệu trên
df_with_duplicates = pd.DataFrame(data_with_duplicates)

# Tìm các dòng bị trùng lặp trong DataFrame
# .duplicated() trả về True cho các dòng trùng lặp (ngoại trừ dòng đầu tiên)
duplicates_rows = df_with_duplicates[df_with_duplicates.duplicated()]

# In ra các dòng bị trùng lặp
print("Duplicates Data: ")
print(duplicates_rows)

# Loại bỏ các dòng trùng lặp, giữ lại dòng đầu tiên xuất hiện (keep="first")
df_no_duplicates = df_with_duplicates.drop_duplicates(keep="first")

# In ra DataFrame sau khi đã loại bỏ dòng trùng lặp
print("\nRemoving Duplicates: ")
print(df_no_duplicates)
