# Import thư viện numpy và đặt tên rút gọn là np
import numpy as np

# Tạo một mảng 1 chiều (1D array)
my_array = np.array([1, 2, 3, 4, 5])

print("For for 1D array: ")
# Duyệt qua từng phần tử trong mảng 1 chiều và in ra
for element in my_array:
    print(element)


print("----------------------")
print("For for 2D array: ")

# Tạo một mảng 2 chiều (2D array) với 2 hàng và 3 cột
array_2D = np.array([[1, 2, 3], [4, 5, 6]])

# Duyệt qua từng hàng trong mảng 2 chiều
for row in array_2D:
    # Duyệt qua từng phần tử trong từng hàng
    for element in row:
        print(element)


print("----------------------")
# Sử dụng np.nditer để duyệt qua từng phần tử trong mảng 2 chiều một cách tuyến tính
for element in np.nditer(array_2D):
    print(element)
