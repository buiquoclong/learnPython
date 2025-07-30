import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 6, 7, 8, 9])

add_result = np.add(array1, array2)
print("Addition result: ", add_result)

subtract_result = np.subtract(array1, array2)
print("Subtraction result: ", subtract_result)

multiply_result = np.multiply(array1, array2)
print("Multiply result: ", multiply_result)

divide_result = np.divide(array1, array2)
print("Division result: ", divide_result)

scalar_mutiply = np.multiply(array1, 2)
print("Scalar multiplication result: ", scalar_mutiply)