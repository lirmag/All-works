def f(s):
    n = 1
    while s <= 205:
        s += 20
        n *= 2
    return n
print(f(26))