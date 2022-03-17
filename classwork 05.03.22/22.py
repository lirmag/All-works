def f(x):
    L, M = 0, 0
    while x > 12:
        L = L + 1
        x = x // 4
        M = x
    if L > M:
        L, M = M, L
    return L, M


for x in range(1, 1000001):
    if f(x) == (3, 7):
        print(x)
