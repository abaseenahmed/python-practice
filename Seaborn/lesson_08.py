# ============================ Regression Plot in Seaborn =============================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.regplot(
    data = df,
    x = 'total_bill',
    y = 'tip',
)
plt.title('Total Bill Vs Tip')
plt.show()

sns.regplot(
    data = df,
    x = 'total_bill',
    y = 'tip',
    ci = None
)
plt.title('Total Bill Vs Tip')
plt.show()

sns.regplot(
    data = df,
    x = 'total_bill',
    y = 'tip',
    order = 2
)
plt.title('Plynomial Regression Plot')
plt.show()

sns.lmplot(
    data=df,
    x = "total_bill",
    y = "tip",
    hue = "sex",
    col = 'time'
)

plt.show()