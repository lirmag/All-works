count = 0
for number in range(200000000,10000000000000000000000001):
    if count == 5:
        break
    sum_1 = 1
    k = []
    if number % 2 == 0:
        for dig in range(2, (number // 2) + 1):
            if len(k) == 5:
                break
            if number % dig == 0:
                k.append(dig)
    else:
        for dig in range(2, ((number + 1) // 2) + 1):
            if len(k) == 5:
                break
            if number % dig == 0:
                k.append(dig)
    if len(k) != 5:
        sum_1 = 0
    else:
        for elem in k:
            sum_1 *= elem
    if (sum_1 % 10 == 1) and (sum_1 < number):
        count += 1
        print(sum_1,max(k))
