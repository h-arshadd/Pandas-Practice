import pandas as pd
#creating df
df=pd.DataFrame({"names": ["Ali","Sara","John"], "age":[20,22,19], "marks":[85,90,78]})
print(df.head(2))
print(df.tail(1))
#basic info
print(df.columns)
print(df.dtypes)
print(df.shape)
#selecting data
print(df[["names","marks"]])
print(df.loc[df["names"] == "Sara", ["names", "age"]])
#basic operations
print(df["marks"].mean())
print(df["age"].max())
df["passed"]=df["marks"]>80
print(df)
df[df["passed"]]
#small functions
df_sorted = df.sort_values(by="marks", ascending=False)
print(df_sorted)
df.loc[df["names"] == "John", "marks"] = 88
print(df)
