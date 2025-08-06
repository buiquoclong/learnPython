# Import hàm random từ numpy để tạo dữ liệu ngẫu nhiên
from numpy import random

# Import matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# Import seaborn để trực quan hóa dễ dàng hơn
import seaborn as sns

# ----------------------------------------
# Tạo dữ liệu phân phối exponential và vẽ đường mật độ (KDE)
# ----------------------------------------

# random.exponential tạo dữ liệu theo phân phối mũ (exponential distribution)
# size=1000 nghĩa là tạo 1000 mẫu dữ liệu

# sns.distplot vẽ biểu đồ mật độ (kde) của dữ liệu
# hist=False để không hiển thị histogram mà chỉ hiển thị đường mật độ
# label="exponential" để đặt tên cho đường biểu diễn (dùng cho legend)

sns.distplot(random.exponential(size=1000), hist=False, label="exponential")

# Hiển thị biểu đồ
plt.show()
