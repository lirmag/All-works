def f(s):
    n = 0
    while s + n < 150:
        s = s - 5
        n = n + 15
    return n
print(f(80))