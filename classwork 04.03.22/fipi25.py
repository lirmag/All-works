count = 0
for number in range(700001,10000000000000):
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
    if len(k) == 0:
        M = 0
    else:
        M = max(k) + min(k)
    if M % 10 == 8:
        count += 1
        print(number, M)