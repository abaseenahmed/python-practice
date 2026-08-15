# ============================= Heatmaps in Seaborn ================================== #
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
sns.heatmap(data)
plt.show()

matrix = df.corr( numeric_only=True)
print(matrix)
sns.heatmap(matrix, annot=True, fmt='.2f', cmap='coolwarm', lw = 0.5, vmin=-1, vmax=1)
plt.show()

mask = np.triu(np.ones_like(matrix, dtype=bool))
sns.heatmap(matrix, annot=True, fmt='.2f', cmap='coolwarm', lw = 0.5, mask=mask)
plt.show()