import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
print(df.head())

sns.scatterplot(
    data = df,
    x = 'total_bill',
    y = 'tip',
    hue = 'sex',
    style = 'smoker'
)

plt.grid(axis='y')
plt.show()

sns.lineplot(data = df, x = 'day', y = 'total_bill', hue = 'sex')
plt.show()