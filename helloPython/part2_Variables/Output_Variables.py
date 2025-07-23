# Output Variables là quá trình in ra các giá trị của biến trong Python.
name = "John Smith"
age = 30

# In ra thông tin bằng cách sử dụng hàm print
print("Name: ", name)
print("Age: ", age)

# In ra thông tin bằng cách sử dụng dấu cộng để nối chuỗi
# Dấu cộng được sử dụng để nối các chuỗi lại với nhau
print("Name: "+ name + ", Age: "+ str(age))

# print with format
# In ra thông tin bằng cách sử dụng f-string
print(f"Name: {name}, Age: {age}")

# In ra thông tin bằng cách sử dụng phương thức format
output = "Name: {}, Age: {}".format(name, age)
print(output)