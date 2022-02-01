def f(x):
    a = 0
    b = 10
    while x > 0:
        d = x % 6
        if d > a:
            a = d
        if d < b:
            b = d
        x = x // 6
    return a + b

for x in range(1,1001):
    if f(x) == 7:
        print(x)
        break