from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x = random.pareto(a=2, size=(4, 5))
# print(x)

shape_parameter = 2.5
data = random.pareto(shape_parameter, size=1000)
plt.hist(data, bins=50, density=True, color="purple", )

plt.show()
