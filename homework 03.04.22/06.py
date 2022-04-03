def f(s):
    n = 20
    while n > s:
        s = s + 1
        n = n - 1
    return n


for s in range(1,1001):
    if f(s) == 16:
        print(s)
        break