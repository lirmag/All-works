for number in range(1,1001):
    num = bin(number)[2:]
    sum_1 = 0
    for x in num:
        x = int(x)
        sum_1 += x
    num = num + str(sum_1 % 2)
    sum_1 = 0
    for l in num:
        l = int(l)
        sum_1 += l
    num = num + str(sum_1 % 2)
    num = int(num,base=2)
    if num < 98:
        print(number)
# 24