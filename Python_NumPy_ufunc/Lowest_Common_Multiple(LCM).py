import numpy as np

numbers = [12, 18, 24]
lcm_result = np.lcm.reduce(numbers)
print("LCM result: ", lcm_result)

custom_lcm = np.frompyfunc(lambda x, y: np.lcm(x, y), 2, 1)
result = custom_lcm.reduce(numbers)
print("Custom lcm: ", result)

array = np.array([3, 6, 9, 12])
x = np.lcm.reduce(array)
print(x)