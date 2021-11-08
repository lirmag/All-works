for number in range(26,1001):
    digit = bin(number)[2:]
    c = ''
    if number % 2 == 0:
        c = '01'
    if number % 2 != 0:
        c = '10'
    answer = str(digit) + str(c)
    answer = int(answer,base=2)
    if answer > 102:
        print(answer)
        break