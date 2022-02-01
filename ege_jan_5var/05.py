for N in range(2,10001):
    a = str(bin(N)[2:])
    number = a[0:len(a) - 1]
    if N % 2 == 0:
        number = number + '01'
    if N % 2 != 0:
        number = number + '10'
    ans = int(number,base=2)
    if ans == 2018:
        print(N)
        break