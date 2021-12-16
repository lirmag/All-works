def f(x):
    Q = 6
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    return L,M
for x in range(1000,-1,-1):
    if f(x) == (3,5):
        print(x)
        break