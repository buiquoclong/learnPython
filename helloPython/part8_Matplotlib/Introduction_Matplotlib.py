# Matplotlib là một thư viện mạnh mẽ trong Python dùng để vẽ đồ thị và biểu đồ.
# Nó cho phép bạn tạo ra các biểu đồ 2D và 3D với nhiều tùy chỉnh.

# Import thư viện matplotlib.pyplot 
import matplotlib.pyplot as plt

# Khởi tạo dữ liệu để vẽ biểu đồ
# Dữ liệu này có thể là danh sách các giá trị hoặc mảng NumPy.  
x = [1, 2, 3, 4, 5] 
y = [10, 15, 13, 17, 20]
# Vẽ biểu đồ đường
plt.plot(x, y, marker='o', color='b', linestyle='--', label = 'My Line')
# marker là kiểu đánh dấu điểm dữ liệu, color là màu đường, linestyle là kiểu đường, label là nhãn cho đường.
# 'o' là hình tròn, 'b' là màu xanh dương, '-' là đường liền, '--' là đường đứt nét.
# Thêm tiêu đề và nhãn trục
plt.title('Simple Line Plot')
plt.xlabel('X-axis label') # X-axis là trục hoành, label là nhãn cho trục.
plt.ylabel('Y-axis label') # Y-axis là trục tung, label là nhãn cho trục.
plt.legend()  # Hiển thị chú thích cho biểu đồ
# Hiển thị chú thích bên trái 
plt.grid(True)  # Hiển thị lưới trên biểu đồ để dễ dàng đọc giá trị
# Hiển thị biểu đồ
plt.show()
# Bạn có thể tùy chỉnh biểu đồ bằng cách thay đổi màu sắc, kiểu đường, và thêm chú thích.
# Matplotlib hỗ trợ nhiều loại biểu đồ khác nhau như biểu đồ cột, biểu đồ tròn, biểu đồ phân tán, v.v.