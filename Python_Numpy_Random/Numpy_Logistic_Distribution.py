# Import các thư viện cần thiết
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------
# Tạo dữ liệu phân phối logistic và normal, vẽ biểu đồ mật độ (KDE)
# --------------------------------------

# random.normal tạo dữ liệu phân phối chuẩn (normal distribution)
# scale=2 là độ lệch chuẩn, size=1000 là số lượng mẫu

# random.logistic tạo dữ liệu phân phối logistic với các tham số mặc định (loc=0, scale=1)

# sns.distplot dùng để vẽ đường mật độ xác suất (KDE)
# hist=False để không hiển thị histogram
# label dùng để đặt tên đường biểu diễn

sns.distplot(random.normal(scale=2, size=1000), hist=False, label="normal")
sns.distplot(random.logistic(size=1000), hist=False, label="logistic")

# Hiển thị biểu đồ
plt.show()
