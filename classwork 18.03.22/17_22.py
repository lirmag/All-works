def f(x):
    m = 0
    s = 0
    while x > 0:
        d = x % 7
        s += d
        if d > m:
            m = d
        x = x // 7
    return m,s


for x in range(1,10001):
    if f(x) == (3,14):
        print(x)
        break