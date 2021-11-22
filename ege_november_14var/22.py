def f(x):
    a = 0
    b = 10
    while x > 0:
        y = x % 10
        x = x // 10
        if y > a:
            a = y
        if y < b:
            b = y
    return a,b
for x in range(10000,100000):
    if f(x) == (6,3):
        print(x)
        break