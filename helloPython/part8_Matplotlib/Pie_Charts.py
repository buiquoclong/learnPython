# Pie chart là một loại biểu đồ hình tròn được sử dụng để thể hiện tỷ lệ phần trăm của các phần trong một tổng thể.
# Sử dụng Matplotlib để tạo biểu đồ hình tròn
import matplotlib.pyplot as plt
import numpy as np  
# Dữ liệu để vẽ biểu đồ hình tròn
y = np.array([35, 25, 25, 15])  # Tạo mảng NumPy với các giá trị phần trăm
labels = ['A', 'B', 'C', 'D']  # Nhãn cho các phần của biểu đồ
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']  # Màu sắc cho các phần của biểu đồ
explode = (0.1, 0, 0, 0)  # Tạo hiệu ứng tách phần đầu tiên ra khỏi biểu đồ, có nghĩa là phần A sẽ được tách ra một chút
plt.pie(y, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
# plt.pie() là hàm để vẽ biểu đồ hình tròn
# y là dữ liệu phần trăm, explode là hiệu ứng tách phần, labels là nhãn cho các phần, colors là màu sắc của các phần,
# autopct là định dạng hiển thị phần trăm, shadow là hiệu ứng bóng đổ, startangle là góc bắt đầu vẽ biểu đồ
plt.axis('equal')  # Đảm bảo biểu đồ hình tròn được vẽ đúng tỷ lệ
plt.title('Pie Chart Example')  # Thêm tiêu đề cho biểu đồ
plt.legend()  # Hiển thị chú thích cho biểu đồ
plt.show()  # Hiển thị biểu đồ hình tròn
# Biểu đồ hình tròn thường được sử dụng để hiển thị tỷ lệ phần trăm của các phần trong một tổng thể,
# giúp người xem dễ dàng nhận biết tỷ lệ của từng phần so với tổng thể.
