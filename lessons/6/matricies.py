def is_symmetric(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False
    return True

def matrix_sum(a):
    n = len(a)
    s = 0
    for i in range(n):
        for j in range(n):
            s += a[i][j]
    return s

def matrix_trace(a):
    n = len(a)
    s = 0
    for i in range(n):
        s += a[i][i]
    return s











if __name__ == "__main__":
    matrix = [[1, -1, 2], [2, 1, -2], [1, 5, 1]]
    print(f"Is matrix simmetric: {is_symmetric(matrix)}")
    print(f"The sum of the all elements from matrix is {matrix_sum(matrix)}")
    print(f"The trace of the matrix is {matrix_trace(matrix)}")

