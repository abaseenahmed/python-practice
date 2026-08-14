# ============================== Different types of categorical plots ============================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

print(df.head())

count_customer = df.groupby('day').size()
print(count_customer)
sns.countplot(data = df, x = 'day')
plt.title('Number of customers for each day')
plt.show()

count_gender = df.groupby('sex').size()
print(count_gender)
sns.countplot(data = df, x = 'sex')
plt.title('Number of customers by gender')
plt.grid()
plt.show()

average_bill = df.groupby('day')['total_bill'].mean()
print(average_bill)
sns.barplot(data = df, x = 'day', y = 'total_bill', label = 'Average Total')
plt.title('Average total bill per day')
plt.show()

average_tip = df.groupby('sex')['tip'].mean()
print(average_tip)
sns.barplot(data = df, x = 'sex', y = 'tip')
plt.title('Average tip by gender')
plt.show()

sns.boxplot(data = df, x = 'day', y = 'total_bill', hue = 'sex')
plt.title('Distribution of Bills by Day')
plt.show()

sns.boxplot(data = df, x = 'day', y = 'tip', hue = 'sex')
plt.title('Distribution of tips by geder')
plt.show()

sns.stripplot(data = df, x = 'day', y = 'total_bill', hue = 'sex', jitter=True)
plt.title('Individual Total bill by Day')
plt.show()

sns.swarmplot(data = df, x = 'day', y = 'tip', hue = 'sex')
plt.title('Individual tip by Day')
plt.show()

print(f'The day with the most customer is: {df.groupby('day')['tip'].idxmax()}')
sns.catplot(data = df, x = 'day', kind = 'count')
plt.title('Day with most Customer')
plt.show()

print(f'The day with the highest average bill is: {df.groupby('day')['total_bill'].idxmax()}')
sns.catplot(data = df, x = 'day', y = 'total_bill', kind = 'bar')
plt.title('Day with highest average bill')
plt.show()

print(f'Difference of total bill accorss days: {df.groupby('day')['total_bill'].sum()}')
sns.lineplot(data = df, x = 'day', y = 'total_bill')
plt.title('Difference of total bill accorss days')
plt.show()

print(f'Difference of tips by gender: {df.groupby('sex')['tip'].sum()}')
sns.catplot(data = df, x = 'sex', y = 'tip', kind = 'bar')
plt.title('Difference of tips by gender')
plt.show()

sns.catplot(data = df, x = 'day', y = 'total_bill', kind = 'scatter')
plt.title('Individual total bill per day')
plt.show()
