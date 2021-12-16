def f(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a = a + x % 8
        else:
            b = b * (x % 8)
        x = x // 2
    return a,b
for x in range(1,1001):
    if f(x) == (6,2):
        print(x)
        break