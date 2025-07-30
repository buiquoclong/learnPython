import numpy as np

x1 = np.sin(np.pi/2)
print(x1)

array = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x2 = np.sin(array)
print(x2)

array = np.array([90, 180, 270, 360])
x3 = np.deg2rad(array)
print(x3)

array1 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x4 = np.rad2deg(array1)
print(x4)

x5 = np.arcsin(1.0)
print(x5)

array2 = np.array([1, 1, 0.1])
x6 = np.arcsin(array2)
print(x6)

base = 3
perp = 4

x7 = np.hypot(base, perp)
print(x7)