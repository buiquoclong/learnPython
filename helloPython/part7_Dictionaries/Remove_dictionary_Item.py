# Dictionary là một cấu trúc dữ liệu trong Python cho phép lưu trữ các cặp khóa-giá trị.
# Remove dictionary là quá trình xóa một hoặc nhiều mục khỏi từ điển.
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Xóa một mục khỏi từ điển
# Sử dụng pop để xóa mục 'age' và lưu giá trị đã xóa
removed_item = my_dict.pop('age', None)
print("Removed item:", removed_item)
print("Updated dictionary:", my_dict)
# Nếu khóa không tồn tại, pop sẽ trả về giá trị mặc định None

# Nếu bạn muốn xóa một mục mà không cần lưu giá trị đã xóa, có thể sử dụng del
# del my_dict['age'] sẽ xóa mục 'age' khỏi từ điển
# Xóa một mục khỏi từ điển bằng del
del my_dict['city']
print("Dictionary after deletion:", my_dict)

# Nếu bạn muốn xóa tất cả các mục trong từ điển, có thể sử dụng clear
my_dict.clear()
print("Dictionary after clearing:", my_dict)

