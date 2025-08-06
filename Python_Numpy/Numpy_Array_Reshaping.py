# Import thư viện numpy với tên viết tắt là np
import numpy as np

# Tạo một mảng 1 chiều gồm 6 phần tử
original_array = np.array([1, 2, 3, 4, 5, 6])

# Chuyển đổi mảng sang dạng 2 hàng, 3 cột theo thứ tự hàng trước (row-major - mặc định của C)
row_major = original_array.reshape(2, 3, order='C')

# Chuyển đổi mảng sang dạng 2 hàng, 3 cột theo thứ tự cột trước (column-major - giống Fortran)
column_major = original_array.reshape(2, 3, order='F')

# Chuyển đổi mảng mà không chỉ định thứ tự, mặc định là row-major ('C')
reshaped_array = original_array.reshape(2, 3)

# In ra mảng ban đầu
print("original_array: ")
print(original_array)

# In ra mảng sau khi reshape (mặc định row-major)
print("reshaped_array: ")
print(reshaped_array)

# In ra mảng đã reshape theo thứ tự row-major (C-style)
print("Row-major reshaped array:")
print(row_major)

# In ra mảng đã reshape theo thứ tự column-major (Fortran-style)
print("Column-major reshaped array: ")
print(column_major)
