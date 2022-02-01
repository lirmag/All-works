def f(x):
    L = 2 * x - 30
    M = 2 * x + 30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    return M
for x in range(100,1001):
    if f(x) == 30:
        print(x)
        break
