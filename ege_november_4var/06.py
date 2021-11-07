def f(number):
    s = number
    n = 1
    while s > 0:
        s = s - 5
        n = n + 3
    return n
print(f(42))