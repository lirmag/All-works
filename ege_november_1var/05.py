k = []
for number in range(10000,100000):
    number = str(number)
    sum_1 = int(number[0]) + int(number[2]) + int(number[4])
    sum_2 = int(number[1]) + int(number[3])
    if sum_1 > sum_2:
        answer_1 = str(sum_2) + str(sum_1)
    else:
        answer_1 = str(sum_1) + str(sum_2)
    if answer_1 == '723':
        k.append(number)
print(k)
print(min(k))