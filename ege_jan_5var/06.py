def f(s):
    n = 200
    while s // n >= 2:
        s = s + 5
        n = n + 5
    return s
print(f(500))

