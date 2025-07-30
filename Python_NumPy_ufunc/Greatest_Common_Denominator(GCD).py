import numpy as np

gcd_result = np.gcd.reduce([24, 36, 48, 50, 56, 78])
print("gcd result: ", gcd_result)

custom_gcd = np.frompyfunc(lambda x, y: np.gcd(x, y), 2, 1)
result = custom_gcd.reduce([14, 36, 48, 50, 56, 78])
print("custom gcd: ", result)

array = np.array([20, 8, 45, 28, 36, 16])
x = np.gcd.reduce(array)
print(x)