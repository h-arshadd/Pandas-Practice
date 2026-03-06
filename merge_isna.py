import pandas as pd
import numpy as np

employees = pd.DataFrame({
    'emp_id':   [101, 102, 103, 104, 105],
    'name':     ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'dept_id':  [1, 2, None, 1, 3]
})

salaries = pd.DataFrame({
    'emp_id':  [101, 102, 103, 106],
    'salary':  [70000, None, 85000, 90000]
})
# Finding employee with missing dept_id
print(employees[employees['dept_id'].isna()])
# Missing values are in each column of employees
print(employees.isna().sum())
# Merging above dataframes
result=pd.merge(employees, salaries, on="emp_id", how="left")
print(result)
#employees have no salary data
print(result[result['salary'].isna()])
# employees in result are missing either dept_id or salary
print(result[result['dept_id'].isna()| result['salary'].isna()])