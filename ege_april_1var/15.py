count = 0
for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        for y in range(1,1001):
            if (((x < 6) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 6))) is False:
                flag = False
                break
        if flag is False:
            break
    if flag is True:
        count += 1
print(count)