def f(n):
    q = 0
    for i in range(1,n):
        if n % i == 0:
            q = i
    return q


for x in range(1,1001):
    if f(x) == 17:
        print(x)
        break