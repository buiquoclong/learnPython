coordinates = (10, 20, 30)
x, y, z = coordinates  # Unpacking the tuple into variables
print("X:", x)
print("Y:", y)
print("Z:", z)

def get_coordinates():
    return (5, 15, 25)  
x, y, z = get_coordinates()  # Unpacking the returned tuple
print("X from function:", x)
print("Y from function:", y)
print("Z from function:", z)

numbers = (1, 2, 3, 4, 5) #Tupel chứ 5 phần tử
a, b, *rest = numbers   #  a và b sẽ nhận hai phần tử đầu tiên, rest sẽ nhận các phần tử còn lại
print("A:", a)
print("B:", b)
print("Rest of the numbers:", rest)  # Rest will contain all remaining elements as a list

nested_tuple = (1, 2, (3, 4))  # Tuple lồng nhau
a, b, (c, d) = nested_tuple # Gán các phần tử của tuple lồng nhau
print("A:", a)
print("B:", b)
print("C:", c)
print("D:", d)