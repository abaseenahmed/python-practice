#========================== Lesson 03 Labeling the graph ==========================#
import matplotlib.pyplot as plt

x = [2019, 2020, 2021, 2022, 2023]
y = [120, 180, 250, 300, 450]
plt.plot(x,y)
plt.title('Company Sales Growth')
plt.xlabel('year')
plt.ylabel('Sale (in thousands)')
plt.grid()
plt.show()

# plt.plot(x,y) draws the figure in canvas
# plt.title() writes title for the graph
# plt.xlabel() labels the values for x axis
# plt.ylabel() labels the values for y axis
# plt.grid() adds grid lines to the graph
# plt.show() prints the graphs and shows it on the screen

