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

# create a new class
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def __str__(self):
        return f"Owner with name: {self.owner} has {self.balance} dollars"

account1 = BankAccount("David", 250)
account1.deposit(500)
account1.deposit(500)
print(account1)