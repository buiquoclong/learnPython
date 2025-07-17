class Dog:
    species = "Animal"

    def __init__(self, name, age):  # đúng là __init__, không phải init
        self.name = name
        self.age = age

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
