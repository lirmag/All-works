def f(x):
    a = 0
    b = 0
    while x > 0:
        a = a + 1
        if x % 2 == 0:
            b += x % 10
        x = x // 10
    return a,b
for x in range(1,10001):
    if f(x) == (3,12):
        print(x)