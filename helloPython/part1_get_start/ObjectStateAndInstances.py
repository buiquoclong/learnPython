# create a basic class

# class Persion:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Name: {self.name} and Age: {self.age}" 
# p1 = Persion("Alex", 25)
# p2 = Persion("James", 30)
# p1.age = 26
# print(p1)
# print(p2)

# Khởi tạo một lớp BankAccount
# Lớp này sẽ có các thuộc tính owner và balance, cùng với phương thức deposit
class BankAccount:
    # Phương thức khởi tạo (constructor) để tạo đối tượng BankAccount
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    # Phương thức để nạp tiền vào tài khoản
    # Phương thức này sẽ cộng số tiền nạp vào balance của tài khoản
    def deposit(self, amount):
        self.balance += amount
    
    # Phương thức để in thông tin tài khoản
    # Phương thức này sẽ trả về một chuỗi mô tả tài khoản
    def __str__(self):
        return f"Owner with name: {self.owner} has {self.balance} dollars"

# Tạo một đối tượng BankAccount
account1 = BankAccount("David", 250)
# Thực hiện nạp tiền vào tài khoản
account1.deposit(500)
account1.deposit(500)
# In thông tin tài khoản
print(account1)