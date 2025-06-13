import pandas as pd

df_customers =pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':["Suresh","Ramesh","Dogesh"]
})

df_orders =pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,350,514]
})

df_merged_inner=pd.merge(df_customers,df_orders,on="CustomerID",how="inner")
df_merged_outer=pd.merge(df_customers,df_orders,on="CustomerID",how="outer")#fill with nan
print(df_merged_inner)
print(df_merged_outer)

"""
cross join
1df = m rows
2df = n rows
m*n rows
"""