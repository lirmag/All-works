for A in range(1, 1001):
    flag = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((x * y) < A) or (y > x) or (x >= 8)) is False:
                flag = False
                break
        if flag is False:
            break
    if flag is True:
        print(A)
        break
