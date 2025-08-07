# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Tạo một list các số nguyên
a = [7, 5, 9]

# Tạo một pandas Series từ list, pandas sẽ tự tạo chỉ số mặc định (0,1,2)
myvar = pd.Series(a)
print(myvar)

# Tạo pandas Series từ list với chỉ số (index) được đặt theo ý muốn
myvar1 = pd.Series(a, index=["p", "q", 'r'])
print(myvar1)

# Tạo một list các số nguyên khác
data_list = [10, 20, 30, 40, 50]

# Tạo Series từ list dữ liệu, chỉ số mặc định là 0 đến 4
series_from_list = pd.Series(data_list)

# Tạo Series từ dictionary, trong đó key sẽ trở thành index của Series
data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

series_with_index = pd.Series(data_dict)

# In ra Series tạo từ list
print("Series from list: ")
print(series_from_list)

# In ra Series tạo từ dictionary (key làm index)
print("\nseries with index: ")
print(series_with_index)
