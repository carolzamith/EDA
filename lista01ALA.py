__author__ = 'Carol'

import numpy as np
from scipy import linalg
from random import random
import time

n = 2

a = np.zeros(shape = (n,n))
for x in range(0,n):
    for y in range(0,n):
        if y>=x :
           a[x][y] = random()


b = np.random.random((n,1))
start_time = time.time()
x = linalg.solve(a,b) #solucao
end_time = time.time()

total_time = end_time - start_time
#print total_time

