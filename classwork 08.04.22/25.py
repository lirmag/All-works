def dig(number):
    k = [1]
    i = 2
    while i ** 2 < number:
        if number % i == 0:
            k.append(i)
            k.append(number // i)
        i += 1
        if i ** 2 == number:
            k.append(number)
    k = sorted(k)[::-1]
    if len(k) >= 2:
        return k[0] + k[1]
    else:
        return 0

count = 0
for num in range(11000001,10000000000000001):
    if count == 5:
        break
    if (dig(num) > 0) and (dig(num) < 10000):
        count += 1
        print(num,dig(num))

