count = -1
for number in range(3144472, 3144601):
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
    if len(k) == 0:
        print(count,number)