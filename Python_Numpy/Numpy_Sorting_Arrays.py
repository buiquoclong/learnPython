import numpy as np

original_array = np.array([3, 4, 6, 8, 9, 1, 2, 2, 1, 7])
original_array1 = np.array([[3, 4, 6], [8, 9, 1], [2, 2, 1]])

sorted_array = np.sort(original_array)
print("sorted array:",sorted_array)

indices = np.argsort(original_array)
print("indices for sorting: ", indices)

sorted_row = np.sort(original_array1, axis=1)
sorted_column = np.sort(original_array1, axis=0)

print("sorted rows: ", sorted_row)
print("sorted column: ", sorted_column)

original_array.sort()
print(original_array)