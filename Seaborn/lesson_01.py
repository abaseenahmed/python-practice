import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "score": [45, 50, 58, 65, 70, 78, 85, 92]
}

df = pd.DataFrame(data)

sns.scatterplot(
    data=df,
    x="study_hours",
    y="score"
)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

plt.show()