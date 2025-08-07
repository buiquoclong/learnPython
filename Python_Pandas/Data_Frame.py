# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Tạo dữ liệu từ một dictionary, với các khóa là tên cột và giá trị là danh sách dữ liệu tương ứng
data_dict = {
    'Name': ['alice', 'bob', 'charlie'],   # Cột "Name" chứa tên
    'Age': [25, 30, 22],                   # Cột "Age" chứa tuổi
    'City': ['New York', 'France', 'UK']   # Cột "City" chứa thành phố hoặc quốc gia
}

# Tạo DataFrame từ dictionary trên
df_from_dict = pd.DataFrame(data_dict)

# In ra DataFrame được tạo từ dictionary
print("DataFrame from dictionary: ")
print(df_from_dict)

# Tạo dữ liệu dưới dạng danh sách các dictionary
data_list_of_dict = [
    {'name': 'david', 'age': 28, 'city': 'chicago'},   # Mỗi dictionary tương ứng với một dòng
    {'name': 'john', 'age': 30, 'city': 'berlin'}
]

# Tạo DataFrame từ danh sách các dictionary
df_from_list_of_dict = pd.DataFrame(data_list_of_dict)

# In ra DataFrame được tạo từ danh sách các dictionary
print("DataFrame from list of dictionary: ")
print(df_from_list_of_dict)
