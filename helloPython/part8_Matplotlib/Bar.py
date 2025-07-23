# Bar trong python là một loại biểu đồ được sử dụng để hiển thị dữ liệu theo dạng cột hoặc thanh, 
# thường được sử dụng để so sánh các giá trị khác nhau.
# Biểu đồ cột thường được sử dụng để hiển thị số lượng, tần suất hoặc các giá trị khác nhau trong các danh mục.
# Import thư viện matplotlib.pyplot
import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C']  # Tạo danh sách các danh mục
values = [10, 15, 7]  # Tạo danh sách các giá trị tương ứng với các danh mục

plt.bar(categories, values, color=['orange', 'blue', 'pink'], edgecolor= 'black', alpha=0.7)  # Vẽ biểu đồ cột với các danh mục và giá trị
# color là màu của cột, có thể sử dụng danh sách màu sắc để tùy chỉnh màu sắc của từng cột,
# edgecolor là màu viền của cột, alpha là độ trong suốt của cột
plt.title('Bar Chart Example')  # Thêm tiêu đề cho biểu đồ
plt.xlabel('Categories')  # Thêm nhãn cho trục x
plt.ylabel('Values')  # Thêm nhãn cho trục y
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Hiển thị lưới trên trục y để dễ dàng đọc giá trị
plt.show()  # Hiển thị biểu đồ cột
