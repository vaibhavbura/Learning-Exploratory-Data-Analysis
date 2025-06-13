import pandas as pd

data ={
    "Name":['Arun','Varun','Karun','Tarun','Narun'],
    "Age":[16,30,30,34,16],
    "Salary":[10000,20000,30000,25300,52000]
}

df = pd.DataFrame(data)

grouped = df.groupby("Age")['Salary'].sum()
print(grouped)
