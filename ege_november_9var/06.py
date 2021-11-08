def f(s):
    n = 300
    while s + n <= 600:
        s = s + 40
        n = n - 20
    return s
print(f(100))