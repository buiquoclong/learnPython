# Import thư viện tạo số ngẫu nhiên
from numpy import random

# Import matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# Import seaborn để trực quan hóa dữ liệu dễ dàng hơn
import seaborn as sns

# -------------------------------
# Tạo dữ liệu phân phối Normal và Poisson và vẽ biểu đồ mật độ (KDE)
# -------------------------------

# Tạo dữ liệu phân phối chuẩn (normal distribution)
# loc=50: trung bình, scale=7: độ lệch chuẩn, size=1000: số mẫu
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label="normal")

# Tạo dữ liệu phân phối Poisson (rời rạc)
# lam=50 là tham số lambda (trung bình số sự kiện trên đơn vị thời gian), size=1000 mẫu
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label="poisson")

# Hiển thị biểu đồ
plt.show()
