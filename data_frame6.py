import pandas as pd
import numpy as np
df=pd.DataFrame({"Name" : ["Huda", "Ali", "Areesha", "Faria", "Mahrukh"], 
                "Age":[22,np.nan,23,24,23], 
                "City": ["Rwp", "Karachi","Isb",np.nan, "Faisalabad"]
                })
print(df.dropna())
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["City"]=df["City"].fillna("Unknown")
df= df.rename(columns={"Name": "FullName"}) 
print(df)