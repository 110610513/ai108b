'''
AND Gate
 x | y | o 
 0 | 0 | 0
 0 | 1 | 0
 1 | 0 | 0
 1 | 1 | 1

 0*w1 + 0*w2 + b = 0
 0*w1 + 1*w2 + b = 0
 1*w1 + 0*w2 + b = 0
 1*w1 + 1*w2 + b = 1

A X = B

 A = 0 0 1  X = w1  B = 0
     0 1 1      w2      0
     1 0 1      b       0
     1 1 1              1

 x*w1 + y*w2 + b = o
'''
import gd2 as gd
import numpy as np
from numpy.linalg import norm, inv
    
A = np.array([[0.0, 1, 1], 
             [1, 0, 1], 
             [1, 1, 1]])
A1 = inv(A)
B = np.array([0.0, 0, 1]).transpose()

X = np.dot(A1, B)
print(X)
