for a in range(1,1001):
    flag = True
    for x in range(1,1001):
        for y in range(1,1001):
            if ((((2 * x) + (3 * y)) > 30) or ((x + y) <= a)) is False:
                flag = False
                break
        if flag is False:
            break

    if flag is True:
        print(a)
        break
