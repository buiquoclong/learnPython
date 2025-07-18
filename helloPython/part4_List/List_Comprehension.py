# Tạo list comprehension trong Python
# List comprehension là một cách ngắn gọn để tạo danh sách mới từ một danh sách hiện có.
square = [x**2 for x in range(5)] #Tạo danh sách bình phương của các số từ 0 đến 4
print(square)

even_squared = [x**2 for x in range(10) if x % 2 == 0] # Tạo danh sách bình phương của các số chẵn từ 0 đến 9
print(even_squared)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Tạo ma trận 3x3
print(matrix)

flatted_matrix = [num for row in matrix for num in row] # Làm phẳng ma trận thành một danh sách
print(flatted_matrix)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 if x % 2 == 0 else x for x in numbers] # Tạo danh sách bình phương cho các số chẵn, giữ nguyên số lẻ

double_numbers = [x*2 for x in range(10)] # Tạo danh sách các số nhân đôi từ 0 đến 9
print(double_numbers)