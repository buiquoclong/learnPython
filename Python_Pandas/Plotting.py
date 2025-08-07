# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Nhập thư viện matplotlib để vẽ biểu đồ
import matplotlib.pyplot as plt

# ----------- Phần 1: Biểu đồ phân tán (scatter plot) -----------

# Tạo dữ liệu biểu diễn mối quan hệ giữa 2 biến X và Y
data_relationship = {
    "X": [1, 2, 3, 4, 5],    # Trục hoành
    "Y": [5, 7, 9, 11, 13]   # Trục tung (có vẻ là Y = 2X + 3)
}

# Tạo DataFrame từ dữ liệu
df_relationships = pd.DataFrame(data_relationship)

# Vẽ biểu đồ phân tán giữa X và Y
df_relationships.plot(x="X", y="Y", kind="scatter")

# Thiết lập nhãn trục và tiêu đề
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot")
# plt.show()  # Đã tạm thời ẩn hiển thị biểu đồ này

# ----------- Phần 2: Biểu đồ phân phối (histogram) -----------

# Tạo dữ liệu cho biểu đồ histogram
data_distribution = {
    "Values": [3, 4, 5, 6, 9, 10, 12, 15, 17, 20, 25, 30]
}

# Tạo DataFrame từ dữ liệu phân phối
df_distribution = pd.DataFrame(data_distribution)

# Vẽ biểu đồ histogram với 5 bins (khoảng)
df_distribution["Values"].plot(kind="hist", bins=5)

# Thiết lập nhãn trục và tiêu đề
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Distribution Histogram")

# Hiển thị biểu đồ
plt.show()
