import pandas as pd

data = {
    "Name":['Ram','Sgyam','Ghnshyam','Dhyansham','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,25,45,85,65,32,56,15],
    "Salary":[5000,2200,215,2222,2566,2456,1555,254545],
    "Performance_score":[85,65,25,26,45,65,65,78],


}

df = pd.DataFrame(data)
print(df)

high_salary = df[df['Salary']>2000]
print('Employees with salary > 2000')

print(high_salary)

#filtering rows salary > 2k & age >30
filtered = df[(df['Age']>30) & (df['Salary']>2000)]
print(f'Employee list Age > 30 + salary >2000 {filtered}')


#using OR condtion

filtered_or = df[(df['Age']>35) | (df["Performance_score"]>50)]
print(f"Employees older than 35 or performance score >50 {filtered_or}")