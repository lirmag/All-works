def f(s):
    n = 170
    while s + n < 325:
        s = s + 25
        n = n - 5
    return s


print(f(0))