for number in range(9999,1001,-1):
    k = []
    number = str(number)
    k.append(int(number[0]) + int(number[1]))
    k.append(int(number[1]) + int(number[2]))
    k.append(int(number[2]) + int(number[3]))
    k.remove(min(k))
    sum_1 = str(min(k)) + str(max(k))
    if sum_1 == '1315':
        print(number)
        break