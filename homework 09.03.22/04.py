count = -1
c = []
for i in range(1,10001,3):
    c.append(i)
print(c)
for number in range(2532000,2532161):
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
    if (len(k) == 0) and (count in c):
        print(count,number)