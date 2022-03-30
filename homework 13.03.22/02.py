import math


def delit(number):
    k = []
    if type(number ** 0.5) == int:
        for dig in range(2,(number ** 0.5) + 1):
            if number % dig == 0:
                k.append(dig)
    return k


for number in range(123456789,223456790):
    ans = delit(number)
    if len(ans) == 3:
        print(number, max(ans))
