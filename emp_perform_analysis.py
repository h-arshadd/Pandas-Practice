import pandas as pd

data = {
    'emp_id':     [1, 2, 3, 2, 4, 1, 5],
    'department': ['HR', 'IT', 'IT', 'IT', 'HR', 'HR', 'Finance'],
    'score':      [88, 95, 70, 95, 60, 88, 75],
    'year':       [2023, 2023, 2023, 2023, 2024, 2023, 2024]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Task 1 - Drop duplicates based on emp_id and score
clean_df = df.drop_duplicates(subset=['emp_id', 'score'])
print("\nAfter Dropping Duplicates:")
print(clean_df)

# Task 2 - Sort by department (A→Z), then score (highest first)
sorted_df = clean_df.sort_values(['department', 'score'], ascending=[True, False])
print("\nSorted by Department & Score:")
print(sorted_df)

# Task 3 - Max score and employee count per department
grouped = clean_df.groupby('department')['score'].agg(
    max_score='max',
    employee_count='count'
)
print("\nMax Score & Employee Count per Department:")
print(grouped)

# Task 4 - Departments where average score > 75
avg_scores = clean_df.groupby('department')['score'].mean()
filtered = avg_scores[avg_scores > 75]
print("\nDepartments with Average Score > 75:")
print(filtered)