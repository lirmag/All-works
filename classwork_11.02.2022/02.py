k = []
for m in range(0, 28, 2):
    for n in range(1, 19, 2):
        N = ((2 ** m) * (3 ** n))
        if (N >= 200000000) and (N <= 400000000):
            k.append(N)
print(*sorted(k))

