def f(x):
    a = 0
    b = 0
    while x > 0:
        a += 1
        if (b < (x % 8)):
            b = x % 8
        x //= 8
    return a,b
for x in range(1,1001):
    if f(x) == (3,2):
        print(x)
        break