import numpy as np

data = np.array([1, 2, 100, 15, -14.5])

print(data)

print(data.sum())

print(data.mean())
print(data.std())

print(data.min(), data.max())
print(data.argmin(), data.argmax())

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(matrix.sum())


print(matrix.sum(axis=1)) # суммирование по первой оси - по строкам
print(matrix.sum(axis=0))