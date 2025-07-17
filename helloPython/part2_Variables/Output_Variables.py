name = "John Smith"
age = 30

# print normal
print("Name: ", name)
print("Age: ", age)

# print with a line
print("Name: "+ name + ", Age: "+ str(age))

# print with format
# example 1
print(f"Name: {name}, Age: {age}")

# example 2
output = "Name: {}, Age: {}".format(name, age)
print(output)