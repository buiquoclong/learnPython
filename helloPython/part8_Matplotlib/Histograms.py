# Histograms là biểu đồ tần suất, thường được sử dụng để trực quan hóa phân phối của một tập hợp dữ liệu.
# Thêm thư viện Matplotlib để vẽ biểu đồ tần suất
import matplotlib.pyplot as plt

# Ví dụ 1
# Tạo dữ liệu để vẽ biểu đồ tần suất
plt.subplot(1, 2, 1)  # Tạo một biểu đồ đơn giản với một lưới
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]  # Tạo danh sách dữ liệu để vẽ biểu đồ tần suất
plt.hist(data, bins=5, color='blue', alpha=0.7, edgecolor='black')  # Vẽ biểu đồ tần suất với dữ liệu, 
# số lượng bins, màu sắc, độ trong suốt và màu viền
# bins là số lượng khoảng giá trị mà dữ liệu sẽ được chia thành, giúp xác định độ chi tiết của biểu đồ.
plt.title('Histogram Example')  # Thêm tiêu đề cho biểu đồ
plt.xlabel('Value')  # Thêm nhãn cho trục x
plt.ylabel('Frequency')  # Thêm nhãn cho trục y
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Hiển thị lưới trên trục y để dễ dàng đọc giá trị
# Biểu đồ tần suất giúp người xem dễ dàng nhận ra phân phối của dữ liệu, từ đó đưa ra những phân tích và kết luận về dữ liệu.

# Ví dụ 2
import numpy as np
plt.subplot(1, 2, 2)  # Tạo một biểu đồ đơn giản với một lưới khác
# Tạo dữ liệu ngẫu nhiên để vẽ biểu đồ tần suất
x = np.random.normal(170, 10, 1025000)  # Tạo dữ liệu ngẫu nhiên với phân phối chuẩn, 
# có nghĩa là trung bình 170 và độ lệch chuẩn 10, với 1.025.000 mẫu
plt.hist(x, bins=100, color='green', alpha=0.7, edgecolor='black')  # Vẽ biểu đồ tần suất với dữ liệu ngẫu nhiên
plt.title('Histogram Example 1')  # Thêm tiêu đề cho biểu đồ
plt.xlabel('Value')  # Thêm nhãn cho trục x
plt.ylabel('Frequency')  # Thêm nhãn cho trục y
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Hiển thị lưới trên trục y để dễ dàng đọc giá trị
plt.show()  # Hiển thị biểu đồ tần suất