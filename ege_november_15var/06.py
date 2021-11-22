def f(s):
    n = 1
    while s <= 1024:
        s += 128
        n *= 2
    return n
print(f(0))