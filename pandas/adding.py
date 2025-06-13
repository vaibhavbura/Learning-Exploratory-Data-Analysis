#adding columns
import pandas as pd
data = {
    "Name":['Ram','Sgyam','Ghnshyam','Dhyansham','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,25,45,85,65,32,56,15],
    "Salary":[5000,2200,215,2222,2566,2456,1555,254545],
    "Performance score":[85,65,25,26,45,65,65,78],


}

df = pd.DataFrame(data)

# sqaure brackets df["Column_Name"] = some_Data
print(df)

df["Bonus"] = df['Salary'] *0.1
print(df)

#using insert method

df.insert(0,"Emplyoyee ID",[10,20,30,40,50,60,70,80])

print(df)