# Import hàm random từ numpy để tạo dữ liệu ngẫu nhiên
from numpy import random

# -----------------------------
# Tạo mẫu ngẫu nhiên có trọng số (xác suất) từ một tập giá trị cho trước
# -----------------------------

# random.choice lấy mẫu ngẫu nhiên từ danh sách [5, 6, 9, 8]
# p=[0.5, 0.2, 0.2, 0.1]: xác suất chọn mỗi phần tử tương ứng
# size=100: tạo mảng 1 chiều gồm 100 phần tử
x = random.choice([5, 6, 9, 8], p=[0.5, 0.2, 0.2, 0.1], size=(100))

# Tương tự nhưng tạo mảng 2 chiều kích thước 3x5
x1 = random.choice([5, 6, 9, 8], p=[0.5, 0.2, 0.2, 0.1], size=(3, 5))

# In ra kết quả
print(x)
print(x1)
