# Import thư viện NumPy để làm việc với mảng
import numpy as np

# Tạo một mảng 1 chiều ban đầu
original_array = np.array([1, 2, 3, 4, 5])

# Tạo một bản sao (copy) độc lập của mảng
copied_array = original_array.copy()

# Thay đổi giá trị phần tử đầu tiên của mảng sao chép
copied_array[0] = 99

# In ra mảng gốc (không bị ảnh hưởng vì đã copy độc lập)
print("original array: ", original_array)

# In ra mảng đã được thay đổi
print("copied array: ", copied_array)

# Tạo một view (liên kết bộ nhớ) từ mảng gốc
array_view = original_array.view()

# Thay đổi phần tử đầu tiên trong view
array_view[0] = 99

# In ra mảng gốc (bị ảnh hưởng do view dùng chung bộ nhớ)
print("original array: ", original_array)

# In ra view sau khi chỉnh sửa
print("view array: ", array_view)

# Tạo một mảng 2 chiều ban đầu
original_array_2D = np.array([[1, 2, 3], [4, 5, 6]])

# Tạo một view từ mảng 2 chiều
array_view_2D = original_array_2D.view()

# Thay đổi hình dạng (shape) của view thành 3 hàng, 2 cột
array_view_2D.shape = (3, 2)

# In ra mảng gốc (shape không bị ảnh hưởng)
print("original array: ")
print(original_array_2D)

# In ra view (đã bị thay đổi shape nhưng vẫn dùng chung dữ liệu với mảng gốc)
print("view array: ")
print(array_view_2D)
