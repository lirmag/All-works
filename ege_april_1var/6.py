def f(s):
    k = 0
    while s < 100:
        s += k
        k += 4
    return k


print(f(0))