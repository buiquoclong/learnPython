# Import thư viện numpy với tên viết tắt là np
import numpy as np

# Tạo một mảng 1 chiều gồm các số nguyên
original_array = np.array([1, 2, 5, 7, 9, 4])

# -------------------------------
# TÌM VỊ TRÍ PHẦN TỬ CÓ GIÁ TRỊ BẰNG 4
# -------------------------------

# np.where trả về tuple chứa chỉ số (index) của phần tử thỏa điều kiện
result = np.where(original_array == 4)
print(result)
# Kết quả: (array([5]),) → phần tử 4 nằm ở vị trí thứ 5 (chỉ số bắt đầu từ 0)

# -------------------------------
# TÌM VỊ TRÍ NÊN CHÈN 4 ĐỂ GIỮ MẢNG CÓ THỨ TỰ
# -------------------------------

# np.searchsorted tìm vị trí thích hợp để chèn giá trị 4 để mảng vẫn được sắp xếp
result1 = np.searchsorted(original_array, 4)
print(result1)
# Kết quả: 2 → nếu muốn chèn 4 vào mảng để mảng được sắp xếp tăng dần, nên chèn tại index 2
# (Lưu ý: mảng chưa được sort, nên kết quả chỉ chính xác nếu mảng đã được sort)

# -------------------------------
# LỌC CÁC PHẦN TỬ LỚN HƠN 4 BẰNG BOOLEAN INDEXING
# -------------------------------

# Lọc các phần tử trong mảng gốc thỏa điều kiện > 4
result2 = original_array[original_array > 4]
print(result2)
# Kết quả: [5 7 9]

# -------------------------------
# LỌC PHẦN TỬ THỎA ĐIỀU KIỆN BẰNG np.extract
# -------------------------------

# Tạo điều kiện: phần tử > 4
condition = original_array > 4

# Dùng np.extract để lấy các phần tử thỏa điều kiện
result3 = np.extract(condition, original_array)
print(result3)
# Kết quả: [5 7 9] (giống với boolean indexing)
