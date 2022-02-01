for N in range(1,1001):
    number = bin(N)[2:]
    if N % 2 == 0:
        number = str(number) + '10'
    if N % 2 != 0:
        number = str(number) + '01'
    number = int(number,base=2)
    if number <= 102:
        print(number)