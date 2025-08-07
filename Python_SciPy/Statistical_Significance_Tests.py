import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import describe

# Tạo 3 mảng dữ liệu giả định, lấy mẫu từ phân phối chuẩn (normal)
v = np.random.normal(size=100)
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

# Kiểm định t-test độc lập (two-sample t-test)
# So sánh trung bình của v1 và v2 xem có khác biệt có ý nghĩa thống kê không
res = ttest_ind(v1, v2)
print(res)  # In kết quả kiểm định t-test

# Kiểm định Kolmogorov-Smirnov
# So sánh phân phối dữ liệu v với phân phối chuẩn ("norm")
res1 = kstest(v, "norm")
print(res1)  # In kết quả kiểm định K-S

# Mô tả các đặc trưng thống kê cơ bản của dữ liệu v
# Trả về số lượng mẫu, trung bình, độ lệch chuẩn, min, max, skewness, kurtosis
res2 = describe(v)
print(res2)
