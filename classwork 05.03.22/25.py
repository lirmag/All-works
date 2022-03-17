count = 0
for number in range(800001,1000000000001):
    if count == 5:
        break
    k = []
    if number % 2 == 0:
        for dig in range(2,(number // 2) + 1):
            if number % dig == 0:
                k.append(dig)
    else:
        for dig in range(2,((number + 1) // 2) + 1):
            if number % dig == 0:
                k.append(dig)
    if len(k) > 0:
        M = min(k) + max(k)
    else:
        M = 1
    if M % 138 == 0:
        print(number,M)
        count += 1