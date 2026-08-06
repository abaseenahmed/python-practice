# ============================ Subplots in Matplotlib =========================#
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [25, 35, 45, 55, 65]
profit = [10, 15, 20, 28, 35]

fig, ax = plt.subplots(1, 2, figsize=(12, 5), dpi=120)

ax[0].plot(
    months,
    sales,
    color='blue',
    marker='o'
)
ax[0].set_title("Monthly Sales")
ax[0].set_xlabel('Months')
ax[0].set_ylabel('Sales')
ax[0].grid()

ax[1].bar(
    months,
    profit,
    color='green',
)
ax[1].set_title('Monthly Profit')
ax[1].set_xlabel('Months')
ax[1].set_ylabel('Profits')

plt.tight_layout()
plt.show()
