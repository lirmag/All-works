def f(x,y):
    if (x > y) or (x == 24):
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1,y) + f((2 * x) + 1,y)
print(f(1,25))