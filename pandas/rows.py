#head()#tail()
#head() 5 
#tail(n)

import pandas as pd
df = pd.read_json("sample_Data.json")
print('Display 10 rows of first')
print(df.head(10))

print('Display 10 rows of last')
print(df.tail(10))


