count = 0
for number in range(194441, 196501):
    count += 1
    k = []
    if number % 2 == 0:
        for dig in range(2,(number // 2) + 1):
            if number % dig == 0:
                k.append(1)
                break
    else:
        for dig in range(2,((number + 1) // 2) + 1):
            if number % dig == 0:
                k.append(1)
                break
    if len(k) == 0 and (number % 100 == 93):
        print(count,number)