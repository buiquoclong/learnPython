# Nhập thư viện pandas để xử lý dữ liệu dạng bảng
import pandas as pd

# Tạo một DataFrame có chứa các ô bị thiếu (giá trị None)
data_with_empty_cells = {
    "name": ['alice', "bob", None, "david"],   # Cột tên, có 1 giá trị bị thiếu (None)
    "age": [25, 30, None, 35],                 # Cột tuổi, có 1 giá trị bị thiếu
    "salary": [50000, None, 35000, 30000]      # Cột lương, có 1 giá trị bị thiếu
}

# Chuyển dữ liệu thành DataFrame
df_with_empty_cells = pd.DataFrame(data_with_empty_cells)

# Kiểm tra các ô bị thiếu bằng cách dùng isnull() – trả về True nếu ô đó bị thiếu
empty_cells = df_with_empty_cells.isnull()
print("Identifying empty cells: ")
print(empty_cells)  # In ra bảng boolean cho biết ô nào bị thiếu dữ liệu

# Xoá các dòng có ít nhất một ô bị thiếu dữ liệu
cleaned_df_rows = df_with_empty_cells.dropna()
print("\nRemoving rows with empty cells: ")
print(cleaned_df_rows)  # In ra DataFrame sau khi đã xoá các dòng chứa giá trị None
