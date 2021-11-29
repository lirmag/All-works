def f(x):
    L = 0
    M = 0
    while x > 0:
        M = M + 2
        if x % 8 != 0:
            L = L + 1
        x = x // 8
    return L, M


for x in range(1, 1001):
    if f(x) == (2, 6):
        print(x)
        break
