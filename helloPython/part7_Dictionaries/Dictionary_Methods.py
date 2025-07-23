# Dictionary Methods là các phương thức được sử dụng để thao tác với từ điển trong Python.
# Các phương thức này cho phép bạn thêm, xóa, cập nhật và truy cập các mục trong từ điển.

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
key = my_dict.keys()  # Trả về một đối tượng view chứa tất cả các khóa trong từ điển
print("Keys:", key)

value = my_dict.values()  # Trả về một đối tượng view chứa tất cả các giá trị trong từ điển
print("Values:", value)

items = my_dict.items()  # Trả về một đối tượng view chứa tất cả các cặp khóa-giá trị trong từ điển
print("Items:", items)

# Kiểm tra xem một khóa có tồn tại trong từ điển hay không
if 'name' in my_dict:
    print("Key 'name' exists in the dictionary.")

# Thêm một mục mới vào từ điển
my_dict['country'] = 'USA'
print("Updated dictionary:", my_dict)

age = my_dict.get('age', 'Not Found')  # Sử dụng get để lấy giá trị của khóa 'age', 'Not Found' nếu không tồn tại
print("Age:", age)

remove_age = my_dict.pop('age', 'Not Found')  # Sử dụng pop để xóa mục 'age' và trả về giá trị đã xóa, 'Not Found' nếu không tồn tại
print("Removed Age:", remove_age)
print("Dictionary after removing age:", my_dict)

new_data = {'age': 31, 'hobby': 'Reading'}
# Cập nhật từ điển bằng cách sử dụng phương thức update
my_dict.update(new_data)
print("Dictionary after update:", my_dict)