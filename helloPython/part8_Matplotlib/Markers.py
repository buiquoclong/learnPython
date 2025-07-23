# Marker là các biểu tượng được sử dụng trong biểu đồ để đại diện cho các điểm dữ liệu.
# Matplotlib cung cấp nhiều loại marker khác nhau để tùy chỉnh cách hiển thị các điểm dữ liệu.  
# Các loại marker bao gồm hình tròn, hình vuông, hình tam giác, và nhiều loại khác.

# Import thư viện matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu để vẽ biểu đồ
ypoints = np.array([3, 8, 1, 10, 5])  # Tạo mảng NumPy với các điểm y

plt.plot(ypoints, marker='o')  # Vẽ biểu đồ với marker là hình tròn
plt.title('Marker Example')  # Thêm tiêu đề cho biểu đồ 
plt.show()  # Hiển thị biểu đồ

# Bạn có thể thay đổi kiểu marker bằng cách sử dụng các ký hiệu khác nhau như 's' cho hình vuông, '^' cho hình tam giác, v.v.
# Ví dụ:
x = [1, 2, 3, 4, 5]  # Tạo danh sách các điểm x
y = [10, 15, 13, 17, 20]  # Tạo danh sách các điểm y
plt.plot(x, y, marker='o', color='r', linestyle='-', label='Circle Marker')  # Vẽ biểu đồ với marker là hình tròn
plt.plot(x, y, marker='s', color='g', linestyle='-', label='Square Marker')  # Vẽ biểu đồ với marker là hình vuông
plt.plot(x, y, marker='^', color='b', linestyle='-', label='Triangle Marker')  # Vẽ biểu đồ với marker là hình tam giác
plt.plot(x, y, marker='*', color='m', linestyle='-', label='Star Marker')  # Vẽ biểu đồ với marker là hình sao
plt.xlabel('X-axis')  # Thêm nhãn cho trục x
plt.ylabel('Y-axis')  # Thêm nhãn cho trục y
plt.legend()  # Hiển thị chú thích cho biểu đồ
plt.title('Basic Marker Example')  # Thêm tiêu đề cho biểu đồ
plt.show()  # Hiển thị biểu đồ