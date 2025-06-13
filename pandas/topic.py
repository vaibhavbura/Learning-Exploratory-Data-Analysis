"""
1- how big is your dataset
2- what are the names of colums

shapes and columns
"""

import pandas as pd

data = {
    "Name":['Ram','Sgyam','Ghnshyam','Dhyansham','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,25,45,85,65,32,56,15],
    "Salary":[5000,2200,215,2222,2566,2456,1555,254545],
    "Performance score":[85,65,25,26,45,65,65,78],


}

df = pd.DataFrame(data)
print(df)
print(f'Shape : {df.shape}')
print(f'Column names: {df.columns}')

