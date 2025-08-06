# Import thư viện numpy với tên viết tắt là np
import numpy as np

# Tạo một mảng 1 chiều gồm 6 phần tử
original_array = np.array([1, 2, 3, 4, 5, 6])

# Tạo một mảng 2 chiều 3x3
original_array1 = np.array([[1, 2, 3], 
                            [4, 5, 6], 
                            [7, 8, 9]])

# Tạo một mảng 1 chiều gồm 9 phần tử
original_array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# -------------------------------
# CHIA MẢNG THÀNH CÁC PHẦN BẰNG NHAU (EQUAL SPLIT)
# -------------------------------

# Chia original_array thành 3 phần bằng nhau
result = np.split(original_array, 3)
print(result)
# Kết quả: [array([1, 2]), array([3, 4]), array([5, 6])]

# -------------------------------
# CHIA MẢNG TẠI CÁC CHỈ SỐ CHỈ ĐỊNH (CUSTOM SPLIT POINTS)
# -------------------------------

# Chia mảng tại các vị trí chỉ định [2, 4] → tạo 3 đoạn: [0:2], [2:4], [4:]
result1 = np.split(original_array, [2, 4])
print(result1)
# Kết quả: [array([1, 2]), array([3, 4]), array([5, 6])]

# -------------------------------
# CHIA MẢNG 2D THEO CHIỀU CỘT (axis=1)
# -------------------------------

# Chia mảng 2D thành 3 phần theo cột (mỗi phần 1 cột)
result2 = np.split(original_array1, 3, axis=1)
print(result2)
# Kết quả:
# [array([[1],
#         [4],
#         [7]]),
#  array([[2],
#         [5],
#         [8]]),
#  array([[3],
#         [6],
#         [9]])]

# -------------------------------
# CHIA MẢNG VỚI KÍCH THƯỚC KHÔNG ĐỀU (array_split)
# -------------------------------

# np.array_split cho phép chia mảng tại các chỉ số ngay cả khi không chia đều được
result3 = np.array_split(original_array2, [2, 5])
print(result3)
# Kết quả: [array([1, 2]), array([3, 4, 5]), array([6, 7, 8, 9])]
