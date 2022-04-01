def dig(number):
    k = []
    i = 2
    while i ** 2 < number:
        if number % i == 0:
            k.append(i)
            k.append(number // i)
        i += 1
        if i ** 2 == number:
            k.append(i)
    if len(k) == 0:
        return 0
    else:
        return max(k) + min(k)


count = 0
for number in range(700000, 10000000000):
    if count == 5:
        break
    if dig(number) % 10 == 8:
        count += 1
        print(number, dig(number))
