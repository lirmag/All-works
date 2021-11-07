for number in range(1,10001):
    answer = number
    if answer % 2 != 0:
        a = '10'
    else:
        a = '01'
    answer = str(bin(answer)[2:-1]) + a
    answer = int(answer,base=2)
    if answer == 2017:
        print(number)

