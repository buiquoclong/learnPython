# Plot là quá trình vẽ đồ thị hoặc biểu đồ để trực quan hóa dữ liệu.
# Matplotlib là một thư viện mạnh mẽ trong Python dùng để vẽ đồ thị và biểu đồ.

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])  # Tạo mảng NumPy với các điểm x từ 1 đến 8
ypoints = np.array([3, 10])  # Tạo mảng NumPy với các điểm y tương ứng

plt.plot(xpoints, ypoints)  # Vẽ biểu đồ đường với các điểm x và y
plt.title('Simple Plot')  # Thêm tiêu đề cho biểu đồ
plt.xlabel('X-axis')  # Thêm nhãn cho trục x
plt.ylabel('Y-axis')  # Thêm nhãn cho trục y
plt.grid(True)  # Hiển thị lưới trên biểu đồ để dễ dàng đọc
plt.show()  # Hiển thị biểu đồ 