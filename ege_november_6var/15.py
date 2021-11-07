for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        for y in range(1,1001):
            if ((((2*x) + (3*y)) != 60) or (A >= x) or (A >= y)) is False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break