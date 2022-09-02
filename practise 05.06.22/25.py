def digs(number):
    k = []
    i = 1
    while i ** 2 < number:
        if number % i == 0:
            if i % 2 != 0:
                k.append(i)
            if (number // i) % 2 != 0:
                k.append(number // i)
        i += 1
        if i ** 2 == number:
            if i % 2 != 0:
                k.append(i)

    return k


for x in range(45000032,50000001):
    if len(digs(x)) == 5:
        print(x,digs(x))

