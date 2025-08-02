import numpy as np

from scipy.sparse import csr_matrix

dense_matrix = np.array([[1, 0, 0], [0, 0, 2], [3, 0, 4]])
array = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

sparse_matrix = csr_matrix(dense_matrix)

print("Dense matrix: ",)
print(dense_matrix)
print("\nSpare matrix: ")
print(sparse_matrix)

print(csr_matrix(array).count_nonzero())

mat = csr_matrix(array)
mat.eliminate_zeros()

print(mat)

new_array = csr_matrix(array).tocsc()
print(new_array)