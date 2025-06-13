import pandas as pd
data = {
    "Name":['Ram',None,'Ghnshyam','Dhyansham','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,25,None,85,65,32,56,15],
    "Salary":[5000,None,215,2222,2566,2456,1555,254545],
    "Performance score":[85,None,25,26,45,65,65,78],


}

df = pd.DataFrame(data)
print(df)

#fillna(value,inplace=True)

# df.fillna(10,inplace=True)

df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)

