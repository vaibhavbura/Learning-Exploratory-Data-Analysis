"""
slicing

array[start:stop:step]

arr[start:end] , start to end -1

negative step, -1 

"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr[1:5])
print(arr[:4])
print(arr[::-1])