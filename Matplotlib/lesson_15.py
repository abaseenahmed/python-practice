#====================== Object Oriented API Method for Matplotlib ax ==========================#
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
visitors = [1200, 1500, 1800, 1700, 2100, 2400]

fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
ax.plot(
    months,
    visitors,
    color='royalblue',
    lw=2,
    marker='o',
    label='Website Visistors',
)
ax.set_title('Monthly Website Visitors')
ax.set_xlabel('Months')
ax.set_ylabel('Visitors')
ax.grid()
ax.legend()
plt.savefig('website_visitors.png', dpi=300, bbox_inches="tight")
plt.show()