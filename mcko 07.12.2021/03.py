def f(s):
    n = 1
    while s < 45:
        s = s + 6
        n = n * 4
    return n
for s in range(1,1001):
    if f(s) == 256:
        print(s)
# 26