def f(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += x % 12
        else:
            b *= x % 12
        x = x // 12
    return a,b
for x in range(1,1001):
    if f(x) == (2,10):
        print(x)
        break