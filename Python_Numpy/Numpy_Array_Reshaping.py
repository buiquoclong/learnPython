import numpy as np

original_array = np.array([1, 2, 3, 4, 5, 6])

row_major = original_array.reshape(2, 3, order='C')
column_major = original_array.reshape(2, 3, order='F')
reshaped_array = original_array.reshape(2, 3)

print("original_array: ")
print(original_array)
print("reshaped_array: ")
print(reshaped_array)

print("Row-major reshaped array:")
print(row_major)
print("Column-major reshaped array: ")
print(column_major)