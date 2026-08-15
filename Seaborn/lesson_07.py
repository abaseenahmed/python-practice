# ============================== Relational Plot in Seaborn ==================================== #
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.scatterplot(data = df, x = 'total_bill', y = 'tip', hue = 'sex')
plt.title('Total Bill VS Tip')
plt.show()

sns.scatterplot(data = df, x = 'total_bill', y = 'tip', hue = 'sex', style = 'time')
plt.title('Total Bill VS Tip by Gender')
plt.show()

sns.lineplot(data = df, x = 'total_bill', y = 'tip', hue = 'sex')
plt.title('Average Total Bill by Day')
plt.show()

