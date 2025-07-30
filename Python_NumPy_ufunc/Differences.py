import numpy as np

data_array = np.array([10, 20, 30, 40, 50, 60])
diff_result = np.diff(data_array)
print("Difference: ", diff_result)

axis_diff_result = np.diff(data_array, axis=0)
print("Difference along axis: ", axis_diff_result)

array = np.array([10, 50, 25, 56, 90])
new_array = np.diff(array, n=2)
print(new_array)