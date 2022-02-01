for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        for y in range(1,1001):
            if ((x > A) or (y > x) or ((2*y + x) < 110)) is False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)