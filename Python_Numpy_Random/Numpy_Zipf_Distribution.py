from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=(3, 4))
# print(x)

sns.distplot(x[x<10], kde=False)
plt.show()