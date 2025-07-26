from numpy import random

x = random.choice([5, 6, 9, 8], p=[0.5, 0.2, 0.2, 0.1], size=(100))
x1 = random.choice([5, 6, 9, 8], p=[0.5, 0.2, 0.2, 0.1], size=(3, 5))
print(x)
print(x1)
