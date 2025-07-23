# Copy dictionary là quá trình tạo một bản sao của từ điển hiện có.
# Điều này có thể hữu ích khi bạn muốn làm việc với một bản sao mà không làm 
# thay đổi từ điển gốc.
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Sử dụng phương thức copy để tạo bản sao nông của từ điển
copied_dict = my_dict.copy()
print("Original dictionary:", my_dict)
print("Copied dictionary:", copied_dict)

new_copied_dict = dict(my_dict)  # Tạo bản sao nông khác
print("New copied dictionary:", new_copied_dict)

# Thay đổi giá trị trong bản sao
copied_dict['age'] = 31
print("Updated copied dictionary:", copied_dict)
# Bản sao gốc không bị ảnh hưởng    
print("Original dictionary after modification:", my_dict)

new_dict = {'persion':{'name': 'Bob', 'age': 25}, 'city': 'Los Angeles'}
# Sử dụng phương thức copy để tạo bản sao nông của từ điển lồng nhau
copied_nested_dict = new_dict.copy()
print("Original nested dictionary:", new_dict)
print("Copied nested dictionary:", copied_nested_dict)