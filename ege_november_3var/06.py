def f(number):
    s = number
    n = 300
    while s + n <= 500:
        s = s + 30
        n = n - 20
    return s
print(f(100))