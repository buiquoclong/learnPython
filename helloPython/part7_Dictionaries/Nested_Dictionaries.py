# Nested dictionary là một từ điển chứa các từ điển khác bên trong nó.
# Điều này cho phép bạn tổ chức dữ liệu phức tạp hơn, ví dụ như lưu trữ thông tin về nhiều đối tượng.
person = {
    'name': 'Alice',    
    'age': 30,  
    'address': {
        'city': 'New York',
        'zip': '10001'
        }
    }

# In ra thông tin từ từ điển lồng nhau
print(f"Name: {person}")

# In ra thông tin từ từ điển lồng nhau
city = person['address']['city']
print(f"City: {city}")
zip_code = person['address']['zip']
print(f"Zip Code: {zip_code}")

# Thêm một mục mới vào từ điển lồng nhau
person['address']['country'] = 'USA'
print(f"Updated Address: {person['address']}")
print(f"Updated Person: {person}")

# Cập nhật giá trị trong từ điển lồng nhau
person['address']['city'] = 'Los Angeles'
print(f"Updated City: {person['address']['city']}")

# Xóa một mục trong từ điển lồng nhau
del person['address']['zip']
print(f"Address after deletion: {person['address']}")
