# Import thư viện numpy với tên viết tắt là np
import numpy as np

# Tạo một mảng 1 chiều (1D array)
original_array = np.array([3, 4, 6, 8, 9, 1, 2, 2, 1, 7])

# Tạo một mảng 2 chiều (2D array) 3x3
original_array1 = np.array([[3, 4, 6],
                            [8, 9, 1],
                            [2, 2, 1]])

# -------------------------------
# SẮP XẾP MẢNG 1 CHIỀU (KHÔNG LÀM THAY ĐỔI MẢNG GỐC)
# -------------------------------

# np.sort() trả về một mảng mới đã được sắp xếp theo thứ tự tăng dần
sorted_array = np.sort(original_array)
print("sorted array:", sorted_array)
# Kết quả: [1 1 2 2 3 4 6 7 8 9]

# -------------------------------
# LẤY CHỈ SỐ SẮP XẾP (argsort)
# -------------------------------

# np.argsort() trả về mảng chứa chỉ số của các phần tử nếu được sắp xếp
indices = np.argsort(original_array)
print("indices for sorting: ", indices)
# Ví dụ: nếu kết quả là [5 8 6 ...], nghĩa là phần tử nhỏ nhất nằm ở index 5

# -------------------------------
# SẮP XẾP MẢNG 2 CHIỀU
# -------------------------------

# Sắp xếp từng hàng (axis=1): mỗi hàng được sắp xếp riêng biệt
sorted_row = np.sort(original_array1, axis=1)
print("sorted rows: ", sorted_row)
# Kết quả:
# [[3 4 6]
#  [1 8 9]
#  [1 2 2]]

# Sắp xếp từng cột (axis=0): mỗi cột được sắp xếp riêng biệt
sorted_column = np.sort(original_array1, axis=0)
print("sorted column: ", sorted_column)
# Kết quả:
# [[2 2 1]
#  [3 4 1]
#  [8 9 6]]

# -------------------------------
# SẮP XẾP MẢNG GỐC (IN-PLACE SORTING)
# -------------------------------

# original_array.sort() sắp xếp mảng gốc, không tạo mảng mới
original_array.sort()
print(original_array)
# Sau khi sort: [1 1 2 2 3 4 6 7 8 9]
