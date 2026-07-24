#====================================== This is The Very First Program in Pandas ==================#
import pandas as pd

students = {
    "Name":["Ali", "Ahmed", "Khan", "Sara", "Jane"],
    "Age": [20, 22, 24, 19, 21],
    "Marks": [88, 91, 95, 82, 85]
}
df = pd.DataFrame(students)
print(df)