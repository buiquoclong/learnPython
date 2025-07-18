name = "Python"
version = 3.9

# This is a format string example 1
formatted_string = f"Welcome to {name} version {version}!"
print(formatted_string)

# This is a format string example 2
formatted_string2 = "Welcome to {} version {}!".format(name, version)
print(formatted_string2)

# This is a format string example 3
course = "Python programming"
hours = 8
course_inffo = "The course '{0}'\nDuration: {1} hours.".format(course, hours)
print(course_inffo)

# This is a format string example 4
pi_value = 3.14159
formatted_pi = "The value of pi is approximately {:.2f}".format(pi_value)
print("original value of pi", pi_value)
print("Formatted value of pi:", formatted_pi)