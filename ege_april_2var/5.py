for num in range(1):
    num = 191
    number = bin(num)[2:]
    print(number)
    number = number[0:-2:]
    print(int(number, base=2))
    number = int(number, base=2) + 4
    number = bin(number)[2:]
    number = number[0:-2:]
    number = int(number, base=2) + 4
    print(number)