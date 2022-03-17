def f(a, n):
    if n == 1:
        return a
    else:
        return f(a * n, n - 1)


print(f(1, 6))
