import pandas as pd
df = pd.read_json("output.json")

print(df.info())

# class 'pandas.core.frame.DataFrame'>
# RangeIndex: 20 entries, 0 to 19
# Data columns (total 6 columns):
#  #   Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   id           20 non-null     int64  
#  1   name         20 non-null     object 
#  2   description  20 non-null     object 
#  3   price        20 non-null     float64
#  4   category     20 non-null     object 
#  5   image        20 non-null     object 
# dtypes: float64(1), int64(1), object(4)
# memory usage: 1.1+ KB
# None


#20 rows 6 columns