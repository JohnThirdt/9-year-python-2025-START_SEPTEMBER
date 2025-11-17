import matplotlib.pyplot as plt

R = 50 # ом

U = [ i/10 for i in range(11)]

I = [i/R for i in U]

P = [i**2 * R  for i in I]

plt.plot(I, P)


plt.show()