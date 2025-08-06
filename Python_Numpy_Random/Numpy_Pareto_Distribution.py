# Import thư viện tạo số ngẫu nhiên
from numpy import random

# Import matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# -----------------------------------------
# Tạo dữ liệu phân phối Pareto và vẽ histogram
# -----------------------------------------

# Tham số shape (a) của phân phối Pareto
shape_parameter = 2.5

# Tạo 1000 mẫu dữ liệu theo phân phối Pareto với tham số shape = 2.5
data = random.pareto(shape_parameter, size=1000)

# Vẽ biểu đồ histogram với:
# bins=50: chia thành 50 cột
# density=True: chuẩn hóa histogram thành mật độ xác suất
# color="purple": màu cột là tím
plt.hist(data, bins=50, density=True, color="purple")

# Hiển thị biểu đồ
plt.show()
