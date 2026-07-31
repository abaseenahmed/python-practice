#======================== Lesson 06 Multiple Lines and Legends in Graph ======================#
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

company_a = [20, 25, 35, 45, 55, 65]
company_b = [18, 28, 30, 50, 58, 70]

plt.plot(months, company_a, color='blue', marker='o', label='Company A')
plt.plot(months, company_b, color='red', marker='s', label='Company B')

plt.title('Company Sales Comparison')
plt.xlabel('Months')
plt.ylabel('Sales (thousands)')
plt.grid()
plt.legend()
plt.show()

# we use the label parameter to give this line a different and unique names such as company A, B etc
# the legend does not appear unless the plt.legend() is called because it is a boolean functions if it is called the legends will show in the graph otherwise will not appear
# a single matplot graph can contain infinite number of lines
# if two lines have the same label it will still appear as two labels the lines can be different