for number in range(1,100001):
    digit = number
    answer = number
    a = ''
    b = ''
    while digit > 0:
        a = a + str(digit % 3)
        digit //= 3
    while answer > 0:
        b = b + str(answer % 5)
        answer //= 5
    if (a[0] == '0') and (b[0] == '0'):
        print(number)
        break
    else:
        a = ''
        b = ''
        digit = 0
        answer = 0
        continue
