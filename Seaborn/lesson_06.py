# ============================== Distribution Plot in Seaborn Practice ============================ #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.histplot(
    data = df,
    x = 'total_bill',
)
plt.title('Distribution of Total Bill')
plt.show()

sns.histplot(
    data = df,
    x = 'total_bill',
    bins = 20
)
plt.title('Distribution of Total Bill')
plt.show()

sns.histplot(
    data = df,
    x = 'tip',
    kde = True,
    bins = 15
)
plt.title('Distribution of Tips')
plt.xlabel('Tips')
plt.ylabel('Count')
plt.show()

sns.histplot(
    data = df,
    x = 'total_bill',
    kde = True,
    hue = 'sex',
    bins = 20
)
plt.title('Difference in Distribution of Total Bill By Gender')
plt.show()

sns.kdeplot(
    data = df,
    x = 'total_bill',
)
plt.title('Distribution Shape of Total Bill')
plt.show()

sns.kdeplot(
    data = df,
    x = 'total_bill',
    fill = True
)
plt.title('Distribution Shape of Total Bill')
plt.show()

sns.kdeplot(
    data = df,
    x = 'total_bill',
    hue = True,
    fill = 'smoker'
)
plt.title('Distribution Shape of Total Bill')
plt.show()

sns.kdeplot(
    data = df,
    x = 'total_bill',
    bw_adjust=0.5
)
plt.title('Distribution Shape (High Bandwidth) of Total Bill')
plt.show()

sns.kdeplot(
    data = df,
    x = 'total_bill',
    bw_adjust=1
)
plt.title('Distribution Shape (Normal Bandwidth) of Total Bill')
plt.show()

sns.kdeplot(
    data = df,
    x = 'total_bill',
    bw_adjust=2
)
plt.title('Distribution Shape (Low Bandwidth) of Total Bill')
plt.show()

sns.displot(
    data = df,
    x = 'total_bill',
    kind = 'hist',
)
plt.show()

sns.displot(
    data = df,
    x = 'total_bill',
    kind = 'kde'
)
plt.show()

sns.displot(
    data = df,
    x = 'total_bill',
    kind = 'hist',
    col = 'sex'
)
plt.show()