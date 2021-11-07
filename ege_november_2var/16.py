def f(n):
    if n > 2:
        return f(n - 1) + G(n - 2)
    else:
        return 1
def G(n):
    if n > 2:
        return G(n - 1) + f(n - 2)
    else:
        return 1
print(f(8))