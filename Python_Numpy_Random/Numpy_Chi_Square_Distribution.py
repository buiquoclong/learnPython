# Import hàm random từ thư viện numpy để tạo dữ liệu ngẫu nhiên
from numpy import random

# Import matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# -------------------------------
# Tạo dữ liệu phân phối Chi-square
# -------------------------------

# Độ tự do (degrees of freedom) của phân phối Chi-square
degrees_of_freedom = 3

# Tạo 1000 mẫu dữ liệu phân phối Chi-square với độ tự do 3
data = random.chisquare(degrees_of_freedom, size=1000)

# -------------------------------
# Vẽ biểu đồ histogram của dữ liệu
# -------------------------------

# plt.hist dùng để vẽ biểu đồ histogram
# bins=50: chia thành 50 cột
# density=True: chuẩn hóa histogram thành mật độ xác suất (area dưới biểu đồ = 1)
# color="black": màu cột histogram là màu đen
plt.hist(data, bins=50, density=True, color="black")

# Hiển thị biểu đồ
plt.show()
