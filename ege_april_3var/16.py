def f(n):
    if n > 0:
        g(n - 1)


def g(n):
    print('*')
    if n > 1:
        f(n - 2)


print(f(11))