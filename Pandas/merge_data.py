#=============================== Merge Data Frames & Tables ================================= #
import pandas as pd

employees = {
    "Employee_ID":[101,102,103,104],
    "Name":["Ali","Ahmed","Sara","John"]
}
employee_df = pd.DataFrame(employees)

salary = {
    "Employee_ID":[101,102,103,104],
    "Salary":[50000,45000,65000,70000]
}
salary_df = pd.DataFrame(salary)

department = {
    "Employee_ID":[101,102,103,104],
    "Department":["IT","HR","Finance","IT"]
}
department_df = pd.DataFrame(department)

print(employee_df)
print('-'*50)

print(salary_df)
print('-'*50)

print(department_df)
print('-'*50)

merged_df = pd.merge(employee_df, salary_df, on='Employee_ID')
print(merged_df)
print('-'*50)

inner_join = pd.merge(employee_df, salary_df, on='Employee_ID', how='inner')
print(inner_join)
print('-'*50)

left_join = pd.merge(employee_df, salary_df, on='Employee_ID', how='left')
print(left_join)
print('-'*50)

right_join = pd.merge(employee_df, salary_df, on='Employee_ID', how='right')
print(right_join)
print('-'*50)

outer_join = pd.merge(employee_df, salary_df, on='Employee_ID', how='outer')
print(outer_join)
print('-'*50)

batch1_df = pd.DataFrame({"Student":["Ali","Ahmed"]})
batch2_df = pd.DataFrame({"Student":["Sara","John"]})
batch_df = pd.concat([batch1_df, batch2_df], axis=1)
print(batch_df)

batch_df = pd.concat([batch1_df, batch2_df], axis=1, ignore_index=True)
print(batch_df)

