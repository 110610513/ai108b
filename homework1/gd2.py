import numpy as np
from numpy.linalg import norm

def df(f, p, k, step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

def grad(f, p, step=0.01):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return gp

def gradientDescendent(f, p0, step=0.01):
    p = p0.copy()
    i = 0
    fp0 = f(p)
    while (True):
        i += 1
        fp = f(p)
        gp = grad(f, p)
        glen = norm(gp)
        print('{:d}:p={:s} f(p)={:.3f} gp={:s} glen={:.5f}'.format(i, str(p), fp, str(gp), glen))
        if glen < 0.00001 or fp0 < fp:
            break
        gstep = np.multiply(gp, -1*step)
        p +=  gstep
        fp0 = fp
    return p
