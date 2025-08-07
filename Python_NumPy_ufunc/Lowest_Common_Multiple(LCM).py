import numpy as np

# Danh sách các số nguyên
numbers = [12, 18, 24]

# Tính bội số chung nhỏ nhất (LCM) của các phần tử trong danh sách
lcm_result = np.lcm.reduce(numbers)
print("LCM result: ", lcm_result)
# Kết quả: 72 vì 72 là số nhỏ nhất chia hết cho cả 12, 18 và 24

# Tạo hàm LCM tùy chỉnh bằng frompyfunc sử dụng lambda gọi np.lcm
# 2: số tham số đầu vào; 1: số giá trị đầu ra
custom_lcm = np.frompyfunc(lambda x, y: np.lcm(x, y), 2, 1)
# Dùng reduce của hàm ufunc tùy chỉnh để tính LCM
result = custom_lcm.reduce(numbers)
print("Custom lcm: ", result)
# Kết quả tương tự: 72

# Tính LCM của mảng numpy
array = np.array([3, 6, 9, 12])
x = np.lcm.reduce(array)
print(x)
# Kết quả: 36 vì 36 là số nhỏ nhất chia hết cho 3, 6, 9, 12
