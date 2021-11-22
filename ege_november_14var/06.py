def f(s):
    n = 1
    while s <= 365:
        s += 36
        n *= 2
    return n
print(f(6))