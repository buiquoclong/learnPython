from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# y = random.exponential(scale=2, size=(2, 3))
# print(y)

sns.distplot(random.exponential(size=1000), hist=False, label="exponential")
plt.show()