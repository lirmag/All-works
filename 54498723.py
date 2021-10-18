import numpy as np

sum_1 = 0
max_1 = 1000000000
m = np.zeros(max_1 + 1, dtype=np.int16)


def f(n, level=0, curmin=max_1):
    if level > curmin: return - 1
    if n <= 3:
        return f(n + 3)
    if n > 3:
        return f(n - 1)
    if n > 3 and f(n - 1) % 2 == 0:
        return f(n - 2)
    if n > 3 and f(n - 1) % 2 != 0:
        return f(n - 2) + 2 * n


for n in range(30, 41):
    print(f(n))
    sum_1 += f(n)
print(sum_1)
