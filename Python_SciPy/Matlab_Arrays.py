import scipy.io
import numpy as np

python_array = np.array([[1, 2, 3], [4, 5, 6]])
scipy.io.savemat("python_data.mat", {"myMatArray": python_array})

mat_data = scipy.io.loadmat("matlab_data.mat")

mat_array = mat_data["myMatArray"]

print("MATLAB Array in Python")
print(mat_array)

sum_column2 = np.sum(mat_array[:, 1])
print(f"Sum of the second column: ", sum_column2)
