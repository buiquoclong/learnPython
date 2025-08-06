# Import thư viện numpy với tên viết tắt là np
import numpy as np

# Tạo một mảng 1 chiều gồm các số nguyên
original_array = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# Tạo điều kiện lọc: các phần tử lớn hơn 4
condition = original_array > 4

# Tạo điều kiện lọc: các phần tử lớn hơn 3
condition1 = original_array > 3

# Tạo điều kiện lọc: các phần tử nhỏ hơn 6
condition2 = original_array < 6

# Kết hợp 2 điều kiện: phần tử lớn hơn 3 và nhỏ hơn 6
# Ký hiệu & dùng để kết hợp điều kiện (and), cần đặt trong dấu ngoặc
combined_condition = (condition1) & (condition2)

# Lọc mảng với điều kiện > 4
filtered_array = original_array[condition]

# Lọc mảng với điều kiện 3 < phần tử < 6
filtered_combine_array = original_array[combined_condition]

# In ra mảng gốc
print("original array: ", original_array)

# In ra mảng đã lọc theo điều kiện > 4
print("filtered_array (element > 4): ", filtered_array)

# In ra mảng đã lọc theo điều kiện 3 < phần tử < 6
print("filtered_array (3 < element < 6): ", filtered_combine_array)
