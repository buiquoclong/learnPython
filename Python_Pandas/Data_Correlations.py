# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Nhập thư viện seaborn để trực quan hóa dữ liệu, đặc biệt là heatmap
import seaborn as sns

# Nhập matplotlib.pyplot để hiển thị biểu đồ
import matplotlib.pyplot as plt

# Tạo một DataFrame với 3 cột: Age (tuổi), Income (thu nhập), Expenses (chi tiêu)
data = {
    "Age": [25, 30, 35, 40, 45],             # Tuổi của cá nhân
    "Income": [25000, 30000, 35000, 60000, 70000],  # Thu nhập
    "Expenses": [23000, 20000, 15000, 14000, 40000] # Chi tiêu
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Tính ma trận tương quan giữa các cột số trong DataFrame
correlation_matrix = df.corr()
print("correlation matrix: ")
print(correlation_matrix)  # In ra ma trận tương quan

# Vẽ biểu đồ heatmap để biểu diễn ma trận tương quan
sns.heatmap(
    correlation_matrix,      # Ma trận tương quan
    annot=True,              # Hiển thị giá trị số trên các ô
    cmap="coolwarm",         # Bảng màu thể hiện độ tương quan (màu nóng/lạnh)
    linewidths=0.5           # Độ rộng đường kẻ giữa các ô
)

# Đặt tiêu đề cho biểu đồ
plt.title("Correlation Heatmap")

# Hiển thị biểu đồ ra màn hình
plt.show()
