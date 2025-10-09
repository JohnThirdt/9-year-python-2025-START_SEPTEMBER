import matplotlib.pyplot as plt

x = list(range(-10, 10, 1))
y = [i**2 for i in range(-10, 10, 1)]

plt.plot(x, y)

plt.title('Парабола y = x^2')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()