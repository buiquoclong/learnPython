# Class và Object là hai khái niệm cơ bản trong lập trình hướng đối tượng.
# Class là một bản thiết kế cho các đối tượng, trong khi Object là một thể hiện
# cụ thể của class đó. Class định nghĩa các thuộc tính và phương thức mà các đối tượng
# sẽ có, trong khi Object là một phiên bản cụ thể với các giá trị riêng.

# Định nghĩa một lớp Dog
# Lớp Dog có thuộc tính name, age và species, cùng với phương thức bark
class Dog:
    species = "Animal" # Thuộc tính chung cho tất cả các đối tượng Dog

    # Phương thức khởi tạo (constructor) để tạo đối tượng Dog
    def __init__(self, name, age):  # đúng là __init__, không phải init
        self.name = name
        self.age = age

    # Phương thức để chó sủa
    def bark(self):
        print("Woof!")

# Tạo đối tượng từ lớp Dog
my_dog = Dog(name="Buddy", age=3)

# Lấy các thuộc tính từ đối tượng
dog_name = my_dog.name
dog_age = my_dog.age
dog_species = my_dog.species

# Gọi phương thức bark
my_dog.bark()

# In thông tin
print(f"Name of the dog: {dog_name}")
print(f"Age of the dog: {dog_age}")
print(f"Species of the dog: {dog_species}")
