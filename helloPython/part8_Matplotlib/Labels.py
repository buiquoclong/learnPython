# Label là quá trình thêm nhãn cho các trục, tiêu đề và chú thích trong biểu đồ để làm rõ ý nghĩa của dữ liệu.

# Thêm thư viện matplotlib.pyplot
import matplotlib.pyplot as plt

# Khởi tạo dữ liệu để vẽ biểu đồ
x = [1, 2, 3, 4, 5]  # Tạo danh sách các điểm x
y = [10, 15, 20, 25, 30]  # Tạo danh sách các điểm y
y2 = [5, 10, 15, 20, 25]  # Tạo danh sách các điểm y khác để so sánh

plt.plot(x, y, marker='o', color='b', linestyle='-', label='Data Line')  # Vẽ biểu đồ đường với các điểm x và y
plt.plot(x, y2, marker='s', color='g', linestyle='--', label='Data Line 1')  # Vẽ biểu đồ đường với các điểm x và y2

plt.title('Label Example')  # Thêm tiêu đề cho biểu đồ
plt.xlabel('X-axis')  # Thêm nhãn cho trục x
plt.ylabel('Y-axis')  # Thêm nhãn cho trục y
plt.legend(loc="upper left", fontsize=12, frameon= False)  # Hiển thị chú thích cho biểu đồ, loc là vị trí của chú thích, fontsize là kích thước chữ, frameon là hiển thị khung hay không
# Có thể tùy chỉnh vị trí của chú thích bằng cách sử dụng các giá trị như 'upper left', 'upper right', 'lower left', 'lower right', 'center', v.v.
# Có thể thay đổi kích thước chữ và hiển thị khung cho chú thích.
plt.grid(True)  # Hiển thị lưới trên biểu đồ để dễ dàng đọc
plt.show()  # Hiển thị biểu đồ