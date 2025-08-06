# Import thư viện numpy với tên viết tắt là np
import numpy as np

# Tạo một mảng 1 chiều (1D array) gồm 5 phần tử
array_1D = np.array([1, 2, 3, 4, 5])

# Tạo một mảng 2 chiều (2D array) gồm 2 hàng, 3 cột
array_2D = np.array([[1, 2, 3], [4, 5, 6]])

# Tạo một mảng 3 chiều (3D array) có cấu trúc 1 x 4 x 2
array_3D = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])

# In ra kích thước (shape) của từng mảng
print("Shape of 1D array:", array_1D.shape)     # (5,)
print("Shape of 2D array:", array_2D.shape)     # (2, 3)
print("Shape of 3D array:", array_3D.shape)     # (1, 4, 2)

# Tạo một mảng với tối thiểu 5 chiều (ndmin=5)
array = np.array([1, 2, 3, 4], ndmin=5)

# In ra mảng đã tạo (sẽ có nhiều dấu ngoặc [] tương ứng với chiều cao)
print(array)

# In ra shape của mảng (kết quả sẽ là (1, 1, 1, 1, 4))
print("Shape of array: ", array.shape)
