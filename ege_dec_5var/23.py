def f(x,y):
    if x == y:
        return 1
    if (x > y) or (x == 26):
        return 0
    if x < y:
        return f(2 * x + 1,y) + f(x + 1,y)
print(f(1,27))