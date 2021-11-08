for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        for y in range(1,1001):
            if (((y + (2 * x)) < A) or (x > 15) or (y > 30)) is False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break