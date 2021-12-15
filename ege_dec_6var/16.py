def f(n):
    print(n,end='')
    if n > 2:
        f(n - 3)
        f(n - 2)
        f(n - 1)
print(f(4))