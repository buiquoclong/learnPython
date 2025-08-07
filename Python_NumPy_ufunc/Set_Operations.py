import numpy as np

# Tạo mảng với các phần tử có thể bị trùng lặp
array = np.array([1, 2, 1, 4, 5, 3, 2, 4])

# Lấy các phần tử duy nhất (unique) trong mảng
x = np.unique(array)
print(x)
# Kết quả: [1 2 3 4 5]

# Tạo 2 mảng khác
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 2, 7, 8, 5])

# Lấy hợp (union) của hai mảng, tức là tập hợp tất cả phần tử không trùng lặp
new_array = np.union1d(array1, array2)
print(new_array)
# Kết quả: [1 2 3 4 5 7 8]

# Lấy giao (intersection) của hai mảng, tức là các phần tử xuất hiện trong cả hai mảng
new_array1 = np.intersect1d(array1, array2, assume_unique=True)
print(new_array1)
# Kết quả: [2 3 5]

# Tạo hai tập hợp khác
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

# Lấy hiệu (difference) của set1 trừ đi set2, tức là các phần tử chỉ có trong set1 mà không có trong set2
new_array2 = np.setdiff1d(set1, set2, assume_unique=True)
print(new_array2)
# Kết quả: [1 2]
