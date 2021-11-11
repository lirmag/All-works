for number in range(13,101):
    a = str(bin(number)[2:])
    sum_1 = 0
    sum_2 = 0
    for i in range(0,len(a) - 1):
        sum_1 += int(a[i])
    answer = a + str(sum_1 % 2)
    for s in range(0,len(answer) - 1):
        sum_2 += int(answer[s])
    final = answer + str(sum_2 % 2)
    final = int(final,base=2)
    if final > 93:
        print(number)
        break
    else:
        sum_1 = 0
        sum_2 = 0
        continue