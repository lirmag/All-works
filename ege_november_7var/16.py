def f(n):
    print(n)
    if n < 5:
        f(n + 1)
        f(n + 2)
print(f(2))