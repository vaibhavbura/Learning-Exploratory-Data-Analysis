"""
.ravel()-> views -> modification in original array
.flatten()-> copy -> no modification in original array
"""

import numpy as np

arr= np.array([10,20,50,30,55,55])

print(arr.ravel())
print(arr.flatten())
