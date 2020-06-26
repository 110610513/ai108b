import gd2 as gd
import numpy as np
from numpy.linalg import norm
    
A = np.array([[0.0, 0, 1], 
             [0, 1, 1], 
             [1, 0, 1], 
             [1, 1, 1]])
B = np.array([0.0, 0, 0, 1]).transpose()

# def deriSig(x):
#     s = sig(x)
#     ds = s * (1 - s)
#     return ds

def sig(x):
    s = 1 / (1 + np.exp(-x))
    return s

def f(p):
    X = p
    Y = np.dot(A, X)
    return norm(Y - B)

p = np.array([0.0, 0, 0])
p = gd.gradientDescendent(f, p)
B = np.dot(A, p)

print("p = {}".format(p))
print("A = {}".format(A))
print("A dot p = {}".format(B))
print("sig(B) = {}".format(sig(B)))
ans = []
for i in B:
    #ans.append(0) if sig(i) <= 0.5 else ans.append(1)
    ans.append(0) if sig(i) <= 0.6 else ans.append(1)
print("ans = {}".format(ans))
