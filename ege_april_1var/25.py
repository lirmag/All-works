def dig(num):
    k = []
    i = 2
    while i**2 < num:
        if num % i == 0:
            k.append(i)
            k.append(num // i)
        i += 1
        if i ** 2 == num:
            k.append(i)
    k = sorted(k)
    if len(k) < 5:
        return 0
    m = 1
    for c in range(5):
        m *= k[c]
    return m


count = 0
for number in range(500000001,1000000000000000000000001):
    if count == 5:
        break
    if (dig(number) > 0) and (dig(number) < number):
        count += 1
        print(dig(number))
