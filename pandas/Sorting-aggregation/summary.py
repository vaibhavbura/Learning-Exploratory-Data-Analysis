
import pandas as pd

data ={
    "Name":['Arun','Varun','Karun'],
    "Age":[16,58,30],
    "Salary":[10000,20000,30000]
}

df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print(avg_salary)
