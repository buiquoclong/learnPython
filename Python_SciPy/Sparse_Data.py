import numpy as np
from scipy.sparse import csr_matrix

# Tạo ma trận dày (dense matrix) - đa phần là số khác 0
dense_matrix = np.array([[1, 0, 0], 
                         [0, 0, 2], 
                         [3, 0, 4]])

# Tạo một ma trận numpy khác để chuyển sang dạng thưa
array = np.array([[0, 0, 0], 
                  [0, 0, 1], 
                  [1, 0, 2]])

# Chuyển ma trận dense sang dạng ma trận thưa CSR (Compressed Sparse Row)
sparse_matrix = csr_matrix(dense_matrix)

print("Dense matrix: ")
print(dense_matrix)

print("\nSparse matrix: ")
print(sparse_matrix)  # In ra thông tin ma trận thưa (không in toàn bộ ma trận)

# Đếm số phần tử khác 0 trong ma trận thưa được tạo từ 'array'
print(csr_matrix(array).count_nonzero())

# Tạo ma trận thưa từ 'array' và loại bỏ phần tử 0 thực sự nếu có
mat = csr_matrix(array)
mat.eliminate_zeros()  # Loại bỏ các phần tử bằng 0 trong ma trận thưa

print(mat)  # In ma trận sau khi loại bỏ số 0 thừa

# Chuyển đổi định dạng ma trận thưa từ CSR sang CSC (Compressed Sparse Column)
new_array = csr_matrix(array).tocsc()
print(new_array)  # In ma trận dưới dạng CSC
