def f(x):
    a = 1
    b = 0
    while x > 0:
        c = x % 10
        a = a * c
        if c > b:
            b = c
        x //= 10
    return a,b


for x in range(1,1001):
    if f(x) == (48,6):
        print(x)
        break