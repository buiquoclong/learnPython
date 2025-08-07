import numpy as np

# Định nghĩa hàm cộng 2 số
def myadd(x, y):
    return x + y

# Chuyển hàm myadd thành một ufunc của numpy
# np.frompyfunc nhận vào:
# - hàm Python (myadd)
# - số lượng tham số đầu vào (2)
# - số lượng giá trị trả về (1)
myadd = np.frompyfunc(myadd, 2, 1)

# Gọi ufunc myadd với 2 mảng, thực hiện cộng phần tử tương ứng
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
# Kết quả: [6 8 10 12]

# Kiểm tra kiểu dữ liệu của hàm np.add (hàm cộng của numpy)
print(type(np.add))  # Thường sẽ là <class 'numpy.ufunc'>

# So sánh kiểu của np.add xem có phải là ufunc không
if type(np.add) == np.ufunc:
    print("Add is ufunc")
else:
    print("Add is not ufunc")
