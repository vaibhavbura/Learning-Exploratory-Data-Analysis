import numpy as np

zeros_array = np.zeros(((3,3,3)))
filled_array = np.full((2,2),7)
print("Zeros")
print(zeros_array)
print(filled_array)

#arange-> arange(start,stop,step)
arrANGE = np.arange(1,5,1)
print(arrANGE)

#creating identity matrices
#eye(size)
print("Identity matrix")
identity_matrix = np.eye(3)
print(identity_matrix)