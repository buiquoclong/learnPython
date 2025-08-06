import numpy as np

# Khởi tạo mảng 1 chiều
original_array = np.array([1, 2, 3, 4, 5, 6])

# Khởi tạo mảng 2 chiều 3x3
original_array1 = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])

# np.random.permutation tạo ra bản sao được hoán vị của mảng đầu vào (không thay đổi mảng gốc)
# Hoán vị các phần tử của mảng 1 chiều
permuted_array = np.random.permutation(original_array)

# Hoán vị các hàng của mảng 2 chiều
permuted_rows = np.random.permutation(original_array1)

# Hoán vị các cột:
# Đầu tiên chuyển vị mảng (từ hàng thành cột)
# Hoán vị các hàng của mảng đã chuyển vị (tức là hoán vị cột ban đầu)
# Sau đó chuyển vị lại để trả về dạng ban đầu
permuted_columns = np.random.permutation(original_array1.T).T

# In kết quả
print("Permuted Array: ", permuted_array)          # Hoán vị phần tử mảng 1D
print("Permuted Rows: ", permuted_rows)            # Hoán vị các hàng mảng 2D
print("Permuted Columns: ", permuted_columns)      # Hoán vị các cột mảng 2D
