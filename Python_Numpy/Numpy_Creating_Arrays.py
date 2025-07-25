# Import thư viện NumPy để làm việc với mảng
import numpy as np

# Tạo một mảng 1 chiều với các phần tử từ 1 đến 5
array_1D = np.array([1, 2, 3, 4, 5])
# In ra mảng 1 chiều
print("array_1D: ", array_1D)

# Tạo một mảng 2 chiều, mảng này có 2 hàng và 3 cột
array_2D = np.array([[1, 2, 3], [4, 5, 6]])
# In ra mảng 2 chiều
print("array_2D: ", array_2D)

# Tạo một mảng 3 chiều. Mảng này có 2 khối, mỗi khối là một mảng 2D với 2 hàng và 3 cột
array_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# In ra mảng 3 chiều
print(array_3D)

# Tạo một mảng với 5 chiều, các chiều đầu tiên có kích thước 1, và chiều cuối cùng chứa 4 phần tử
array = np.array([1, 2, 3, 4], ndmin=5)
# In ra mảng 5 chiều
print(array)
# In ra số chiều của mảng 
print(array.ndim)
