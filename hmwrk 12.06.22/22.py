def f(x):
    L = 1
    M = 0
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L * (x % 8)
        x = x // 8
    return L,M


for x in range(1,1001):
    if f(x) == (21,3):
        print(x)