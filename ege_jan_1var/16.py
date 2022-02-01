def f(n):
    if n > 0:
        f(n // 3)
        print(n,'\n')
        f(n - 3)
f(9)