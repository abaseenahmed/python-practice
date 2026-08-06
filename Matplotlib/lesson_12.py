#============================= Pie Charts in Matplotlib ==============================#
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8), dpi=120)

platforms = ["YouTube", "Instagram", "Facebook", "LinkedIn"]
users = [45, 25, 20, 10]

plt.pie(
    users,
    labels=platforms,
    autopct="%1.1f%%",
    startangle=90,
    # shadow=True,
    # explode=[0.03, 0.03, 0.03, 0.03]
)

plt.title("Social Media Usage")

plt.show()

#  the pie charts looks better and proffesional without shadow