def f(n):
    if n < 8:
        f(n + 3)
        print(n,end='')
        f(2 * n)


print(f(1))