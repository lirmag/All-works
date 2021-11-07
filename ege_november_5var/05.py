for number in range(1,101):
    b = number
    stage = '0'
    if number % 2 == 0:
        stage = '00'
    if number % 2 != 0:
        stage = '11'
    number = bin(number)[2:]
    answer = str(number) + str(stage)
    a = int(answer,base=2)
    # a = ''
    # while answer > 0:
    #     a = a + str(answer % 2)
    #     answer //= 2
    if a >= 115:
        print(b)
        break