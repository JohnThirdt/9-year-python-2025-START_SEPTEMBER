n = 93

f = True
for i in range (2, n):
    if n % i == 0:
        f = False

print(f"Число простое {f}")