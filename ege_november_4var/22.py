def f(x):
    a = 0
    b = 0
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 6
        x = x // 6
    return a,b
for x in range(1,1001):
    if f(x) == (2,8):
        print(x)
        break