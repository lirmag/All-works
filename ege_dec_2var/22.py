def f(x):
    S = x
    R = 0
    while x > 0:
        d = x % 2
        R = 10 * R + d
        x = x // 2
    S = R + S
    return str(S)
for x in range(1,1001):
    if len(f(x)) == 6:
        print(x)
        break