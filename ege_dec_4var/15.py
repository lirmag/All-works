k = []
for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        for y in range(1,1001):
            if (((x < 5) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 5))) is False:
                flag = False
                break
            if flag == False:
                break
        if flag == False:
            break
    if flag == True:
        k.append(A)
print(len(k))