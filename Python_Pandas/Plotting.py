import pandas as pd
import matplotlib.pyplot as plt

data_relationship = {"X": [1, 2, 3, 4, 5],
                     "Y": [5, 7, 9, 11, 13]}

df_relationships = pd.DataFrame(data_relationship)

df_relationships.plot(x="X", y="Y", kind="scatter")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot")
# plt.show()

data_distribution = {"Values": [3, 4, 5, 6, 9, 10, 12, 15, 17, 20, 25, 30]}
df_distribution = pd.DataFrame(data_distribution)

df_distribution["Values"].plot(kind="hist", bins=5)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Distribution Histogram")
plt.show()