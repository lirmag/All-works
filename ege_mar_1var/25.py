import math
for number in range(123456789, 223456790):
    k = []
    if type(number ** 0.5) == int:
        for dig in range(2,math.ceil(number ** 0.5) + 1):
            if len(k) > 3:
                k = []
                break
            if number % dig == 0:
                k.append(dig)
        if len(k) == 3:
            k = []
            print(number,max(k))