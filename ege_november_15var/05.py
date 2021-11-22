for number in range(1000,10000):
    k = []
    num = str(number)
    sum_1 = int(num[0]) + int(num[1])
    k.append(sum_1)
    sum_2 = int(num[1]) + int(num[2])
    k.append(sum_2)
    sum_3 = int(num[2]) + int(num[3])
    k.append(sum_3)
    ans = str(max(k))
    k.remove(max(k))
    ans += str(max(k))
    if ans == '1515':
        print(number)

