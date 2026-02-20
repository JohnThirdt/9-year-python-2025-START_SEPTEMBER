import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0, 360, 10)

a = np.radians(a)

b = np.sin(a)
plt.plot(a, b)
plt.show()