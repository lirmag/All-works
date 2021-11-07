count = 0
for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        for y in range(1,1001):
            if (((x < A) <= ((x**2) < 100)) and (((y**2) <=64) <= (y <= A))) is False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        count += 1
        print(A)
print(count)