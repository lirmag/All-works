k = []
def f(x):
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if M < x:
            M = M + (x % 10) * 2
        x = x // 10
    return L, M
for x in range(1,10001):
    if f(x) == (3,28):
        k.append(x)
print(min(k))