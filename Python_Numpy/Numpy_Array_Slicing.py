# Import thư viện NumPy để làm việc với mảng
import numpy as np

# Tạo một mảng 1 chiều chứa các số từ 0 đến 9
array_1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing mảng 1 chiều từ chỉ số 2 đến 5 (vị trí 6 không được lấy)
# Lấy các phần tử từ chỉ số 2 đến 5 (bao gồm phần tử tại chỉ số 2 và 5)
slice_result = array_1D[2:6]
# In ra mảng con sau khi slicing
print(slice_result)

# Slicing mảng 1 chiều từ chỉ số 1 đến 8 với bước nhảy là 2
slice_result_1D = array_1D[1:9:2]
# In ra mảng con sau khi slicing
print(slice_result_1D)

# Tạo một mảng 2 chiều 3x3
array_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing mảng 2 chiều để lấy các phần tử từ hàng 0 đến 1 (không bao gồm hàng 2)
# và lấy các phần tử từ cột 1 đến 2 (không bao gồm cột 3)
slice_result = array_2D[0:2, 1:3]
# In ra mảng con sau khi slicing
print(slice_result)
