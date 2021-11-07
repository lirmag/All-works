k  = []
count = 0
digit = 2
for number in range(123456789,223456790):
    if number % 2 == 0:
        for digit in range(2,(number // 2) + 1):
            if number % digit != 0:
                continue
            if number % digit == 0:
                count += 1
                k.append(digit)
    else:
        for digit in range(2,((number -1) // 2)):
            if number % digit != 0:
                continue
            if number % digit == 0:
                count += 1
                k.append(digit)
    if count == 3:
        print(number,max(k))
        k = []
        count = 0
    else:
        k = []
        count = 0