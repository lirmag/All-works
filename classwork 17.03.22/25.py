import math
count = 0
for number in range(11000001,10000000000000000001):
    if count == 5:
        break
    k = []
    for dig in range(math.ceil(number // 2), 3,-1):
        if len(k) == 2:
            break
        if number % dig == 0:
            k.append(dig)
    if len(k) < 2:
        M = 0
    else:
        M = max(k) + min(k)
    if (M > 0) and (M < 10000):
        count += 1
        print(number,M)