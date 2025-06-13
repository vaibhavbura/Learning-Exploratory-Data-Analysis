"""
np.insert(array,index,value,axis=None)
array-original array
index-position no
value- value to be inserted
axis- if it is none then it is inserted into flatten array  (2d-arrary axis-0) axis1-clounmn wise insert

"""

import numpy as np

arr = np.array([10,20,30])

new_arr=np.insert(arr,2,100)
print(new_arr)