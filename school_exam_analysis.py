# Uses pivot table and corr() function
import pandas as pd

df = pd.DataFrame({
    'student': ['Alice','Alice','Alice','Bob','Bob','Bob','Carol','Carol','Carol','Dave','Dave','Dave'],
    'subject': ['Math','Science','English','Math','Science','English','Math','Science','English','Math','Science','English'],
    'score':   [85, 92, 78, 90, 88, 76, 72, 65, 80, 95, 89, 91],
    'hours_studied': [5, 6, 4, 7, 6, 5, 3, 2, 4, 8, 7, 9]
})

pivot = pd.pivot_table(
    df, 
    values='score',
    index='student',
    columns='subject',
    aggfunc='mean'
)

print(pivot)
print(df[['score', 'hours_studied']].corr())

pivot2= pd.pivot_table(
    df,
    values='score',
    index='student',
    columns='subject',
    aggfunc='mean'
)
print(pivot2)
print(pivot2.corr())