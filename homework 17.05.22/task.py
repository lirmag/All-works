import random
flag = True
while flag:
    for a in range(0,10):
        k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        k.remove(a)
        for b in k:
            k.remove(b)
            for