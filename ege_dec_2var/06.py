def f(s):
    n = 0
    while 2 * s * s < 10 * s:
        s = s + 1
        n = n + 2
    return n
print(f(0))