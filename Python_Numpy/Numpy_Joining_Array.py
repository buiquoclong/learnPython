# Import thư viện numpy với tên viết tắt là np
import numpy as np

# Tạo một mảng 2 chiều (2 hàng, 3 cột)
array = np.array([[10, 20, 30], 
                  [40, 45, 47]])

# Tạo hai mảng 1 chiều có cùng số phần tử
array1 = np.array([50, 60, 70])
array2 = np.array([80, 90, 100])

# -------------------------
# NỐI THEO CHIỀU NGANG (HORIZONTAL STACKING)
# -------------------------

# Nối array1 và array2 theo chiều ngang (tạo ra 1 mảng 1 chiều mới)
result1 = np.hstack((array1, array2))
print(result1)
# Kết quả: [ 50  60  70  80  90 100]

# -------------------------
# NỐI THEO CHIỀU DỌC (VERTICAL STACKING)
# -------------------------

# Nối array1 và array2 theo chiều dọc (tạo ra mảng 2D, mỗi mảng là 1 hàng)
result2 = np.vstack((array1, array2))
print(result2)
# Kết quả: 
# [[ 50  60  70]
#  [ 80  90 100]]

# -------------------------
# CONCATENATE (GHÉP MẢNG LINH HOẠT)
# -------------------------

# Ghép array1 và array2 theo chiều mặc định là axis=0 (giống hstack nếu là 1D)
result3 = np.concatenate((array1, array2))
print(result3)
# Kết quả: [ 50  60  70  80  90 100]

# -------------------------
# NỐI MẢNG 1D VÀO MẢNG 2D THEO CHIỀU DỌC
# -------------------------

# Nối array1 vào array (array1 sẽ trở thành 1 hàng mới, nên phải cùng số cột)
result4 = np.vstack((array, array1))
print(result4)
# Kết quả:
# [[10 20 30]
#  [40 45 47]
#  [50 60 70]]
