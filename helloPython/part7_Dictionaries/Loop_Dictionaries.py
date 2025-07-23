# Loop Dictionaries in Python là quá trình lặp qua các mục trong một từ điển để truy cập hoặc xử lý các cặp khóa-giá trị.
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Lặp qua các mục trong từ điển
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Lặp qua các khóa trong từ điển
for key in my_dict.keys():
    print(f"Key: {key}")

# Lặp qua các giá trị trong từ điển
for value in my_dict.values():
    print(f"Value: {value}")

# Lặp qua từ điển với enumerate để có chỉ mục, enumerate là một hàm tích hợp trong Python
#  cho phép bạn lặp qua một iterable và nhận được chỉ mục của từng phần tử.
for index, (key, value) in enumerate(my_dict.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")