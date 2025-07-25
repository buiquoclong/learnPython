# Import thư viện NumPy để làm việc với mảng
import numpy as np

# Tạo mảng số nguyên (int) mặc định
array_int = np.array([1, 2, 3])

# Tạo mảng số thực (float) mặc định
array_float = np.array([1.0, 2.5, 5.6])

# Tạo mảng số phức (complex) mặc định
array_complex = np.array([1 + 2j, 3 - 4j])

# In ra kiểu dữ liệu (dtype) của mảng số nguyên
# Mặc định sẽ là int64 (trên máy 64-bit)
print(array_int.dtype)

# In ra kiểu dữ liệu của mảng số thực
# Mặc định sẽ là float64
print(array_float.dtype)

# In ra kiểu dữ liệu của mảng số phức
# Mặc định sẽ là complex128
print(array_complex.dtype)

# Tạo mảng số nguyên với kiểu dữ liệu được chỉ định rõ ràng là int32
array_explicit_int = np.array([1, 2, 3], dtype='int32')

# In ra kiểu dữ liệu của mảng vừa tạo
# Kết quả sẽ là int32
print(array_explicit_int.dtype)

# Tạo mảng số phức với kiểu dữ liệu chỉ định là complex128 (độ chính xác cao)
array_complex64 = np.array([1 + 2j, 3 - 4j], dtype='complex128')

# In ra kiểu dữ liệu của mảng array_explicit_int (chắc là bạn muốn in array_complex64)
# Nhưng đang in nhầm lại array_explicit_int.dtype -> vẫn là int32
print(array_explicit_int.dtype)
