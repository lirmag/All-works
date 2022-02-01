def f(s):
    n = 25
    while s + n <= 100:
        s = s + 20
        n = n - 5
    return s
print(f(0))