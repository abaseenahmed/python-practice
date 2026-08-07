#=========================== Saving the Matplot Generated Charts =======================#
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6), dpi=120)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [50, 55, 65, 70, 80, 95]

plt.plot(
    months,
    revenue,
    color='blue',
    marker='o',
    linewidth=2,
)
plt.grid()
plt.title('Monthly Revenue')
plt.xlabel('Months')
plt.ylabel('Revenue (Thousands)')

plt.savefig('monthly_revenue.png', dpi=300, bbox_inches="tight")
plt.show() 