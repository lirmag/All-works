count = 0
c = 0
ans = []
for number in range(10000000,2,-1):
    if count == 3:
        break
    k = []
    if number % 2 == 0:
        for dig in range(2,(number // 2) + 1):
            if number % dig == 0:
                k.append(dig)
                break
    else:
        for dig in range(2,((number + 1) // 2) + 1):
            if number % dig == 0:
                k.append(dig)
                break
    if len(k) == 0:
        count += 1
        ans.append(str(10000000 - number) + ' '+ str(number))
for number in range(10000000,10000000000000000000,1):
    if c == 3:
        break
    a = []
    if number % 2 == 0:
        for dig in range(2,(number // 2) + 1):
            if number % dig == 0:
                a.append(dig)
                break
    else:
        for dig in range(2,((number + 1) // 2) + 1):
            if number % dig == 0:
                a.append(dig)
                break
    if len(a) == 0:
        c += 1
        ans.append(str(number - 10000000) + ' '+ str(number))
print(ans)
