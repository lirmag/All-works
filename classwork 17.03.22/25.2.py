import math
def dig(number):
    k = []
    a = math.ceil(number // 2)
    for dig in range(a, 3, - 1):
        if len(k) == 2:
            break
        if number % dig == 0:
            k.append(dig)
    if len(k) == 2:
        return max(k) + min(k)
    else:
        return 0


count = 0
for number in range(11000001,10000000000000000001):
    b = dig(number)
    if count == 5:
        break
    if (b > 0) and (b < 10000):
        count += 1
        print(number,b)