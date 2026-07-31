import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6), dpi=120)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [10, 15, 18, 25, 30, 40]

plt.plot(
    months,
    sales,
    color="purple",
    marker="o",
    linewidth=2,
    label='Montly Profit'
)

plt.title("Company Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit (Thousands)")
plt.grid()
plt.legend()

plt.show()
#============================================================

plt.figure(figsize=(8, 5), dpi=120)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25, 30, 40, 50, 65, 80]
plt.plot(
    months,
    sales,
    color="green",
    marker="o",
    linewidth=2
)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (Thousands)")
plt.grid()
plt.show()