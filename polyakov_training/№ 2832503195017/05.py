for N in range(1,1001):
    number = bin(N)[2:]
    if N % 2 == 0:
        number = '1' + str(number)
    if N % 2 != 0:
        number = str(number) + '0'
    if number.count('1') % 2 == 0:
        number = str(number) + '1'
    if number.count('1') % 2 != 0:
        number = str(number) + '0'
    ans = int(number,base=2)
    if ans > 228:
        print(N)
        break