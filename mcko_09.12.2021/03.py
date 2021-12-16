def f(d):
    n = 1
    s = 9
    while s < 500:
        s = s + d
        n = n * 2
    return n
for d in range(1,1001):
    if f(d) == 64:
        print(d)
        break