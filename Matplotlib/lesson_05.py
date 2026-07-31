#=========================== Lesson 05 Markers Customization =====================#
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [31, 33, 35, 36, 34, 32, 30]

plt.plot(days, temperature, color='cyan', linewidth=2, linestyle='-', marker='^', ms=10, mfc='green', mec='orange', mew=2)
plt.title('Weekly Temperature')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.grid()
plt.show()

#every new marker related argument gives more details to the styling of the marker such as width, edge, color, style, face etc
# line be 
# inside of the marker yellow color
# border of the marker is blue
# shape of the marker is daimond