
import pandas as pd

data ={
    "Name":['Arun','Varun','Karun'],
    "Age":[16,58,30],
    "Salary":[10000,20000,30000]
}

df = pd.DataFrame(data)
df.sort_values(by=["Age","Salary"],ascending=[True,False],inplace=True)
print(f'Sorted Multiple columns{df}')
