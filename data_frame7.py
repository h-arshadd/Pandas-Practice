import pandas as pd
df=pd.DataFrame({"Name" : ["Huda", "Ali", "Areesha", "Faria", "Mahrukh"], 
                "Age":[22,22,23,24,23], 
                "City": ["Rwp", "Karachi","Isb","Isb", "Faisalabad"]
                })
df2 = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Zara"],
    "Age": [20, 21, 19, 22]
})
print(df["City"])
print(df.groupby("City")["Age"].mean())
print(df.value_counts("City"))
print(df.sort_values("Age", ascending=False))
merge_df=pd.merge(df,df2, on='Age')
concat_row=pd.concat([df,df2], axis=0)
print(merge_df)
print(concat_row)