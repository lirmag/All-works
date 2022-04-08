def dig(number):
    k = []
    i = 2
    while i ** 2 < number:
        if (number % i == 0) and ((i % 10 == 8) or (number // i) % 10 == 8) and (i != 8):
            if (number // i) % 10 == 8:
                k.append(number // i)
            else:
                k.append(i)
            if (number % i == 0) and (i % 10 == 8) and (i != 8):
                k.append(i)
        i += 1
    return sorted(k)

count = 0
for num in range(500001,100000000000001):
    if count == 5:
        break
    if len(dig(num)) > 0:
        count += 1
        print(num,dig(num)[0])