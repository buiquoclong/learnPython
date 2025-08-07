import numpy as np

# Tính Ước số chung lớn nhất (GCD) của các phần tử trong danh sách bằng hàm reduce của np.gcd
gcd_result = np.gcd.reduce([24, 36, 48, 50, 56, 78])
print("gcd result: ", gcd_result)
# Kết quả: 2 vì 2 là số lớn nhất chia hết cho tất cả các số trên

# Tạo hàm GCD tùy chỉnh bằng frompyfunc sử dụng lambda gọi np.gcd
# 2: số tham số đầu vào; 1: số giá trị đầu ra
custom_gcd = np.frompyfunc(lambda x, y: np.gcd(x, y), 2, 1)
# Dùng reduce của hàm ufunc tùy chỉnh để tính GCD
result = custom_gcd.reduce([14, 36, 48, 50, 56, 78])
print("custom gcd: ", result)
# Kết quả tương tự: 2

# Tính GCD của mảng numpy
array = np.array([20, 8, 45, 28, 36, 16])
x = np.gcd.reduce(array)
print(x)
# Kết quả: 1 vì không có số lớn hơn 1 chia hết cho tất cả phần tử trong mảng này
