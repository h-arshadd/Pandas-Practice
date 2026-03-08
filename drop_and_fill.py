import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name':   ['Alice', 'Bob', None, 'Diana', 'Eve'],
    'Age':    [25, None, 30, None, 22],
    'Score':  [85, 90, None, 78, None],
    'City':   [None, 'NYC', 'LA', None, 'Chicago']
})
df = df.dropna(subset=['Name'])
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].fillna(0)
df['City'] = df['City'].fillna('Unknown')

print(df)