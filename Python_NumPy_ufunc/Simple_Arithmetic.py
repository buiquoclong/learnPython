import numpy as np

# Tạo hai mảng 1 chiều
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 6, 7, 8, 9])

# Cộng hai mảng (cộng phần tử tương ứng)
add_result = np.add(array1, array2)
print("Addition result: ", add_result)
# Kết quả: [6 8 10 12 14]

# Trừ hai mảng (trừ phần tử tương ứng)
subtract_result = np.subtract(array1, array2)
print("Subtraction result: ", subtract_result)
# Kết quả: [-4 -4 -4 -4 -4]

# Nhân hai mảng (nhân phần tử tương ứng)
multiply_result = np.multiply(array1, array2)
print("Multiply result: ", multiply_result)
# Kết quả: [5 12 21 32 45]

# Chia hai mảng (chia phần tử tương ứng)
divide_result = np.divide(array1, array2)
print("Division result: ", divide_result)
# Kết quả: [0.2        0.33333333 0.42857143 0.5        0.55555556]

# Nhân mảng với một số vô hướng (scalar)
scalar_mutiply = np.multiply(array1, 2)
print("Scalar multiplication result: ", scalar_mutiply)
# Kết quả: [ 2  4  6  8 10]
