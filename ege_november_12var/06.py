def f(s):
    n = 0
    while 2 * s < 111:
        s = s + 8
        n = n + 2
    return n
print(f(0))