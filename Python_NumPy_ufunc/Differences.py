import numpy as np

# Tạo mảng 1 chiều
data_array = np.array([10, 20, 30, 40, 50, 60])

# Tính hiệu số giữa các phần tử liền kề trong mảng
diff_result = np.diff(data_array)
print("Difference: ", diff_result)
# Kết quả: [10 10 10 10 10] vì 20-10=10, 30-20=10,...

# Tính hiệu số theo chiều (axis) 0
# Với mảng 1 chiều thì tương tự như trên
axis_diff_result = np.diff(data_array, axis=0)
print("Difference along axis: ", axis_diff_result)

# Tạo mảng mới để thử tính hiệu số bậc 2
array = np.array([10, 50, 25, 56, 90])

# np.diff với n=2 tính hiệu số bậc 2 (lấy hiệu của hiệu)
new_array = np.diff(array, n=2)
print(new_array)
# Ví dụ: hiệu bậc 1: [40, -25, 31, 34]
# Hiệu bậc 2: [-65, 56, 3]
