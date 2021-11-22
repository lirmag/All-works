for number in range(100,1000):
    number = str(number)
    sum_1 = int(number[0]) + int(number[1])
    sum_2 = int(number[1]) + int(number[2])
    answer = str(min(sum_2,sum_1)) + str(max(sum_1,sum_2))
    if answer == '714':
        print(number)
        break