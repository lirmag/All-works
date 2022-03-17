for N in range(1,10001):
    number = bin(N)[2:]
    if N % 2 != 0:
        number = str(number) + '0'
    else:
        number = '1' + str(number)
    if number.count('1') % 2 == 0:
        number = number + '1'
    else:
        number = number + '0'
    number = int(number,base=2)
    if number > 228:
        print(N)
        break