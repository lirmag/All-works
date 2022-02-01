for N in range(1,101):
    number = str(bin(N))[2:]
    if N % 2 == 0:
        number = '1' + number + '0'
    if N % 2 != 0:
        number = '11' + number + '11'
    R =  int(number,base=2)
    if R > 52:
        print(N)
        break