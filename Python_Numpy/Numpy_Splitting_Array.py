import numpy as np

original_array = np.array([1, 2, 3, 4, 5, 6])
original_array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
original_array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
result = np.split(original_array, 3)
print(result)

result1 = np.split(original_array, [2, 4])
print(result1)

result2 = np.split(original_array1, 3, axis=1)
print(result2)

result3 = np.array_split(original_array2, [2, 5])
print(result3)