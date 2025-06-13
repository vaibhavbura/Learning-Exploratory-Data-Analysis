import pandas as pd
data = {
    "Name":['Ram',None,'Ghnshyam','Dhyansham','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,25,None,85,65,32,56,15],
    "Salary":[5000,None,215,2222,2566,2456,1555,254545],
    "Performance score":[85,None,25,26,45,65,65,78],


}

df = pd.DataFrame(data)
print(df)

#methods -> linear polynomial,time

df.interpolate(method="linear",axis=1,inplace=True)

print(df)