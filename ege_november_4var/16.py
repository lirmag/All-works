def f(n):
    if n < 10:
        f(n + 3)
        print(n)
        f(3 * n)
print(f(1))