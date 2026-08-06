import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [42, 48, 56, 63, 71, 79, 88, 95]

plt.scatter(
    study_hours,
    exam_scores,
    color="purple",
    s=120,
    marker="D",
)

plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid()

plt.show()