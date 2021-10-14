k = []


def func_1(number):
    s = number
    n = 1
    while s < 185:
        s = s + 30
        n = n * 3
    return n


for i in range(1, 1000):
    if func_1(i) == 729:
        k.append(i)
print(max(k), min(k), sep="")
