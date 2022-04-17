def digs(number):
    i = 2
    k = []
    while i ** 2 < number:
        if number % i == 0:
            if (i % 10 == 7) and (i != 7):
                k.append(i)
            if ((number // i) != 7) and ((number // i) % 10 == 7):
                k.append(number // i)
        i += 1
        if (i**2 == number) and ((i**2) % 10 == 7) and (i**2 != 7):
            k.append(i)
    return sorted(k)


count = 0
for number in range(600001,100000000001):
    if count == 5:
        break
    if len(digs(number)) >= 1:
        count += 1
        print(number,digs(number)[0])