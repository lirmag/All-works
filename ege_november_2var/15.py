for A in range(1,10001):
    flag = True
    for x in range(1,10001):
        for y in range(1,10001):
            if ((((3 * x) + (4 * y)) != 70) or (A > x) or (A > y)) is False:
                flag = False
                break
        if flag == False:
            break
    if flag is True:
        print(A)