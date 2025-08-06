# Import thư viện tạo số ngẫu nhiên, vẽ biểu đồ
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Tạo dữ liệu ngẫu nhiên theo phân phối chuẩn (normal distribution)
# ------------------------------

# Tạo mảng 2x3 với các giá trị ngẫu nhiên theo phân phối chuẩn chuẩn (mean=0, std=1)
x = random.normal(size=(2, 3))

# Tạo mảng 2x3 với phân phối chuẩn có mean=1, std=2
x1 = random.normal(loc=1, scale=2, size=(2, 3))

# In ra màn hình 2 mảng dữ liệu vừa tạo
print(x)
print(x1)

# ------------------------------
# Vẽ biểu đồ mật độ (KDE) cho dữ liệu phân phối chuẩn 1 chiều (1000 mẫu)
# hist=False để chỉ vẽ đường mật độ, không hiển thị histogram
sns.distplot(random.normal(size=1000), hist=False)

# Hiển thị biểu đồ
plt.show()
