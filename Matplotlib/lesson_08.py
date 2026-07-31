#======================== Lesson 08: Colors, Color Codes & Multiple Styling Options ======================#
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
income = [30, 35, 45, 50, 65, 75]
expenses = [20, 25, 30, 35, 40, 50]

plt.figure(figsize=(10, 6), dpi=120, )
plt.plot(
    months,
    income,
    color="#2ecc71",
    linewidth=3,
    marker="o",
    alpha=0.9,
    label='Icome'
)
plt.plot(
    months,
    expenses,
    color="#e74c3c",
    linewidth=3,
    marker="s",
    alpha=0.7,
    label='Expenses'
)
plt.title('Icome VS Expenses')
plt.xlabel('Months')
plt.ylabel('Amount (Thousands)')
plt.grid()
plt.legend()
plt.show()