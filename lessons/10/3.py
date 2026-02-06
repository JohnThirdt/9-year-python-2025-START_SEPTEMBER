import math

def phi(n):
    count = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            count += 1
    return count

for p in [2, 3, 5, 7, 11]:
    print(f"phi({p}) = {phi(p)}")

for p in [6, 25, 36, 49, 15]:
    print(f"phi({p}) = {phi(p)}")