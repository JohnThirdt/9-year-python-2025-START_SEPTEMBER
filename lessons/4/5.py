x0 = 10

v0 = 2

a = -1

import numpy as np

t = [i for i in range(0, 100)]

x = [x0 + v0*tau + a*tau**2/2 for tau in t]

import matplotlib.pyplot as plt

plt.plot(t, x)

plt.xlabel('Время, с')
plt.ylabel('Координата, м')

plt.show()
