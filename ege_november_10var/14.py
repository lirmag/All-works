for dig in range(2,37):
    num_1 = 144
    num_2 = 25
    ans_1 = ''
    ans_2 = ''
    while num_1 > 0:
        ans_1 = ans_1 + str(num_1 % dig)
        num_1 //= dig
    while num_2 > 0:
        ans_2 = ans_2 + str(num_2 % dig)
        num_2 //= dig
    ans_1 = int(ans_1,base=dig)
    ans_2 = int(ans_2,base=dig)
    if ans_1 + ans_2 == 201:
        print(dig)
        break