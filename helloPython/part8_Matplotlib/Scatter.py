# Scatter là quá trình vẽ biểu đồ phân tán để trực quan hóa mối quan hệ giữa hai biến.

# Thêm thư viện Matplotlib để vẽ biểu đồ phân tán
import matplotlib.pyplot as plt

# Tạo dữ liệu để vẽ biểu đồ phân tán
x = [2, 4, 5, 7, 8]  # Tạo danh sách các điểm x
y = [10, 15, 20, 25, 30]  # Tạo danh sách các điểm y

plt.scatter(x, y, color='blue', marker='o', label='Data Points', s=100, edgecolor='black')  # Vẽ biểu đồ phân tán với các điểm x và y,
# color là màu của điểm, marker là kiểu đánh dấu điểm, label là nhãn cho điểm, s là kích thước điểm, edgecolor là màu viền của điểm
plt.title('Scatter Plot Example')  # Thêm tiêu đề cho biểu đồ
plt.xlabel('X-axis')  # Thêm nhãn cho trục x
plt.ylabel('Y-axis')  # Thêm nhãn cho trục y
plt.legend()  # Hiển thị chú thích cho biểu đồ
plt.grid(linestyle= '--')  # Hiển thị lưới trên biểu đồ để dễ dàng đọc
plt.show()  # Hiển thị biểu đồ phân tán
# Biểu đồ phân tán giúp người xem dễ dàng nhận ra mối quan hệ giữa các biến x và y, từ đó đưa ra những phân tích và kết luận về dữ liệu.