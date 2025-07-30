import numpy as np

data_array = np.array([1, 2, 3, 4, 5])

product_result = np.prod(data_array)
print("result: ", product_result)

axis_product_result = np.prod(data_array, axis=0)
print("Along axis result: ", axis_product_result)

array = np.array([5, 6, 7, 8,9 ])
new_array = np.cumprod(array)
print(new_array)