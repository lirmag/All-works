def digs(number):
    i = 2
    k = []
    while i ** 2 < number:
        if number % i == 0:
            if (i != 8) and (i % 10 == 8):
                k.append(i)
            if ((number // i) != 8) and ((number // i) % 10 == 8):
                k.append(number // i)
        i += 1
        if (i ** 2 == number) and ((i**2) % 10 == 8) and (i**2 != 8):
            k.append(i)
    return sorted(k)


count = 0
for num in range(500001,1000000000000000):
    if count == 5:
        break
    if len(digs(num)) >= 1:
        count += 1
        print(num,digs(num)[0])

