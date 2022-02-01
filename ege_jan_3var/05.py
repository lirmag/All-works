for N in range(1,101):
    number = bin(N)[2:]
    sum_1 = 0
    sum_2 = 0
    for elem in number:
        elem = int(elem)
        sum_1 = sum_1 + elem
    number = str(number) + str(sum_1 % 2)
    for el in number:
        sum_2 = sum_2 + int(el)
    number = str(number) + str(sum_2 % 2)
    number = int(number,base=2)
    if number > 97:
        print(number)
        break