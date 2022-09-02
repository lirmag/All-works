def f(s):
    k = 1
    while s < 66:
        k += 3
        s += k
    return k


print(f(0))