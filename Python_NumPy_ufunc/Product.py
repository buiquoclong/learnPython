import numpy as np

# Tạo mảng 1 chiều gồm các số nguyên
data_array = np.array([1, 2, 3, 4, 5])

# Tính tích (tích các phần tử trong mảng)
product_result = np.prod(data_array)
print("result: ", product_result)
# Kết quả: 120 (1*2*3*4*5)

# Tính tích dọc theo trục (axis=0)
# Với mảng 1 chiều thì tương tự như trên
axis_product_result = np.prod(data_array, axis=0)
print("Along axis result: ", axis_product_result)

# Tạo mảng mới
array = np.array([5, 6, 7, 8, 9])

# Tính tích lũy (cumulative product) của mảng
new_array = np.cumprod(array)
print(new_array)
# Kết quả: [5, 30, 210, 1680, 15120]
# Giải thích: 5, 5*6=30, 30*7=210, 210*8=1680, 1680*9=15120
