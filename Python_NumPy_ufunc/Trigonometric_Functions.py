import numpy as np

# Tính sin của π/2 (90 độ) - kết quả là 1
x1 = np.sin(np.pi/2)
print(x1)  # Output: 1.0

# Tạo mảng gồm các giá trị radian, tính sin của từng phần tử
array = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x2 = np.sin(array)
print(x2)  
# Output: [1.         0.8660254  0.70710678 0.58778525]

# Chuyển đổi các góc từ độ sang radian
array = np.array([90, 180, 270, 360])
x3 = np.deg2rad(array)
print(x3)
# Output: [1.57079633 3.14159265 4.71238898 6.28318531]

# Chuyển đổi các góc từ radian sang độ
array1 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x4 = np.rad2deg(array1)
print(x4)
# Output: [ 90. 180. 270. 360.]

# Tính arcsin (hàm nghịch đảo của sin) của 1.0, kết quả ra radian
x5 = np.arcsin(1.0)
print(x5)
# Output: 1.5707963267948966 (tương đương π/2)

# Tính arcsin cho từng phần tử trong mảng (phần tử trong khoảng [-1,1])
array2 = np.array([1, 1, 0.1])
x6 = np.arcsin(array2)
print(x6)
# Output: [1.57079633 1.57079633 0.10016742]

# Tính độ dài cạnh huyền (hypotenuse) trong tam giác vuông với hai cạnh góc vuông base và perp
base = 3
perp = 4
x7 = np.hypot(base, perp)
print(x7)
# Output: 5.0 (theo định lý Pythagoras)
