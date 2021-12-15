def f(x):
    L = x
    M = 65
    if L % 2 == 0:
        M = 52
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    return M
for x in range(100,1001):
    if f(x) == 26:
        print(x)
        break