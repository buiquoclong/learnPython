import numpy as np
from scipy.sparse import csr_matrix

dense_matrix = np.array([[1, 0, 0], [0, 0, 2], [3, 0, 4]])

spare_matrix = csr_matrix(dense_matrix)

print("Dense matrix: ")
print(dense_matrix)
print("\nSpare matrix: ")
print(spare_matrix)

array = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(array).data)
print(csr_matrix(array).count_nonzero())

mat = csr_matrix(array)
mat.eliminate_zeros()
mat.sum_duplicates()

print(mat)

new_array = csr_matrix(array).tocsc()
print(new_array)

