import numpy as np

original_array = np.array([1, 2, 3, 4, 5, 6])
original_array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# shuffle_array = np.random.shuffle(original_array)
permuted_array = np.random.permutation(original_array)

permuted_rows = np.random.permutation(original_array1)
permuted_columns = np.random.permutation(original_array1.T).T

print("Permuted Array: ", permuted_array)
print("Permuted Rows: ", permuted_rows)
print("Permuted Columns: ", permuted_columns)