import numpy as np

# Tính hàm hyperbolic sine sinh(x) tại x = π/2
x = np.sinh(np.pi / 2)
print(x)
# Kết quả là sinh(π/2)

# Tính hàm ngược của sinh (arcsinh) tại giá trị 2.0
x1 = np.arcsinh(2.0)
print(x1)
# arcsinh là hàm ngược của sinh, trả về giá trị x sao cho sinh(x) = 2.0

# Tạo mảng dữ liệu gồm các giá trị trong khoảng (-1, 1)
array = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

# Tính hàm arctanh (hàm ngược của hàm hyperbolic tangent tanh) cho từng phần tử trong mảng
x2 = np.arctanh(array)
print(x2)
# Lưu ý: arctanh chỉ định nghĩa với giá trị đầu vào nằm trong khoảng (-1, 1)
