from numpy import random
import matplotlib.pyplot as plt

# x = random.chisquare(df=2, size=(3, 4))
# print(x)

degrees_of_freedom = 3
data = random.chisquare(degrees_of_freedom, size=1000)
plt.hist(data, bins=50, density=True, color="black")

plt.show()