def f(M, K):
    M = int(bin(M)[2:])
    K = int(bin(K)[2:])
    return M * K

for A in range(1, 1001):
    flag = True
    for x in range(1, 1001):
        if ((x & 34 == 0) <= ((x & 36 != 0) <= (x & A != 0))) is False:
            flag = False
            break
        if flag is False:
            break
    if flag is True:
        print(A)
        break
