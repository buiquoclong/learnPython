import numpy as np

original_array = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

condition = original_array > 4
condition1 = original_array > 3
condition2 = original_array < 6
combined_condition = (condition1) & (condition2)

filtered_array = original_array[condition]
filtered_combine_array = original_array[combined_condition]
print("original array: ", original_array)
print("filtered_array (element > 4): ", filtered_array)
print("filtered_array (3 < element < 6): ", filtered_combine_array)