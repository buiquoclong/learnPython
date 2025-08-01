import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {"Age": [25, 30, 35, 40, 45],
        "Income": [25000, 30000, 35000, 60000, 70000],
        "Expenses": [23000, 20000, 15000, 14000, 40000]}

df = pd.DataFrame(data)
correlation_matrix = df.corr()
print("correlation matrix: ")
print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=.5)

plt.title("Correlation Heatmap")
plt.show()
