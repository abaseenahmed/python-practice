#========================= Lesson 04 Styling the Graph ==============================#
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20, 35, 30, 45, 60, 75]

plt.plot(months, sales, color='green', linewidth=3, linestyle='--', marker='o')
plt.title('First Half Sales Report')
plt.xlabel('Sales (Thousands)')
plt.ylabel('Sales (Thousands)')
plt.grid()
plt.show()

# color='green' adds color green to the graph
# linewidth=3 controls the width of the line in graph
# linestyle='--' gives different stylings to the line
# marker='o' marks the graph with different shapes
# if you remove plt.show() the graph will never show on the screen
# the difference between marker="o" and linestyle="--" is the the marker gives a mileston shape while the linestyle gives different types of lines to graph
# the linewidth=3 is easier to read because it is neither too thick nor too thin as compare to the default linewidth
 