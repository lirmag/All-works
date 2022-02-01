
for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        for y in range(1,1001):
            if (((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))) is False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)