import math


def delit(number):
    count = 0
    for dig in range(1,(math.ceil(number ** 0.5)) + 1):
        if number % dig == 0:
            a = (number // dig) - dig
            if (a > -1) and (a < 101):
                count += 1
                if count >= 3:
                    break
    return count


for number in range(1000000, 2000001):
    if delit(number) >= 3:
        print(number)



