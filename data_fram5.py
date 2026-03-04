import pandas as pd
df=pd.DataFrame({"Name" : ["Huda", "Ali", "Areesha", "Faria", "Mahrukh"], 
                "Age":[22,22,23,24,23], 
                "City": ["Rwp", "Karachi","Isb","Chakwal", "Faisalabad"]
                })
print(df)
print(df[["Name", "Age"]])
print(df[df["Age"]>23])
print(df.loc[3])
print(df.iloc[3])
print(df[df["Name"]=="Ali"])