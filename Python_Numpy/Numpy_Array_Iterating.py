import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
print("For for 1D array: ")
for element  in my_array:
    print(element)


print("----------------------")
print("For for 2D array: ")
array_2D = np.array([[1, 2, 3], [4, 5, 6]])
for row in array_2D:
    for element in row:
        print(element)


print("----------------------")
for element in np.nditer(array_2D):
    print(element)