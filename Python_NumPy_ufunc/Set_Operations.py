import numpy as np

array = np.array([1, 2, 1, 4, 5, 3, 2, 4])

x = np.unique(array)
print(x)

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 2, 7, 8, 5])

new_array = np.union1d(array1, array2)
print(new_array)

new_array1 = np.intersect1d(array1, array2, assume_unique=True)
print(new_array1)

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

new_array2 = np.setdiff1d(set1, set2, assume_unique=True)
print(new_array2)