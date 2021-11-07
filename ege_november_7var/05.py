for number in range(10000,100000):
    number = str(number)
    sum_1 = int(number[0]) + int(number[2]) + int(number[4])
    sum_2 = int(number[1]) + int(number[3])
    answer = str(min(sum_1,sum_2)) + str(max(sum_1,sum_2))
    if answer == '621':
        print(number)
        break