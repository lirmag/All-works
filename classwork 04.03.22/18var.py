# print(2**29)
# print(3**18)
for m in range(1,30,2):
    for n in range(2,19,2):
        N = (2**m) * (3**n)
        if (N > 150000000) and (N < 300000000):
            print(N, n + m)
