# Line là một loại biểu đồ trong Matplotlib dùng để hiển thị mối quan hệ giữa hai biến số bằng cách nối các điểm dữ liệu bằng đường thẳng.
# Biểu đồ đường thường được sử dụng để hiển thị xu hướng theo thời gian hoặc để so sánh các tập dữ liệu khác nhau.

# Import thư viện matplotlib.pyplot
import matplotlib.pyplot as plt

# Khởi tạo dữ liệu để vẽ biểu đồ
x = [1, 2, 3, 4, 5]  # Tạo danh sách các điểm x
y = [10, 15, 25, 30, 20]  # Tạo danh sách các điểm y
y2 = [5, 10, 15, 20, 25]  # Tạo danh sách các điểm y khác để so sánh

plt.plot(x, y, marker='o', color='b', linestyle='-', label='Data Line')  # Vẽ biểu đồ đường với các điểm x và y
plt.plot(x, y2, marker='o', color='g', linestyle='--', label='Data Line 1')  # Vẽ biểu đồ đường với các điểm x và y


plt.title('Line Plot Example')  # Thêm tiêu đề cho biểu đồ

plt.xlabel('X-axis')  # Thêm nhãn cho trục x
plt.ylabel('Y-axis')  # Thêm nhãn cho trục y
plt.legend()  # Hiển thị chú thích cho biểu đồ
plt.grid(True)  # Hiển thị lưới trên biểu đồ để dễ dàng đọc
plt.show()  # Hiển thị biểu đồ