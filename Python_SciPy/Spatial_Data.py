import numpy as np
from scipy.sparse import csr_matrix

# Tạo ma trận dày (dense matrix)
dense_matrix = np.array([[1, 0, 0], 
                         [0, 0, 2], 
                         [3, 0, 4]])

# Chuyển ma trận dense sang dạng ma trận thưa CSR (Compressed Sparse Row)
spare_matrix = csr_matrix(dense_matrix)

print("Dense matrix: ")
print(dense_matrix)  # In ma trận dày

print("\nSparse matrix: ")
print(spare_matrix)  # In ma trận thưa dạng CSR (chỉ in thông tin, không in toàn bộ ma trận)

# Tạo một ma trận numpy khác để chuyển sang dạng thưa
array = np.array([[0, 0, 0], 
                  [0, 0, 1], 
                  [1, 0, 2]])

# Lấy ra mảng dữ liệu (phần tử khác 0) trong ma trận thưa
print(csr_matrix(array).data)  # In ra các phần tử khác 0

# Đếm số phần tử khác 0 trong ma trận thưa
print(csr_matrix(array).count_nonzero())

# Tạo ma trận thưa từ 'array'
mat = csr_matrix(array)

# Loại bỏ các phần tử bằng 0 dư thừa trong ma trận thưa (nếu có)
mat.eliminate_zeros()

# Gộp các phần tử trùng lặp (nếu ma trận có phần tử lặp vị trí)
mat.sum_duplicates()

print(mat)  # In ma trận thưa sau khi loại bỏ 0 dư và gộp phần tử trùng

# Chuyển đổi ma trận thưa từ CSR sang CSC (Compressed Sparse Column)
new_array = csr_matrix(array).tocsc()

print(new_array)  # In ma trận dưới dạng CSC
