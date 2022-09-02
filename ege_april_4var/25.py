import math
def dig(number):
    k = []
    i = 2
    while i ** 2 < number:
        if number % i == 0:
            k.append(number // i)
            k.append(i)
        i += 1
        if i ** 2 == number:
            k.append(i)
    k = sorted(k)
    if len(k) < 5:
        return 0
    return math.prod(k[0:5])


count = 0
for num in range(200000001,100000000000000):
    if count == 5:
        break
    if (dig(num) < num) and (dig(num) > 0):
        count += 1
        print(dig(num))

