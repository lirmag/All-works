def f(s):
    n = 1
    while s > 200:
        s = s - 15
        n = n + 3
    return n
for s in range(1,10001):
    if f(s) == 46:
        print(s)