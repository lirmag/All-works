import datetime
start = datetime.datetime.now()


def dig(number):
    k = [1,number]
    i = 2
    while i ** 2 < number:
        if number % i == 0:
            k.append(i)
            k.append(number // i)
        i += 1
        if i ** 2 == number:
            k.append(number)
    return sorted(k)


print(dig(10**8))
print(start - datetime.datetime.now())