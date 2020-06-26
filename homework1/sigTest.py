import numpy as np
import matplotlib.pyplot as plt

def sig(x):
    s = 1 / (1 + np.exp(-x))
    return s

def deriSig(x):
    s = sig(x)
    ds = s * (1 - s)
    return ds

def gradientDescend(p0, grad, step, epochs):
    gd = []
    gd.append(p0)
    p = p0

    for _ in range(epochs):
        w = p - step * deriSig(p)
        gd.append(w)
        p = w
    return np.array(gd)

p = 0
epochs = 100
step = 0.01
gd = gradientDescend(p, deriSig, step, epochs)
print(gd)

t = np.arange(-10, 10, 0.01)
plt.plot(t, deriSig(t), c = 'b')
plt.plot(gd, deriSig(gd), c = 'r', label = 'step = {}'.format(step))
plt.scatter(gd, deriSig(gd), c = 'r')
plt.legend()
plt.show()

t = np.arange(-5.5, 5.5, 0.01)
plt.plot(t, sig(t), c = 'b')
plt.plot(gd, sig(gd), c = 'r', label = 'step = {}'.format(step))
plt.scatter(gd, sig(gd), c = 'r')
plt.legend()
plt.show()