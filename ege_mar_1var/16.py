def f(n):
    if n < 8:
        f(2 * n)
        print(n)
        f(n + 3)


print(f(1))