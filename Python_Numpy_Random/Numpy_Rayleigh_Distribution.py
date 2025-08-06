# Import thư viện tạo số ngẫu nhiên
from numpy import random

# Import matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# Import seaborn để trực quan hóa dữ liệu
import seaborn as sns

# ------------------------------
# Tạo dữ liệu phân phối Rayleigh và vẽ đường mật độ xác suất (KDE)
# ------------------------------

# random.rayleigh tạo dữ liệu theo phân phối Rayleigh
# size=1000 nghĩa là tạo 1000 mẫu dữ liệu

# sns.distplot vẽ biểu đồ mật độ (KDE) của dữ liệu
# hist=False để không hiển thị histogram mà chỉ hiển thị đường mật độ

sns.distplot(random.rayleigh(size=1000), hist=False)

# Hiển thị biểu đồ
plt.show()
