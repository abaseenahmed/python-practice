# ===================================== Bar Plots in Seaborn ===================================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

# CountPlot answers how many obervations bolong to each category
sns.countplot(data=df, x='day', hue='sex')
plt.title('Cont Plot For Day')
plt.show()

# BarPlot answers What is the average value of a numerical variable for each category
sns.barplot(data = df, x = 'day', y = 'total_bill', hue = 'sex')
plt.title('Bar Plot For Total Bill')
plt.show()

# BoxPLot Lets you see the distribution (quirtiles, outliers, etc)
sns.boxplot(data=df, x="day", y="total_bill")
plt.title('Boxplt for Day - Total Bill')
plt.show()

sns.boxenplot(data = df, x = 'day', y = 'total_bill', hue='sex')
plt.title('Boxenplot for Day - Total Bill Distributions')
plt.show()

# violin plot is similar to a boxplot, but it gives you more information about the shape of the distribution.
sns.violinplot(data = df, x = 'day', y = 'total_bill')
plt.title('Violinplot for more informative distribution shape')
plt.show()

# Stripplot let's show the actual individual observations.
sns.stripplot(data = df, x = 'day', y = 'total_bill', jitter=True)
plt.title('Stripplot For Actual Individual Observation')
plt.show()

# Swarmplot gives you the individual observations while arranging them more intelligently.
sns.swarmplot(data = df, x = 'day', y = 'total_bill')
plt.title('Swarmplot Diagram')
plt.show()

# catplot() is a figure-level interface that can create several types of categorical plots.
sns.catplot(data = df, x = 'day', y = 'total_bill', kind = 'bar')
plt.title('Catplor is a Categorical Plot interface')
plt.show()

# The Categorical Plot Cheat Sheet
# | Plot           | Main question                                             |
# | -------------- | --------------------------------------------------------- |
# | `countplot()`  | How many?                                                 |
# | `barplot()`    | What's the average?                                       |
# | `boxplot()`    | What's the distribution/spread?                           |
# | `violinplot()` | What's the shape of the distribution?                     |
# | `stripplot()`  | Where are the individual observations?                    |
# | `swarmplot()`  | Where are the individual observations, with less overlap? |
# | `boxenplot()`  | What's the detailed distribution?                         |
# | `catplot()`    | Create/facet categorical plots                            |
