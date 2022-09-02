def f(s):
    k = 0
    while s < 80:
        s += 2 * k
        k += 4
    return s


print(f(0))