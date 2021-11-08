def f(x):
    a = 0
    b = 0
    while x > 0:
        c = x % 2
        if c == 0 :
            a += 1
        else:
            b += 1
        x //= 10
    return a,b
for x in range(-2**31,(2**31) - 1):
    if f(x) == (2,3):
        print(x)
        break