def f(number):
    s = number
    n = 20
    while s + n <= 100:
        s = s + 25
        n = n - 5
    return s
print(f(0))