#============================== Boxplot in Matplotlib ================================#
import matplotlib.pyplot as plt

salary = [
    25000, 27000, 28000, 30000,
    32000, 34000, 35000, 36000,
    38000, 40000, 42000, 45000,
    90000
]

fig, ax = plt.subplots(figsize=(8, 5), dpi=120)
ax.boxplot(
    salary,
    patch_artist=True,
    boxprops={'facecolor' : 'lightblue'},
    medianprops={'color' : 'red', 'linewidth' : 2},
)
ax.set_title('Employee Salary Distribution')
ax.set_ylabel('Salary PKR')
plt.show()

# The outlier value is 90000 because it is the maximum value.