import numpy as np

# Tạo mảng 1 chiều với các số nguyên
data_array = np.array([10, 20, 30, 40, 50])

# Tính tổng tất cả phần tử trong mảng
sum_result = np.sum(data_array)
print("Summation result: ", sum_result)
# Kết quả: 150

# Tính tổng theo một trục (axis=0), ở đây mảng 1 chiều nên tương đương với tổng toàn bộ
axis_sum_result = np.sum(data_array, axis=0)
print("Summation axis: ", axis_sum_result)
# Kết quả: 150

# Tạo mảng khác
array = np.array([1, 2, 3, 4, 5])

# Tính tổng tích lũy (cumulative sum), tức là phần tử thứ i là tổng các phần tử từ đầu đến i
new_array = np.cumsum(array)
print(new_array)
# Kết quả: [ 1  3  6 10 15]
