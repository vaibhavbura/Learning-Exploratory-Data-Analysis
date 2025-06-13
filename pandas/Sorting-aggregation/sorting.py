#sorting data
#SORTING DATA 1 COLUMN sort_values()
#single column
import pandas as pd

data ={
    "Name":['Arun','Varun','Karun'],
    "Age":[16,58,30],
    "Salary":[10000,20000,30000]
}

df = pd.DataFrame(data)
df.sort_values(by="Age",ascending=False,inplace=True)
print(f'Sorted Age by Descending{df}')
