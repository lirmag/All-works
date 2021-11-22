for number in range(1,101):
    b_number = bin(number)[2:]
    if number % 2 != 0:
        b_number =b_number +  '0'
    if number % 2 == 0:
        b_number = '1' + b_number
    if (b_number.count('1') % 2) == 0:
        b_number = b_number + '1'
    if (b_number.count('1') % 2) != 0:
        b_number = b_number + '0'
    ans = int(b_number,base=2)
    if ans > 228:
        print(number)
        break