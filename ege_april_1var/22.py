def f(x,y):
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
    return a,x,y


for x in range(1,101):
    for y in range(1,101):
        if f(x,y)[0] == 7 and f(x,y)[1] == 42:
            print(f(x,y))