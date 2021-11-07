def f(n):
    if n < 8:
        f(n + 3)
        f(2 * n)
        print(n)
print(f(1))