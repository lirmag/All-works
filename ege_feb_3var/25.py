count = 0
for number in range(10000000,10000000001):
    if count == 5:
        break
    k = []
    if number % 2 == 0:
        for dig in range(number // 2,2,-1):
            if len(k) == 2:
                break
            if number % dig == 0:
                k.append(dig)
    else:
        for dig in range(number // 2 + 1, 2, -1):
            if len(k) == 2:
                break
            if number % dig == 0:
                k.append(dig)
    if (sum(k) > 0) and (sum(k) < 10000):
        print(sum(k))
        count += 1
