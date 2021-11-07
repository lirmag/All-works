count = 0
for number in range(700001,800000):
    digit = 2
    while number % digit != 0:
        digit += 1
        if digit >= number:
            digit = 0
            break
    if digit == 0:
        continue
    M = str(digit + (number // digit))
    if M[-1] == '8':
        count += 1
        print(number,M,digit)
    if count == 5:
        break