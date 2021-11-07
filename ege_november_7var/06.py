def f(number):
    s = number
    n = 1
    while n <= 300:
        s = s + 30
        n = n * 3
    return s
print(f(0))