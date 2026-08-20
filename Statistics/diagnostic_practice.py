import pandas as pd

data = {
    "employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "salary": [35, 38, 42, 48, 55, 63, 72, 150],
    "projects": [1, 2, 2, 3, 4, 5, 6, 7],
    "performance": [60, 65, 67, 72, 78, 82, 85, 88]
}

df = pd.DataFrame(data)
print(df.head(5))
print(f'Mean: {df.mean()}')
print(f'Median: {df.median()}')
# The median represents the "typical" salary here.
# the mean is affected by extreme high or low numbers, while the median is not. so if there is very large or very small value in this dataset the mean is affected but median remains original.
