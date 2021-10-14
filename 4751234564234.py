k = 0


def func_1(number):
    s = number
    n = 1
    while s > n:
        s = s - 15
        n = n * 5
    return (n)


for i in range(1, 10000):
    if func_1(i) == 125:
        k += 1
print(k)
