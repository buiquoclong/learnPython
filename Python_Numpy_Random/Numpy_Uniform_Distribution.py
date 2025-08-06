# Import thư viện tạo số ngẫu nhiên
from numpy import random

# Import matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# Import seaborn để trực quan hóa dữ liệu dễ dàng hơn
import seaborn as sns

# ------------------------------
# Tạo dữ liệu phân phối đồng đều (uniform distribution) và vẽ đường mật độ (KDE)
# ------------------------------

# random.uniform tạo dữ liệu phân phối đều từ 0 đến 1 (mặc định)
# size=1000 nghĩa là tạo 1000 mẫu dữ liệu

# sns.distplot vẽ biểu đồ mật độ xác suất (KDE)
# hist=False để không vẽ histogram mà chỉ hiển thị đường mật độ

sns.distplot(random.uniform(size=1000), hist=False)

# Hiển thị biểu đồ
plt.show()
