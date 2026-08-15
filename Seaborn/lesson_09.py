# ===================================== Pair Plots & Joint Plots ============================= #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.pairplot(data = df, hue = 'sex', vars=["total_bill", "tip", "size"])
plt.show()

sns.jointplot(
    data=df,
    x="total_bill",
    y="tip",
    kind = "reg",
)

plt.show()