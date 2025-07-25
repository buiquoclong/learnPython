import numpy as np

array_1D = np.array([1, 2, 3, 4, 5])
array_2D = np.array([[1, 2, 3], [4, 5, 6]])
array_3D = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])

print("Shape of 1D array:", array_1D.shape)
print("Shape of 2D array:", array_2D.shape)
print("Shape of 3D array:", array_3D.shape)

array = np.array([1, 2, 3, 4], ndmin=5)
print(array)
print("Shape of array: ", array.shape)