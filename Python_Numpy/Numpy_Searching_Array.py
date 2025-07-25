import numpy as np

original_array = np.array([1, 2, 5, 7, 9, 4])
result = np.where(original_array == 4)
print(result)

result1 = np.searchsorted(original_array, 4)
print(result1)

result2 = original_array[original_array > 4]
print(result2)

condition = original_array > 4
result3 = np.extract(condition, original_array)
print(result3)