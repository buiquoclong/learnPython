# Import thư viện numpy để sinh dữ liệu ngẫu nhiên
import numpy as np

# Import matplotlib để hiển thị biểu đồ
import matplotlib.pyplot as plt

# Import seaborn để trực quan hóa dữ liệu dễ dàng hơn
import seaborn as sns

# -----------------------------
# VẼ PHÂN PHỐI LIÊN TỤC (Normal Distribution)
# -----------------------------

# sns.distplot đã bị deprecated trong Seaborn ≥ 0.11, nên bạn có thể dùng kdeplot/histplot thay thế
# Nhưng trong ví dụ này vẫn minh họa cách dùng distplot (với hist=False để chỉ vẽ đường KDE)

# Tạo dữ liệu theo phân phối chuẩn (normal distribution)
# loc=50: giá trị trung bình (mean)
# scale=5: độ lệch chuẩn (standard deviation)
# size=1000: số lượng mẫu
sns.distplot(np.random.normal(loc=50, scale=5, size=1000), 
             hist=False,   # không vẽ histogram, chỉ vẽ đường KDE
             label="normal")

# -----------------------------
# VẼ PHÂN PHỐI RỜI RẠC (Binomial Distribution)
# -----------------------------

# Tạo dữ liệu theo phân phối nhị thức (binomial)
# n=100: số lần thử
# p=0.5: xác suất thành công mỗi lần thử
# size=1000: số lượng mẫu
sns.distplot(np.random.binomial(n=100, p=0.5, size=1000), 
             hist=False, 
             label="binomial")

# -----------------------------
# HIỂN THỊ BIỂU ĐỒ
# -----------------------------
plt.show()
