for a in range(1,1001):
    flag = True
    for x in range(1,1001):
        for y in range(1,1001):
            if (((y + 2*x) < a) or (x > 30) or (y > 20)) is False:
                flag = False
                break
        if flag is False:
            break
    if flag is True:
        print(a)
        break