# Nhập thư viện scipy.io để làm việc với file .mat và numpy để xử lý mảng
import scipy.io
import numpy as np

# Tạo một mảng numpy 2 chiều (2 hàng, 3 cột)
python_array = np.array([[1, 2, 3], [4, 5, 6]])

# Lưu mảng numpy vào file .mat với tên biến trong file là "myMatArray"
scipy.io.savemat("python_data.mat", {"myMatArray": python_array})

# Đọc dữ liệu từ file MATLAB có tên "matlab_data.mat"
mat_data = scipy.io.loadmat("matlab_data.mat")

# Truy xuất mảng với tên biến "myMatArray" trong file MATLAB vừa đọc
mat_array = mat_data["myMatArray"]

# In ra mảng đã được đọc từ file MATLAB
print("MATLAB Array in Python")
print(mat_array)

# Tính tổng các phần tử ở cột thứ 2 (index 1) của mảng
sum_column2 = np.sum(mat_array[:, 1])
print(f"Sum of the second column: ", sum_column2)
