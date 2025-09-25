# n! = 1 * 2 * ... * n

def factorial(n):
    r = 1
    for i in range(1, n+1):
        r = r * i
    return r

print(factorial(4))

def factorial2(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial2(4))