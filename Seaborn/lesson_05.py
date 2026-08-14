# ================================ Distribution Plots in Seaborn ============================= #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.histplot(data = df,
    x = 'total_bill', 
    bins = 10, 
    kde = True, 
    stat = 'count', 
    hue = 'smoker', 
    multiple = 'stack')
plt.title('Total Bill Distribution')
plt.show()

sns.kdeplot(
    data = df,
    x = 'total_bill',
    hue = 'sex',
    fill = True, 
    bw_adjust=1
)
plt.title('KDE of Total Bills')
plt.show()

sns.displot(
    data = df,
    x = 'total_bill',
    hue = 'sex',
    row = 'smoker', 
    col = 'time',
    kind = 'kde'
)
plt.show()


