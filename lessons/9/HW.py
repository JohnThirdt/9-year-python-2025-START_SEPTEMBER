import time
import math

def count(n):
    result = 0
    for i in range(n):
        result += math.sqrt(i) * math.sin(i)
    return f"{result}"

#Последовательно
def count_sequential():
    for i in range(8):
        result = count(1000000)
        print(f"Задача {i+1}: {result}")

# 2. Параллельно
# Используй multiprocessing.Pool или Process