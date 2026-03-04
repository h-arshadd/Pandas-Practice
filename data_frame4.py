import pandas as pd
df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Zara"],
    "Age": [20, 21, 19, 22]
})
print(df.sort_values("Age", ascending=False))
print(df.reset_index(drop=True))