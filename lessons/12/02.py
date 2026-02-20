import numpy as np

a = np.arange(10, 100, 10)

print(a)
print(a[2])

print(a[1:4])

a_slice = a[1:4]
# print(a_slice)
#
# a_slice[0] = 777
# 
# print(a_slice)


c = a[1:4].copy()

c[0] = 777
print(c, a)
