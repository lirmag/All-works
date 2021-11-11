def f(s):
    n = 75
    while s + n < 150:
        s = s + 15
        n = n - 5
    return n
print(f(0))