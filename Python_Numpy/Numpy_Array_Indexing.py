# Import thư viện NumPy để làm việc với mảng
import numpy as np

# Tạo mảng 1 chiều với các phần tử từ 0 đến 4
array_1D = np.array([0, 1, 2, 3, 4])

# In ra phần tử tại vị trí chỉ số 2 (bắt đầu từ 0)
# Kết quả sẽ là giá trị tại vị trí thứ 3 của mảng (index 2)
print(array_1D[2])

# In ra phần tử cuối cùng của mảng (sử dụng index âm để lấy phần tử cuối cùng)
# index -1 là phần tử cuối cùng của mảng
print(array_1D[-1])

# Tạo một mảng 1 chiều mới với các giá trị từ 1 đến 9
new_array_1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Tạo một mảng boolean (mask) để lọc các giá trị lớn hơn 2
mask = new_array_1D > 2
# In ra mảng con chứa các giá trị thỏa mãn điều kiện mask (lớn hơn 2)
# Chỉ các giá trị trong new_array_1D mà lớn hơn 2 sẽ được in ra
print(new_array_1D[mask])

# Tạo một mảng 2 chiều 3x3
array_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# In ra phần tử tại vị trí hàng thứ 2, cột thứ 3 (index bắt đầu từ 0)
# array_2D[1, 2] sẽ lấy giá trị ở hàng thứ 2 và cột thứ 3
print(array_2D[1, 2])
