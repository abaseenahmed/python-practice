import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 35, 45, 60, 90]

fig, ax = plt.subplots(figsize=(9, 5), dpi=120)

ax.plot(
    months,
    sales,
    marker="o"
)

ax.annotate(
    "Highest Sales",
    xy=("May", 90),
    xytext=("Mar", 75),
    arrowprops={"arrowstyle": "->"}
)

ax.annotate(
    'Lowest Sales',
    xy=('Jan', 20),
    xytext=('Feb', 30),
    arrowprops={'arrowstyle': '->'}
)

ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

ax.grid()

plt.show()