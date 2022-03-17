def f(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return f(x + 1,y) + f(x + 2,y)


print((f(11,17) * f(17,29)) + (f(11,23) * f(23,29)) + (f(11,17) * f(17,23) * f(23,29)))