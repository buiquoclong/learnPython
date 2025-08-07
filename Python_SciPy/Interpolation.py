# Nhập các hàm nội suy từ thư viện scipy và numpy để tạo dữ liệu ví dụ
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf
import numpy as np

# Tạo dữ liệu mẫu: xs từ 0 đến 9, ys theo hàm y = 2x + 1
xs = np.arange(10)
ys = 2 * xs + 1

# Tạo hàm nội suy dạng tuyến tính 1 chiều dựa trên dữ liệu xs, ys
interp_func = interp1d(xs, ys)

# Sử dụng hàm nội suy để tính giá trị tại các điểm mới nằm giữa xs
# np.arange(2.1, 3, 0.1) tạo các điểm từ 2.1 đến 2.9 với bước 0.1
new_array = interp_func(np.arange(2.1, 3, 0.1))
print(new_array)  # In ra giá trị nội suy tại các điểm mới

# Tạo dữ liệu phức tạp hơn: ys1 là hàm của xs gồm bình phương và sin(x)
ys1 = xs**2 + np.sin(xs) + 1

# Tạo hàm nội suy spline bậc nhất (UnivariateSpline) cho dữ liệu xs, ys1
interp_func1 = UnivariateSpline(xs, ys1)

# Nội suy spline trên các điểm mới từ 2.1 đến 2.9 với bước 0.1
new_array1 = interp_func1(np.arange(2.1, 3, 0.1))
print(new_array1)  # In ra kết quả nội suy spline

# Tạo hàm nội suy RBF (Radial Basis Function) cho dữ liệu xs, ys1
interp_func2 = Rbf(xs, ys1)

# Nội suy RBF tại các điểm mới từ 2.1 đến 2.9 với bước 0.1
new_array2 = interp_func2(np.arange(2.1, 3, 0.1))
print(new_array2)  # In ra kết quả nội suy RBF
