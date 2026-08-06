#=============================== Lesson 10 Bar Charts in Matplotlib =============================#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6), dpi=120)

courses = ['Python', 'Java', 'JavaScript', 'C++', 'AI']
students = [120, 95, 70, 110, 85]

plt.bar(
    courses,
    students,
    # color='teal',
    color='#3275A8',
    # width=0.6
    width=0.8
)
plt.title('Students Enrolled Per Course')
plt.xlabel('Courses')
plt.ylabel('Number of Students')
plt.grid(axis='y')
plt.show()

# the bar charts of color = 'teal' and width=0.6 looks much better becausse the width of bars are not increased too much and looks good ui looks
