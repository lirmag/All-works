def f(n):
    if n > 2:
        return f(n - 1) + g(n - 2)
    else:
        return 2
def g(n):
    if n > 2:
        return g(n - 1) + f(n - 2)
    else:
        return 2
print(g(6))