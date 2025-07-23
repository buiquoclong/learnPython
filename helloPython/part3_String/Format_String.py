name = "Python"
version = 3.9

# Format string bằng cách sử dụng f-string
# F-string là một cách định dạng chuỗi trong Python, cho phép chèn giá trị của biến vào trong chuỗi một cách dễ dàng
# F-string được định nghĩa bằng cách đặt chữ cái 'f' trước chuỗi và sử dụng dấu ngoặc nhọn {} để chèn biến
formatted_string = f"Welcome to {name} version {version}!"
print(formatted_string)

# Format string bằng cách sử dụng phương thức format
# Phương thức format cho phép chèn giá trị của biến vào trong chuỗi bằng cách sử dụng dấu ngoặc nhọn {}
# Các biến được truyền vào phương thức format sẽ được thay thế vào vị trí tương ứng trong chuỗi
formatted_string2 = "Welcome to {} version {}!".format(name, version)
print(formatted_string2)

# Format string với chỉ định vị trí
# Có thể chỉ định vị trí của các biến trong chuỗi bằng cách sử dụng chỉ số trong dấu ngoặc nhọn
course = "Python programming"
hours = 8
course_inffo = "The course '{0}'\nDuration: {1} hours.".format(course, hours)
print(course_inffo)

# Format string với định dạng số
# Định dạng số cho phép hiển thị số với số chữ số thập phân cụ thể
pi_value = 3.14159
formatted_pi = "The value of pi is approximately {:.2f}".format(pi_value)
print("original value of pi", pi_value)
print("Formatted value of pi:", formatted_pi)