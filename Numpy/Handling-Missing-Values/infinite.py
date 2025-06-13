import numpy as np

arr = np.array([1,2,np.inf,4,-np.inf,6])

clean_arr = np.nan_to_num(arr,nan=1)


print(arr)