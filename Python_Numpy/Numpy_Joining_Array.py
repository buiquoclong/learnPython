import numpy as np

array = np.array([[10, 20, 30], [40, 45, 47]])
array1 = np.array([50, 60, 70])
array2 = np.array([80, 90, 100])

result1 = np.hstack((array1, array2))
print(result1)

result2 = np.vstack((array1, array2))
print(result2)

result3 = np.concatenate((array1, array2))
print(result3)

result4 = np.vstack((array, array1))
print(result4)