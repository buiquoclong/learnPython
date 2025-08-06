# Import thư viện vẽ biểu đồ
import matplotlib.pyplot as plt
import seaborn as sns

# Vẽ đường mật độ xác suất (KDE) cho dữ liệu rời rạc [0,1,2,3,4,5]
# hist=False để không vẽ histogram, chỉ vẽ đường KDE
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

# Hiển thị biểu đồ
plt.show()  # Thêm dấu ngoặc () để gọi hàm plt.show đúng cách
