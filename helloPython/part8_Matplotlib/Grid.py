# Grid là quá trình tạo lưới trong biểu đồ để giúp người xem dễ dàng đọc và phân tích dữ liệu.

# Thêm thư viện Matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]  # Tạo danh sách các điểm x
y = [10, 15, 20, 25, 30]  # Tạo danh sách các điểm y

# Vẽ biểu đồ thứ nhất với lưới
plt.subplot(1, 2, 1)  # Tạo một biểu đồ đơn giản với một lưới
# subplot(1, 2, 1) có nghĩa là tạo một lưới với 1 hàng và 2 cột, và đây là biểu đồ đầu tiên trong lưới.

plt.plot(x, y, marker='o', color='b', linestyle='-', label='Data Line')  # Vẽ biểu đồ đường với các điểm x và y
plt.title('Grid Example')  # Thêm tiêu đề cho biểu đồ
plt.xlabel('X-axis')  # Thêm nhãn cho trục x
plt.ylabel('Y-axis')  # Thêm nhãn cho trục y
plt.legend()  # Hiển thị chú thích cho biểu đồ
plt.grid(color="gray", linestyle= '--', linewidth=0.5)  # Hiển thị lưới trên biểu đồ để dễ dàng đọc, color là màu của lưới, 
# linestyle là kiểu đường lưới, linewidth là độ dày của đường lưới
# Có thể tùy chỉnh màu sắc, kiểu đường và độ dày của lưới theo ý muốn.
# Vẽ biểu đồ thứ hai 
plt.subplot(1, 2, 2)  # Tạo một biểu đồ đơn giản với một lưới khác
# subplot(1, 2, 2) có nghĩa là tạo một lưới với 1 hàng và 2 cột, và đây là biểu đồ thứ hai trong lưới.
plt.plot(x, [i**2 for i in y], marker='s', color='g', linestyle='-', label='Data Line 1')  # Vẽ biểu đồ đường với các điểm x và y
plt.title('Grid Example 1')  # Thêm tiêu đề cho biểu đồ
plt.xlabel('X-axis')  # Thêm nhãn cho trục x
plt.ylabel('Y-axis')  # Thêm nhãn cho trục y
plt.legend()  # Hiển thị chú thích cho biểu đồ
plt.grid(color="gray", linestyle= '-', linewidth=0.5) 
plt.show()  # Hiển thị biểu đồ