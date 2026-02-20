import numpy as np


b = [3, 4, 5, 6]
a = [1, 2, 3, 4]


c = [0]*4
for i in range(len(a)):
    c[i] = b[i] + a[i]

print(c)


b = [3, 4, 5, 6]
a = [1, 2, 3, 4]

a1 = np.array(a)
b1 = np.array(b)
print(a1 + b1, type(a1))

d = [1, 0, 3, 7]

e = [x*2 for x in d]
print(e)

d1 = np.array(d)
e1 = d1 * 2
print(d1 * 2, "\n", d1 ** 0.5)

