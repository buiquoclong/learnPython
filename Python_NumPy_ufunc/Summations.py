import numpy as np

data_array = np.array([10, 20, 30, 40, 50])

sum_result = np.sum(data_array)
print("Summation result: ", sum_result)

axis_sum_result =np.sum(data_array, axis=0)
print("Summation axis: ", axis_sum_result)

array = np.array([1, 2, 3, 4, 5])
new_array = np.cumsum(array)
print(new_array)