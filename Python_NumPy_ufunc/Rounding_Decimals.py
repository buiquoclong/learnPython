import numpy as np

# Tạo mảng gồm các số thập phân (float)
decimal_array = np.array([3.14159, 2.1765, 1.4234, 0.7865])

# Làm tròn các phần tử trong mảng đến 2 chữ số thập phân
rounded_array = np.round(decimal_array, decimals=2)
print("Rounded array: ", rounded_array)
# Kết quả: [3.14, 2.18, 1.42, 0.79]

# Làm tròn các phần tử trong mảng đến 1 chữ số thập phân
around_result = np.around(decimal_array, decimals=1)
print("Around result: ", around_result)
# Kết quả: [3.1, 2.2, 1.4, 0.8]
