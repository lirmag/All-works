def f(x,k):
    if x == 15:
        return 1
    if x > 15:
        return 0
    if x < 15:
        return f(x + 1,k + 1) + f(x * 2,k + 1) + f(2 * x + 1, k + 1) + f(x * 10,k + 1)


print(f(1,0))