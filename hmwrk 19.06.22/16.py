def f(n):
    if n > 0:
        g(n - 1)


def g(n):
    print('*',end='')
    if n > 1:
        f(n - 3)


print(f(11))