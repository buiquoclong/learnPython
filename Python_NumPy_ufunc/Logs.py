import numpy as np

# Tạo mảng số nguyên từ 1 đến 5
number_array = np.array([1, 2, 3, 4, 5])

# Tính logarit tự nhiên (cơ số e) cho từng phần tử trong mảng
logarithmic_result = np.log(number_array)
print("Logarithmic result: ", logarithmic_result)
# Ví dụ: log(1)=0, log(2)=~0.693,...

# Tính hàm mũ (exponential) e^x cho từng phần tử trong mảng
exponential_result = np.exp(number_array)
print("Exponential result: ", exponential_result)
# Ví dụ: e^1 ≈ 2.718, e^2 ≈ 7.389,...

# Tính logarit cơ số 10 cho từng phần tử trong mảng
log_base_10_result = np.log10(number_array)
print("Log base 10 result: ", log_base_10_result)
# Ví dụ: log10(1)=0, log10(10)=1,...
