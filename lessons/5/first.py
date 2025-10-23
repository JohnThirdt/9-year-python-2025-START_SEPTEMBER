from math import factorial

def C0(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k)) # // намного быстрее /

print("C(n, k) =", C0(8, 2)) # если мы здесь получилии дробную часть, то где-то  было деление - возможно

print(factorial(5)) # факториал возвращает целые числа

# print(factorial(1.5))  факториал дробных чисел не определен! - Traceback


a = [1, 1, 1, 1, 1, 1] # списки могут содержать повторяющиеся элементы

b = {1, 1, 1, 2, 3, 3, 3} # а в множестве повторяющихся элементов нет!
print(b, type(b))

c = set(a)

print(f"set c = {c} is defined with list  {a}")


def C1(n, k):
    if (n<0) or (k<0) or (k>n):
        return 0
    if k == 0:
        return 1 # только пустое множество
    return C1(n-1, k-1) + C1(n-1, k)

print("C(n, k) = ", C1(8, 2))
