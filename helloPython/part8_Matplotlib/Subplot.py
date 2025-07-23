# Subplot là quá trình tạo nhiều biểu đồ trong cùng một hình vẽ để so sánh hoặc hiển thị dữ liệu khác nhau.

# Sử dụng Matplotlib để tạo subplot
import matplotlib.pyplot as plt

# Tạo một hình vẽ với nhiều biểu đồ con
# Tạo biểu đồ thứ nhất với lưới 2x2
plt.subplot(2, 2, 1)  # Tạo một lưới 2x2 và chọn ô đầu tiên
plt.plot([1, 2, 3], [4, 5, 6], marker='o', color='b', linestyle='-', label='Line 1')  # Vẽ biểu đồ đường
plt.title('Subplot 1')  # Thêm tiêu đề cho biểu đồ 

# Tao biểu đồ thứ hai
plt.subplot(2, 2, 2)  # Chọn ô thứ hai trong lưới
plt.plot([1, 2, 3], [6, 5, 4], marker='s', color='g', linestyle='--', label='Line 2')  # Vẽ biểu đồ đường khác
plt.title('Subplot 2')  # Thêm tiêu đề cho biểu đồ

# Tạo biểu đồ thứ ba
plt.subplot(2, 2, 3)  # Chọn ô thứ ba trong lưới
plt.plot([1, 2, 3], [4, 6, 5], marker='^', color='r', linestyle=':', label='Line 3')  # Vẽ biểu đồ đường khác
plt.title('Subplot 3')  # Thêm tiêu đề cho biểu đồ

# Tạo biểu đồ thứ tư
plt.subplot(2, 2, 4)  # Chọn ô thứ tư trong lưới
plt.plot([1, 2, 3], [5, 4, 6], marker='*', color='m', linestyle='-.', label='Line 4')  # Vẽ biểu đồ đường khác
plt.title('Subplot 4')  # Thêm tiêu đề cho biểu đồ

plt.tight_layout()  # Tự động điều chỉnh khoảng cách giữa các biểu đồ, giúp tránh chồng lấn tiêu đề và nhãn trục
plt.show()  # Hiển thị tất cả các biểu đồ trong cùng một hình vẽ