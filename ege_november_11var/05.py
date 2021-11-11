for number in range(100,1000):
    num = str(number)
    sum_1 = int(num[0]) + int(num[1])
    sum_2 = int(num[1]) + int(num[2])
    answer = str(max(sum_1,sum_2)) + str(min(sum_1,sum_2))
    if answer == '159':
        print(number)
        break