# Array là một cấu trúc dữ liệu trong Python cho phép lưu trữ một tập hợp các phần tử có cùng kiểu dữ liệu.
import numpy as np
# Khởi tạo một mảng NumPy
# Mảng NumPy là một mảng đa chiều, có thể chứa các giá trị số
array = np.array([1, 2, 3, 4, 5])
list = [1, 2, 3, 4, 5]
# Truy cập các phần tử trong mảng bằng chỉ số, bắt đầu từ 0
first_element = list[0]

# Truy cập các phần tử trong mảng NumPy, từ chỉ số 1 đến 3 (không bao gồm 4)
subset = list[1:4] 

# Thay đổi giá trị của phần tử tại chỉ số 2
list[2] = 10 

# Thêm phần tử mới vào cuối danh sách
list.append(6) 

# Thêm phần tử mới vào đầu danh sách
list.insert(0, 0) 

# Thêm nhiều phần tử vào cuối danh sách
list.extend([7, 8]) 

# Xóa phần tử có giá trị 4 khỏi danh sách
list.remove(4) 

# Xóa phần tử tại chỉ số 1 khỏi danh sách
list.pop(1) 

# Thực hiện in ra với mảng thường
print(f'list: {list *2}')
print(f'first element: {first_element}')
print(f'subset: {subset}')

# Thực hiện in ra với mảng NumPy
print(f'array: {array*2}') 
print(f'first element_array: {array[0]}')
print(f'subset: {array[1:4]}')