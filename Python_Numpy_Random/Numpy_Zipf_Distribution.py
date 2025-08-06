# Import hàm tạo số ngẫu nhiên từ numpy
from numpy import random

# Import matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# Import seaborn để vẽ biểu đồ dễ dàng hơn
import seaborn as sns

# ---------------------------
# Tạo dữ liệu phân phối Zipf và vẽ histogram
# ---------------------------

# random.zipf tạo dữ liệu theo phân phối Zipf với tham số a=2
# size=(3,4): tạo mảng kích thước 3x4

x = random.zipf(a=2, size=(3, 4))

# In dữ liệu nếu muốn (đang bị comment)
# print(x)

# Vì phân phối Zipf có thể tạo ra giá trị rất lớn,
# ta chỉ lấy các giá trị nhỏ hơn 10 để biểu diễn rõ hơn trên biểu đồ
# kde=False để chỉ vẽ histogram, không vẽ đường mật độ

sns.distplot(x[x < 10], kde=False)

# Hiển thị biểu đồ
plt.show()
