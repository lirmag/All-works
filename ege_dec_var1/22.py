def f(x,y):
    k = []
    if y > x:
        z = x
        x = y
        y = z
    a = x
    b = y
    while b > 0:
        r = a % b
        a = b
        b = r
    # return a,x,y
    k.append(a)
    k.append(x)
    k.append(y)
    return k
for x in range(1,1001):
    for y in range(1,1001):
        if (f(x,y)[0] == 7) and (f(x,y)[1] == 42):
            print(y)