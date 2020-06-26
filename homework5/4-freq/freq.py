import matplotlib.pyplot as plt
from numpy import arange, cos, pi, set_printoptions as setPr
from numpy.fft import ifft
from random import randint

setPr(precision=4, suppress=True)

freq = randint(0, 10)
t = arange(-10*pi, 10*pi, 0.1*pi)

ft = 10*cos(freq*t)
fi = ifft(ft)
print('ft=', ft)
print('fi=', fi)
plt.plot(t, ft, color="red")
plt.plot(t, fi, color="blue")

plt.show()
