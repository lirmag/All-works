def f(n):
    if n > 0:
        print(n)
        f(n - 4)
        f(n // 2)
print(f(9))