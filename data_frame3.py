import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Zara"],
    "Age": [20, 21, 19, 22]
})


df["Adult"]=True
print(df[df["Age"]>20])