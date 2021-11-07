for A in range(1,1001):
    flag = True
    for m in range(1,1001):
        for n in range(1,1001):
            if (((3*m + 4*n) > 66) or (m <= A) or (n < A)) is False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
