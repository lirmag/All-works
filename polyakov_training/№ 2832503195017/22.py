def f(x):
    s = 0
    while x > 0:
       s = s + x % 9
       x = x // 3
    return s


for x in range(81,1000001):
    if f(x) == 17:
        print(x)
        break