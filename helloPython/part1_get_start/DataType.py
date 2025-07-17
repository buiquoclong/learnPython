# Integer
number = 10
# Float
float_number = 3.14 
# String
text1 = "This is string1"
text2 = "This is string2"
# Boolean
booleanVariable = True
# List
fruits = ["Apple", "Banana", "Orange"]

print(type(number))
print(type(float_number))
print(type(text1))
print(type(booleanVariable))
print(type(fruits))

newString = text1 + " " + text2
print(newString)

# Add a new fruit
fruits.append("Strawberry")
print(fruits)

# Remove a fruit
fruits.remove("Orange")
print(fruits)

list_number = (1, 2, 3, 4, 5)
print(list_number[1])
