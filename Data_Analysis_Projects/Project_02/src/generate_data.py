import numpy as np
import pandas as pd

np.random.seed(42)

n = 10000

student_id = np.arange(1, n + 1)

gender = np.random.choice(
    ["Male", "Female"],
    n
)

age = np.random.randint(
    17,
    25,
    n
)

study_hours = np.random.normal(
    4.5,
    2,
    n
)

study_hours = np.clip(
    study_hours,
    0,
    12
)

attendance = np.random.normal(
    78,
    12,
    n
)

attendance = np.clip(
    attendance,
    40,
    100
)

sleep_hours = np.random.normal(
    7,
    1.2,
    n
)

sleep_hours = np.clip(
    sleep_hours,
    3,
    11
)

previous_score = np.random.normal(
    65,
    15,
    n
)

previous_score = np.clip(
    previous_score,
    20,
    100
)

assignments_completed = np.random.randint(
    40,
    101,
    n
)

class_participation = np.random.randint(
    0,
    101,
    n
)

internet_access = np.random.choice(
    ["Yes", "No"],
    n,
    p=[0.85, 0.15]
)

parental_support = np.random.choice(
    ["Low", "Medium", "High"],
    n,
    p=[0.2, 0.5, 0.3]
)

final_score = (
    0.30 * previous_score
    + 2.5 * study_hours
    + 0.15 * attendance
    + 0.08 * assignments_completed
    + 0.05 * class_participation
    + np.random.normal(0, 8, n)
)

final_score = np.clip(
    final_score,
    0,
    100
)

df = pd.DataFrame({
    "student_id": student_id,
    "gender": gender,
    "age": age,
    "study_hours": study_hours,
    "attendance": attendance,
    "sleep_hours": sleep_hours,
    "previous_score": previous_score,
    "assignments_completed": assignments_completed,
    "class_participation": class_participation,
    "internet_access": internet_access,
    "parental_support": parental_support,
    "final_score": final_score
})

# Introduce missing values intentionally

missing_columns = [
    "study_hours",
    "attendance",
    "sleep_hours",
    "internet_access",
    "parental_support"
]

for column in missing_columns:
    indices = np.random.choice(
        df.index,
        size=100,
        replace=False
    )

    df.loc[indices, column] = np.nan


# Introduce duplicate rows

duplicates = df.sample(
    50,
    random_state=42
)

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

df.to_csv(
    "../data/student_performance.csv",
    index=False
)

print("Dataset generated successfully.")
print(df.shape)