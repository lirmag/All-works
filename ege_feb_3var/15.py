for A in range(0,1001):
    flag = True
    for x in range(0,1001):
        for y in range(0,1001):
            if ((((2 * x) + (3 * y)) > 30) or ((x + y) <= A)) is False:
                flag = False
                break
        if flag is False:
            break
    if flag is True:
        print(A)
        break