__author__ = 'Carol'

import numpy as np

A = np.array([[1,0, 0, 0], [1,1,1,1],[1,2,4,8], [1,3,9,27]])
b = np.array([[1],[0],[-1],[2]])
print A
print b

A_inv = np.linalg.inv(A)

v = A_inv * b

print v
